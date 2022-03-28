from django.urls import path, re_path
# from rest_auth.registration.views import VerifyEmailView
from users.api.views import CustomRegisterView
from .views import login_view, FacebookLogin


urlpatterns = [
    path('', CustomRegisterView.as_view(), name="user-register"),
    path('facebook/login/', login_view, name="facebook-login"),
    path('facebook/login/class/', FacebookLogin.as_view(), name="facebook-test"),
    # name='account_confirm_email'),
    # path('registration/', include('rest_auth.registration.urls')),
    # path('registration/', RegisterView.as_view(), name='account_signup'),
    # re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),
    #  name='account_email_verification_sent'),
    # re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
    #  name='account_confirm_email'),
]
