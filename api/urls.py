from django.urls import path, include
from . import views


urlpatterns = [
    path('generics/', views.TodosGenericApiView.as_view()),
    path('generics/<int:pk>/', views.TodosGenericDetailsApiView.as_view()),
    path('users/', views.UserGenericApiView.as_view(), name='UserGenericApiView'),
]
