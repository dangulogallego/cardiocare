from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm, PacienteForm
from .models import Paciente

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    if request.user.is_authenticated():
        pacientes = Paciente.objects.order_by('fecha_creacion')
        return render(request, 'index.html', {'pacientes': pacientes})
    else:
        return redirect('login')

def nuevo_paciente(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = PacienteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = PacienteForm()
        return render(request, 'pacientes/form.html', {'form': form})
    else:
        return redirect('login')
