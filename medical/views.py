# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Observaciones, Examen
from .forms import ASATestForm
from profiling.models import Paciente

def observaciones(request):
    if request.user.is_authenticated():
        observaciones = Observaciones.objects.order_by('categoria')
        return render(request, 'observaciones/index.html', {'observaciones': observaciones})
    else:
        return redirect('login')

def test_asa(request):
    if request.user.is_authenticated():
        tests = Examen.objects.filter(tipo__nombre="Test Asa")
        return render(request, 'testsasa/index.html', {'tests': tests})
    else:
        return redirect('login')

def new_test_asa(request, paciente_pk):
    if request.user.is_authenticated():
        paciente = Paciente.objects.get(pk=paciente_pk)
        if request.method == 'POST':
            form = ASATestForm(request.POST, paciente=paciente)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = ASATestForm(paciente=paciente)
        return render(request, 'examenes/form.html', {'form': form, 'paciente': paciente})
    else:
        return redirect('login')
