from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # import the CustomUser model


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser  # use CustomUser instead of User
        fields = ('username', 'password')
