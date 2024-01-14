# myapp/urls.py
from django.urls import path
from .views import category, post, home

urlpatterns = [
    path('categories/', category, name='category-list'),
    path('posts/', post, name='post-list'),
]
