from django.urls import path, include
from . import views


urlpatterns = [
    path('onbording/', views.OnbordingGenericApiView.as_view()),
    path('onbording/<int:pk>/', views.OnbordingGenericDetailsApiView.as_view()),
    path('posts/', views.PostsGenericApiView.as_view()),
    path('posts/<int:pk>/', views.PostsGenericDetailsApiView.as_view()),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/<int:pk>/', views.RegisterDetailsView.as_view(), name='register'),
    path('select-country/', views.SelectCountryView.as_view(), name='select-country'),
    path('select-country/<int:pk>/', views.SelectCountryDetails.as_view()),
]
