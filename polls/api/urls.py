from django.urls import path, re_path
from .views import QuestionList, QuestionDetail, ChoiceList, Vote  # VoteView


urlpatterns = [
    path('', QuestionList.as_view(), name="question-list"),
    path('<int:pk>/', QuestionDetail.as_view(), name="question-details"),
    path('<int:pk>/choices/', ChoiceList.as_view(), name="choice-details"),
    path('<int:pk1>/choices/<int:pk2>/', Vote.as_view(), name="vote-taken"),
    # path('registration/', include('rest_auth.registration.urls')),
    # path('registration/', RegisterView.as_view(), name='account_signup'),
    # re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),
    #  name='account_email_verification_sent'),
    # re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
    #  name='account_confirm_email'),
]
