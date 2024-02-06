from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views import View
from .forms import RegisterForm


class Register(View):
    def get(self, request):
        # register_form = RegisterForm()
        # context = {
        #     'register_form': register_form,
        # }
        # return render(request, 'register.html', context)
        pass

    def post(self, request):
        # register_form = RegisterForm(request.POST, request.FILES)
        # if register_form.is_valid():
        #     user = get_user_model()
        #     user.objects.create_user(
        #         username=register_form.cleaned_data['username'],
        #         password=register_form.cleaned_data['password'],
        #         phone_number=register_form.cleaned_data['phone_number'],
        #         image=register_form.cleaned_data['image'],
        #         is_active=register_form.cleaned_data['is_active'],
        #         is_staff=register_form.cleaned_data['is_staff'],
        #     )
        #     return render(request, 'register.html')
        # else:
        #     context = {
        #         'register_form': register_form,
        #     }
        #     return render(request, 'register.html', context)
        pass
