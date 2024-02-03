from rest_framework import serializers
from .models import Post, Category, Onbording, Register
from django.contrib.auth import get_user_model

User = get_user_model()


class OnbordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onbording
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
