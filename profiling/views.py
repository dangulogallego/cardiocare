from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm, PacienteForm, HabitsAntecedentsForm
from .models import Paciente, HabitsAntecedents

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
        if request.user.is_staff or request.user.is_superuser:
            pacientes = Paciente.objects.order_by('fecha_creacion')
            return render(request, 'index.html', {'pacientes': pacientes})
        else:
            return redirect('testsasa')
    else:
        return redirect('login')


def nuevo_paciente(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = PacienteForm(request.POST)
            if form.is_valid():
                paciente = form.save()
                paciente.save()
                return redirect('index')
        else:
            form = PacienteForm()
        return render(request, 'pacientes/form.html', {'form': form})
    else:
        return redirect('login')


def detalle_paciente(request, paciente_pk):
    if request.user.is_authenticated():
        paciente = Paciente.objects.get(pk=paciente_pk)
        return render(request, 'pacientes/detalle.html', {'paciente': paciente})
    else:
        return redirect('login')


def editar_paciente(request, paciente_pk):
    if request.user.is_authenticated():
        paciente = Paciente.objects.get(pk=paciente_pk)
        if request.method == 'POST':
            form = PacienteForm(request.POST, instance=paciente)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = PacienteForm(instance=paciente)
        return render(request, 'pacientes/edit.html', {'form': form, 'paciente': paciente})
    else:
        return redirect('login')


def habitos_antecedentes(request):
    if request.user.is_authenticated():
        if request.user.is_staff or request.user.is_superuser:
            habits = HabitsAntecedents.objects.order_by('fecha')
        else:
            habits = HabitsAntecedents.objects.order_by('fecha').filter(paciente__user=request.user)
        return render(request, 'habitsantecedents/index.html', {'habits': habits})
    else:
        return redirect('login')


def nuevo_habitos_antecedentes(request, paciente_pk):
    if request.user.is_authenticated():
        paciente = Paciente.objects.get(pk=paciente_pk)
        if request.method == 'POST':
            paciente = Paciente.objects.get(pk=paciente_pk)
            form = HabitsAntecedentsForm(request.POST)
            if form.is_valid() and paciente:
                counter = HabitsAntecedents.objects.filter(paciente=paciente).count() + 1
                habit = HabitsAntecedents(paciente=paciente)
                habit.tabaquismo = form.cleaned_data['tabaquismo']
                habit.diabetes = form.cleaned_data['diabetes']
                habit.hipertension = form.cleaned_data['hipertension']
                habit.iam = form.cleaned_data['iam']
                habit.seguimiento = counter
                habit.save()
                return redirect('index')
        else:
            form = HabitsAntecedentsForm()
        return render(request, 'habitsantecedents/form.html', {'form': form, 'paciente':paciente})
    else:
        return redirect('login')
