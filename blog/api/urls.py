from django.urls import path
from .views import PostList, PostDetail, CategoriesList, CommentDetail, CommentListView, CategoriesDetailView, CategoryPostList, CommentPost


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('<int:pk>/comments/', CommentListView.as_view()),
    path('<int:pk>/comments/post/', CommentPost.as_view()),
    path('categories/', CategoriesList.as_view()),
    path('categories/post/list/<int:pk>/', CategoryPostList.as_view()),
    path('categories/<int:pk>/', CategoriesDetailView.as_view()),
]