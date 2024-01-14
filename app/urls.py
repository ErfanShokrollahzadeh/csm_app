# myapp/urls.py
from django.urls import path
from .views import CategoryList, PostList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('posts/', PostList.as_view(), name='post-list'),
]
