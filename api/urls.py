from django.urls import path, include
from . import views


urlpatterns = [
    path('posts/', views.PostsGenericApiView.as_view()),
    path('posts/<int:pk>/', views.PostsGenericDetailsApiView.as_view()),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('users/', views.UserGenericApiView.as_view(), name='UserGenericApiView'),
]
