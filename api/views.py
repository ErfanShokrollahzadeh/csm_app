from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views import View
from rest_framework.request import Request  # new
from rest_framework.response import Response  # new
from rest_framework import status  # new
from rest_framework.decorators import api_view  # new *
from rest_framework.views import APIView  # new *
from rest_framework import generics, mixins  # new *
from rest_framework import viewsets  # new * new
from .models import Post, Category, Onbording, CustomUser, SelectCountry, Topics, NewsScoure, FillProfile
from .serializer import PostSerializer, CategorySerializer, OnbordingSerializer, UserSerializer, SelectCountrySerializer, TopicsSerializer, NewsScoureSerializer, FillProfileSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class OnbordingGenericApiView(generics.ListCreateAPIView):
    queryset = Onbording.objects.all()
    serializer_class = OnbordingSerializer


class OnbordingGenericDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
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


class RegisterView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class RegisterDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class SelectCountryView(generics.ListCreateAPIView):
    queryset = SelectCountry.objects.all()
    serializer_class = SelectCountrySerializer


class SelectCountryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = SelectCountry.objects.all()
    serializer_class = SelectCountrySerializer


class TopicsView(generics.ListCreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer


class TopicsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer


class NewsScoureView(generics.ListCreateAPIView):
    queryset = NewsScoure.objects.all()
    serializer_class = NewsScoureSerializer


class NewsScoureDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsScoure.objects.all()
    serializer_class = NewsScoureSerializer


class FillProfileView(generics.ListCreateAPIView):
    queryset = FillProfile.objects.all()
    serializer_class = FillProfileSerializer


class FileProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = FillProfile.objects.all()
    serializer_class = FillProfileSerializer
