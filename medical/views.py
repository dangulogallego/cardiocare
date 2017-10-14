# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from .forms import *
from profiling.models import Paciente


def observaciones(request):
    if request.user.is_authenticated():
        observaciones = Observaciones.objects.order_by('categoria')
        return render(request, 'observaciones/index.html', {'observaciones': observaciones})
    else:
        return redirect('login')


def test_asa(request):
    if request.user.is_authenticated():
        if request.user.is_staff or request.user.is_superuser:
            tests = Examen.objects.filter(tipo__nombre="Test Asa")
        else:
            tests = Examen.objects.filter(tipo__nombre="Test Asa").filter(paciente__user=request.user)
        return render(request, 'testsasa/index.html', {'tests': tests})
    else:
        return redirect('login')


def new_test_asa(request, paciente_pk):
    if request.user.is_authenticated():
        paciente = Paciente.objects.get(pk=paciente_pk)
        if request.method == 'POST':
            form = ASATestForm(request.POST, paciente=paciente)
            if form.is_valid():
                asa_type = TipoExamen.objects.get(nombre="Test Asa")
                counter = Examen.objects.filter(paciente=paciente).filter(tipo__nombre="Test Asa").count() + 1
                test = Examen(tipo=asa_type, paciente=paciente, seguimiento=counter)
                test.save()
                for field in form:
                    question = asa_type.preguntas.get(pk=field.name)
                    value = form.cleaned_data[field.name]
                    if question:
                        answer = Respuesta(pregunta=question, valor=value)
                        answer.save()
                        test.respuestas.add(answer)
                test.calcularResultado()
                return redirect('index')
        else:
            form = ASATestForm(paciente=paciente)
        return render(request, 'examenes/form.html', {'form': form, 'paciente': paciente, 'title': 'Test ASA'})
    else:
        return redirect('login')


def test_fatty(request):
    if request.user.is_authenticated():
        if request.user.is_staff or request.user.is_superuser:
            tests = Examen.objects.filter(tipo__nombre="Examen Lipídico")
        else:
            tests = Examen.objects.filter(tipo__nombre="Examen Lipídico").filter(paciente__user=request.user)
        return render(request, 'lipidicos/index.html', {'tests': tests})
    else:
        return redirect('login')


def new_test_fatty(request, paciente_pk):
    if request.user.is_authenticated():
        paciente = Paciente.objects.get(pk=paciente_pk)
        if request.method == 'POST':
            form = FattyTestForm(request.POST, paciente=paciente)
            if form.is_valid():
                fatty_type = TipoExamen.objects.get(nombre="Examen Lipídico")
                counter = Examen.objects.filter(paciente=paciente).filter(tipo__nombre="Examen Lipídico").count() + 1
                test = Examen(tipo=fatty_type, paciente=paciente, seguimiento=counter)
                test.save()
                for field in form:
                    question = fatty_type.preguntas.get(pk=field.name)
                    value = form.cleaned_data[field.name]
                    if question:
                        answer = Respuesta(pregunta=question, valor=value)
                        answer.save()
                        test.respuestas.add(answer)
                return redirect('index')
        else:
            form = FattyTestForm(paciente=paciente)
        return render(request, 'examenes/form.html', {'form': form, 'paciente': paciente, 'title': 'Examen Lipídico'})
    else:
        return redirect('login')


def get_single_test(request, test_pk):
    if request.user.is_authenticated():
        test = Examen.objects.get(pk=test_pk)
        if test.tipo.nombre == "Test Asa":
            return render(request, 'examenes/asa_detalle.html', {'test': test})
        else:
            return render(request, 'examenes/lipid_detalle.html', {'test': test})
    else:
        return redirect('login')
