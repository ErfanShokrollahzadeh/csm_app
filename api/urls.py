from django.urls import path
from . import views


urlpatterns = [
    path('generics/', views.TodosGenericApiView.as_view(),
         name='TodosGenericApiView'),
    path('generics/<int:pk>/', views.TodosGenericDetailsApiView.as_view(),
         name='TodosGenericDetailsApiView'),

]
