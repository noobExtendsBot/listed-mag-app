from rest_auth.registration.views import RegisterView, SocialLoginView
from users.models import CustomUser
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from datetime import datetime
from django.http import JsonResponse
import facebook
from rest_framework.authtoken.models import Token
import json
from django.views.decorators.csrf import csrf_exempt



class CustomRegisterView(RegisterView):
    queryset = CustomUser.objects.all()



class TemplateView():
    pass


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


@csrf_exempt
def login_view(request):
    """
        FUNCTION FOR LOGIN AND REGISTER WITH FACEBOOK
    """
    data = json.loads(request.body.decode('utf-8'))
    access_token = data.get('access_token')
    # access_token = request.POST['access_token']
    new_user = False

    try:
        graph = facebook.GraphAPI(access_token=access_token)
        user_info = graph.get_object(
            id='me',
            fields='first_name, middle_name, last_name, email, id')
        # print(user_info)
        # print(user_info.get('id'))
    except facebook.GraphAPIError:
        return JsonResponse({'error': 'Invalid data'}, safe=False)

    try:
        user = CustomUser.objects.get(facebook_id=user_info.get('id'))
        # print("user new", user)
    except CustomUser.DoesNotExist:
        password = CustomUser.objects.make_random_password()
        user = CustomUser(
            first_name=user_info.get('first_name'),
            last_name=user_info.get('last_name'),
            email=user_info.get('email') or '{0} without email'.format(user_info.get('last_name')),
            facebook_id=user_info.get('id'),
            is_active=True
        )
        user.set_password(password)
        user.save()
        new_user = True
    token = Token.objects.get(user=user).key

    if token:
        return JsonResponse({'key': token, 'new_user': new_user}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid data'}, safe=False)