# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.dispatch import receiver
from django.shortcuts import render, redirect
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Substitution, Mail
from django.db.models.signals import post_save
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib
from .models import *
from .forms import *
from profiling.models import Paciente

sg = sendgrid.SendGridAPIClient(apikey='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')


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
                return redirect('testsasa')
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
                return redirect('lipidicos')
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


@receiver(post_save, sender=Examen)
def send_email_lipid(sender, instance=None, created=False, **kwargs):
    if created:
        rcv = instance.paciente.calculateRCV()
        asa = instance.paciente.examenes.filter(tipo__nombre="Test Asa").order_by('seguimiento').first()
        data = {
          "personalizations": [
            {
              "to": [
                {
                  "email": instance.paciente.user.email
                }
              ],
              "substitutions": {
                "<%nombre%>": instance.paciente.nombre +
                                " " + instance.paciente.primer_apellido +
                                (" " + instance.paciente.segundo_apellido if instance.paciente.segundo_apellido else "" ),
                "<%asa_number%>": str(asa.resultado),
                "<%asa_conceptual%>": asa.calcularConceptual(),
                "<%risk_percentage%>": rcv['numeric'],
                "<%risk_concept%>": rcv['conceptual'],
                "<%observaciones%>": instance.paciente.getRecomendations(),
                "<%date%>": str(instance.fecha),
              },
              "subject": "Prueba"
            },
          ],
          "from": {
            "email": "hms@mail.com"
          },
          "template_id": "20215cda-dc28-4a8a-b9e1-9e42487e13ee"
        }
        try:
            response = sg.client.mail.send.post(request_body=data)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except urllib.HTTPError as e:
            print (e.read())
            exit()
