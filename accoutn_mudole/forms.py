from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput())
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=200, widget=forms.TextInput())
    image = forms.ImageField(required=False, widget=forms.FileInput())
    is_active = forms.BooleanField(
        blank=True, required=False, widget=forms.CheckboxInput())
    is_staff = forms.BooleanField(
        blank=True, required=False, widget=forms.CheckboxInput())
