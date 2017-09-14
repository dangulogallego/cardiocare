# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Examen, Observaciones, TestAsa

def examenes(request):
    if request.user.is_authenticated():
        examenes = Examen.objects.order_by('fecha')
        return render(request, 'examenes/index.html', {'examenes': examenes})
    else:
        return redirect('login')

def observaciones(request):
    if request.user.is_authenticated():
        observaciones = Observaciones.objects.order_by('categoria')
        return render(request, 'observaciones/index.html', {'observaciones': observaciones})
    else:
        return redirect('login')

def testasa(request):
    if request.user.is_authenticated():
        tests = TestAsa.objects.order_by('fecha')
        return render(request, 'testsasa/index.html', {'tests': tests})
    else:
        return redirect('login')
