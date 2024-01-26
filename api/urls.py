from django.urls import path
from . import views


urlpatterns = [
    path('cbv/', views.TodosListApiView.as_view(), name='ManageTodoApiView'),
    path('cbv/<int:pk>/', views.TodosDetailApiView.as_view(),
         name='TodoDetailApiView'),

]
