# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Opcional.')
    last_name = forms.CharField(max_length=50, required=False, help_text='Opcional.')
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese un email válido.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
