from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_todos, name='all_todos'),
    path('<pk>', views.todo_detail_view, name='todo_detail_view'),

]
