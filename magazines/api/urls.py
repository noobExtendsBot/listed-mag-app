from django.urls import path
from .views import MagazineListView
from magazines.views import MagazineDetailView

urlpatterns = [
    path('', MagazineListView.as_view()),
    path('<int:pk>/', MagazineDetailView.as_view()),

]
