# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from .models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Opcional.', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, required=False, help_text='Opcional.', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese un email válido.', widget=forms.EmailInput(attrs={'class':'form-control'}))
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control datepicker-register'}))
    genero = forms.ChoiceField(choices=GENERO, widget=forms.Select(attrs={'class':'form-control'}))
    telefono = forms.CharField(max_length=50, required=False, help_text='Opcional.', widget=forms.TextInput(attrs={'class':'form-control'}))
    estado_civil = forms.ChoiceField(choices=ESTADO_CIVL, widget=forms.Select(attrs={'class':'form-control'}))
    estrato = forms.ChoiceField(choices=ESTRATO, widget=forms.Select(attrs={'class':'form-control'}))
    facultad = forms.ModelChoiceField(queryset=Facultad.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    regimen_salud = forms.ModelChoiceField(queryset=RegimenSalud.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
        }

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'primer_apellido', 'segundo_apellido', 'cod_paciente', 'fecha_nacimiento', 'genero', 'telefono', 'estado_civil', 'estrato', 'facultad', 'regimen_salud')
        widgets = {
            'cod_paciente': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento' : forms.DateInput(format='%d/%m/%y', attrs={'class':'form-control datepicker'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'estado_civil': forms.Select(attrs={'class':'form-control'}),
            'estrato': forms.Select(attrs={'class':'form-control'}),
            'facultad': forms.Select(attrs={'class':'form-control'}),
            'regimen_salud': forms.Select(attrs={'class':'form-control'}),
        }


class HabitsAntecedentsForm(ModelForm):
    class Meta:
        model = HabitsAntecedents
        fields = ('tabaquismo', 'diabetes', 'hipertension', 'iam')
