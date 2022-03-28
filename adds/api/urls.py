from django.urls import path
from .views import AddListView


urlpatterns = [
    path('', AddListView.as_view()),
]
