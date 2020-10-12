from django import forms
from .models import UserProfileInfo, domainUser
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class DomainForm(forms.ModelForm):
    domain = forms.CharField(max_length=10, label='Dominio')
    desciprion = forms.CharField(label='descripcion')
    domain_user = forms.CharField(max_length=8, label='Usuario')
    passwrd = forms.CharField(
        widget=forms.PasswordInput(), max_length=10, label='contraseña')

    class Meta():
        model = domainUser
        exclude = ('user',)
