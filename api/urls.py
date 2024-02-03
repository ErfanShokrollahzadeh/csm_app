from django.urls import path, include
from . import views


urlpatterns = [
    path('onbording/', views.OnbordingGenericApiView.as_view()),
    path('onbording/<int:pk>/', views.OnbordingGenericDetailsApiView.as_view()),
    path('posts/', views.PostsGenericApiView.as_view()),
    path('posts/<int:pk>/', views.PostsGenericDetailsApiView.as_view()),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('register/', views.RegisterUser.as_view(), name='register-user'),
]
