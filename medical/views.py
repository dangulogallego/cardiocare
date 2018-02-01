# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.dispatch import receiver
from django.shortcuts import render, redirect
import sendgrid
import os
import math
from sendgrid.helpers.mail import Email, Content, Substitution, Mail
from django.db.models.signals import post_save
from django.contrib import messages
import datetime
from django.conf import settings
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib
from .models import *
from .forms import *
from profiling.models import Paciente, HabitsAntecedents

sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)


def graphics(request):
    if request.user.is_authenticated():
        pacientes = Paciente.objects.order_by('fecha_creacion')
        x = 0
        x2 = 0
        y = 0
        y2 = 0
        xy = 0
        n = 0
        promX = 0
        promY = 0
        sx = 0
        sy = 0
        rxy = 0
        data = []
        # Se recorre cada paciente
        for paciente in pacientes:
            # Se trae el ultimo examen lipido de cada paciente
            last_lipid = Examen.objects.filter(tipo__nombre="Examen Lipídico").filter(paciente__user=paciente.user).order_by('seguimiento').last()
            if last_lipid:
                # se busca el test asa relacionado con el examen lipido
                last_asa = paciente.examenes.filter(tipo__nombre="Test Asa", seguimiento=last_lipid.seguimiento).first()
                x += last_asa.resultado
                x2 += math.pow(last_asa.resultado, 2)
                y += paciente.calculateRCVCount(last_asa.seguimiento)
                y2 += math.pow(paciente.calculateRCVCount(last_asa.seguimiento), 2)
                xy += last_asa.resultado * paciente.calculateRCVCount(last_asa.seguimiento)
                data.append([last_asa.resultado, paciente.calculateRCVCount(last_asa.seguimiento)])
                n += 1
        promX = x / n
        promY = y / n
        sx = math.sqrt((x2/n) - math.pow(promX, 2))
        sy = math.sqrt((y2/n) - math.pow(promY, 2))
        rxy = ((xy / n) - (promX * promY)) / (sx * sy)
        print data
        print rxy
        return render(request, 'graphics/index.html', {'values': [[80,23], [37, 53], [72, 40], [24, 91]], 'pacientes': pacientes, 'pearson': rxy})
    else:
        return redirect('login')


def observaciones(request):
    if request.user.is_authenticated():
        observaciones = Observaciones.objects.order_by('categoria')
        return render(request, 'observaciones/index.html', {'observaciones': observaciones})
    else:
        return redirect('login')


def detalle_observacion(request, observacion_pk):
    if request.user.is_authenticated():
        observacion = Observaciones.objects.get(pk=observacion_pk)
        return render(request, 'observaciones/detalle.html', {'observacion': observacion})
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

                # Se valida el seguimiento
                counterHab = HabitsAntecedents.objects.filter(paciente=paciente).count()
                counterLipid = Examen.objects.filter(paciente=paciente).filter(tipo__nombre="Examen Lipídico").count()
                counterAsa = Examen.objects.filter(paciente=paciente).filter(tipo__nombre="Test Asa").count() + 1
                if counterHab == counterAsa:
                    test = Examen(tipo=asa_type, paciente=paciente, seguimiento=counterAsa)
                    test.save()
                    for field in form:
                        question = asa_type.preguntas.get(pk=field.name)
                        value = form.cleaned_data[field.name]
                        if question:
                            answer = Respuesta(pregunta=question, valor=value)
                            answer.save()
                            test.respuestas.add(answer)
                    test.calcularResultado()
                    return redirect('testsasa')
                elif counterAsa > counterHab and counterHab == counterLipid:
                    messages.error(request, 'Debes ingresar primero la información de tus hábitos y antecedentes.')
                    form = ASATestForm(paciente=paciente)
                else:
                    messages.error(request, 'Ya has respondido el Test ASA por favor, procede a ingresar los resultados de tu examen lipídico.')
                    form = ASATestForm(paciente=paciente)
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
                # Se valida el seguimiento
                counterAsa = Examen.objects.filter(paciente=paciente).filter(tipo__nombre="Test Asa").count()
                counterLipid = Examen.objects.filter(paciente=paciente).filter(tipo__nombre="Examen Lipídico").count() + 1
                if counterAsa == counterLipid:
                    test = Examen(tipo=fatty_type, paciente=paciente, seguimiento=counterLipid)
                    test.save()
                    for field in form:
                        question = fatty_type.preguntas.get(pk=field.name)
                        value = form.cleaned_data[field.name]
                        if question:
                            answer = Respuesta(pregunta=question, valor=value)
                            answer.save()
                            test.respuestas.add(answer)
                    # Llamar a Sendgrid
                    send_mail_lipid(paciente, counterLipid)
                    return redirect('lipidicos')
                else:
                    messages.error(request, 'Debes ingresar primero la información del Test ASA.')
                    form = FattyTestForm(paciente=paciente)
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


def send_mail_lipid (paciente, seguimiento):
    if paciente and seguimiento:
        rcv = paciente.calculateRCV(seguimiento)
        asa = paciente.examenes.filter(tipo__nombre="Test Asa", seguimiento=seguimiento).first()
        data = {
            "personalizations": [
                {
                    "to": [
                        {
                            "email": "diegofer_1018@hotmail.com"
                            # "email":  paciente.user.email
                        }
                    ],
                    "substitutions": {
                        "<%nombre%>": paciente.nombre +
                        " " + paciente.primer_apellido +
                        (" " + paciente.segundo_apellido if paciente.segundo_apellido else ""),
                        "<%asa_number%>": str(asa.resultado),
                        "<%asa_conceptual%>": asa.calcularConceptual(),
                        "<%risk_percentage%>": rcv['numeric'],
                        "<%risk_concept%>": rcv['conceptual'],
                        "<%observaciones%>": paciente.getRecomendations(seguimiento),
                        "<%date%>": str(datetime.date.today()),
                    },
                    "subject": "Examen de riesgo cardiovascular"
                },
            ],
            "from": {
                "email": "cardiocare@gmail.com"
            },
            "template_id": "20215cda-dc28-4a8a-b9e1-9e42487e13ee"
        }
        try:
            print("Send SendGrid")
            response = sg.client.mail.send.post(request_body=data)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except urllib.HTTPError as e:
            print (e.read())
            exit()
