from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request  # new
from rest_framework.response import Response  # new
from rest_framework import status  # new
from rest_framework.decorators import api_view  # new *
from rest_framework.views import APIView  # new *
from rest_framework import generics, mixins  # new *
from rest_framework import viewsets  # new * new
from .models import Post, Category, Onbording
from .serializer import PostSerializer, UserSerializer, CategorySerializer, OnbordingSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class OnbordingGenericApiView(generics.ListCreateAPIView):
    queryset = Onbording.objects.all()
    serializer_class = OnbordingSerializer


class PostsGenericApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostsGenericDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
