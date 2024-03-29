from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.views import View


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class Register(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form,
        }
        return render(request, 'register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            user.is_active = True
            user.is_staff = False
            user.save()
            # redirect to login page after successful registration
            return redirect('login')
        else:
            context = {
                'register_form': register_form,
            }
            return render(request, 'register.html', context)
