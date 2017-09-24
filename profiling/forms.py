# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from .models import Paciente

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Opcional.')
    last_name = forms.CharField(max_length=50, required=False, help_text='Opcional.')
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese un email válido.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'primer_apellido', 'segundo_apellido', 'cod_paciente', 'fecha_nacimiento', 'genero', 'telefono', 'estado_civil', 'estrato', 'facultad', 'regimen_salud')
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'cod_paciente': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker form-control'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'estado_civil': forms.Select(attrs={'class':'form-control'}),
            'estrato': forms.Select(attrs={'class':'form-control'}),
            'facultad': forms.Select(attrs={'class':'form-control'}),
            'regimen_salud': forms.Select(attrs={'class':'form-control'}),
        }
