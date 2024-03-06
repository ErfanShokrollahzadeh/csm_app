from rest_framework import serializers
from .models import Post, Category, Onbording, CustomUser, SelectCountry, Topics, NewsScoure
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class SelectCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectCountry
        fields = '__all__'


class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'


class NewsScoureSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsScoure
        fields = '__all__'
