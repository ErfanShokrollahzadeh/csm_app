from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    Posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
