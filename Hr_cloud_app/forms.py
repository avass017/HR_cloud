from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Hr_cloud_app.views import Login, hr


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ['username', 'password1', 'password2']


class HrRegister(forms.ModelForm):
    class Meta:
        model = hr
        fields = ['Name', 'email','phone_number','department','document']


