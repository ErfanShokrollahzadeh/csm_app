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
    path('topics/', views.TopicsView.as_view(), name='topics'),
    path('topics/<int:pk>/', views.TopicsView.as_view(), name='topics'),
    path('news_scoure/', views.NewsScoureView.as_view(), name='news_scoure'),
    path('news_scoure/<int:pk>/', views.NewsScoureDetails.as_view()),
    path('fill-profile/', views.FillProfileView.as_view(), name='fill-profile'),
    path('fill-profile/<int:pk>/', views.FileProfileDetails.as_view()),
]
