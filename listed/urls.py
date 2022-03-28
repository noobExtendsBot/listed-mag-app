from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import confirm_email as allauthemailconfirmation
from .views import VerifyEmailView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^rest/auth/account-confirm-email/(?P<pk>[0-9]+)/$', allauthemailconfirmation,
         name='account_confirm_email'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
        name='account_confirm_email'),
    path('rest/auth/', include('rest_auth.urls')),
    path('api/users/', include('users.api.urls')),
    path('polls/', include('polls.api.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('blog/', include('blog.api.urls')),
    path('adds/', include('adds.api.urls')),
    # path('files/magazines/', include('frontend.urls')),
    path('files/magazines/', include('magazines.api.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#         urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
