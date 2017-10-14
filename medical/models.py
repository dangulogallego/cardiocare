# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profiling.models import Paciente, HabitsAntecedents
import json

class PuntajeCategoria(models.Model):
    nombre = models.CharField(max_length=50, default="Default")
    minmala = models.IntegerField(default=1)
    maxmala = models.IntegerField(default=1)
    minbuena = models.IntegerField(default=1)
    maxbuena = models.IntegerField(default=1)
    def __unicode__(self):
        return self.nombre

class Observaciones(models.Model):
    categoria = models.ForeignKey(PuntajeCategoria, related_name="observaciones")
    observacion = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return self.observacion

class OpcionPregunta(models.Model):
    texto = models.CharField(max_length=50, default="Default")
    valor = models.IntegerField(default=0)
    def __unicode__(self):
        return self.texto

class Pregunta(models.Model):
    slug = models.CharField(max_length=50, blank=True, null=True)
    texto = models.TextField(default="Default")
    opciones = models.ManyToManyField(OpcionPregunta, blank=True)
    categoria = models.ForeignKey(PuntajeCategoria, blank=True, null=True)
    def __unicode__(self):
        return self.texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, blank=True)
    valor = models.FloatField(blank=True, null=True)
    def __unicode__(self):
        return str(self.pregunta.pk) + " : " + str(self.valor)

    def value2Opcion(self):
        value = int(self.valor)
        opt = OpcionPregunta.objects.get(valor=value)
        return opt

class TipoExamen(models.Model):
    nombre = models.CharField(max_length=50, default="Test Asa")
    preguntas = models.ManyToManyField(Pregunta, blank=True)
    def __unicode__(self):
        return self.nombre

class Examen(models.Model):
    tipo = models.ForeignKey(TipoExamen, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, blank=True, null=True, related_name="examenes")
    resultado = models.IntegerField(default=0)
    fecha = models.DateField(auto_now=True)
    respuestas = models.ManyToManyField(Respuesta, blank=True)
    seguimiento = models.IntegerField(default=0)
    def __unicode__(self):
        return self.tipo.nombre + " - " + self.paciente.cod_paciente

    def calcularResultado(self):
        answers = self.respuestas.all()
        for ans in answers:
            self.resultado = self.resultado + int(ans.valor)
        self.save()
        return self

    def calcularConceptual(self):
        if self.resultado == 24:
            return 'Muy bajo'
        elif self.resultado > 24 and self.resultado <= 48:
            return 'Bajo'
        elif self.resultado > 48 and self.resultado <= 72:
            return 'Media'
        elif self.resultado > 72 and self.resultado <= 96:
            return 'Buena'

    def calcularCategorias(self):
        data = []
        tmp = {}
        answers = self.respuestas.order_by('pregunta__categoria')
        for answer in answers:
            if answer.pregunta.categoria:
                key = str(answer.pregunta.categoria.pk)
                if key in tmp:
                    points = tmp[key]['points'] + answer.valor
                    tmp[key]['points'] = points
                else:
                    adata = {
                        'points': answer.valor,
                        'cat_nombre': answer.pregunta.categoria.nombre,
                        'cat_minmala': answer.pregunta.categoria.minmala,
                        'cat_maxmala': answer.pregunta.categoria.maxmala,
                        'cat_minbuena': answer.pregunta.categoria.minbuena,
                        'cat_maxbuena': answer.pregunta.categoria.maxbuena,
                    }
                    tmp[key] = adata
                if answer.valor >= answer.pregunta.categoria.minmala and answer.valor <= answer.pregunta.categoria.maxmala:
                    tmp[key]['observaciones'] = ""
                    for recomendation in answer.pregunta.categoria.observaciones.all():
                        tmp[key]['observaciones'] += recomendation.observacion + ". "
                else:
                    tmp[key]['observaciones'] = "Estás haciendo un excelente trabajo"
        for dt in tmp:
            data.append(tmp[dt])
        return data

    def calcularByLipidCategorias(self):
        data = []
        tmp = {}
        asa_test = Examen.objects.filter(tipo__nombre="Test Asa").order_by('seguimiento').first()
        answers = asa_test.respuestas.order_by('pregunta__categoria')

        for answer in answers:
            key = str(answer.pregunta.categoria.pk)
            if key in tmp:
                points = tmp[key]['points'] + answer.valor
                tmp[key]['points'] = points
            else:
                adata = {
                    'points': answer.valor,
                    'cat_nombre': answer.pregunta.categoria.nombre,
                    'cat_minmala': answer.pregunta.categoria.minmala,
                    'cat_maxmala': answer.pregunta.categoria.maxmala,
                    'cat_minbuena': answer.pregunta.categoria.minbuena,
                    'cat_maxbuena': answer.pregunta.categoria.maxbuena,
                }
                tmp[key] = adata
            if answer.valor >= answer.pregunta.categoria.minmala and answer.valor <= answer.pregunta.categoria.maxmala:
                tmp[key]['observaciones'] = ""
                for recomendation in answer.pregunta.categoria.observaciones.all():
                    tmp[key]['observaciones'] += recomendation.observacion + ". "
            else:
                tmp[key]['observaciones'] = "Estás haciendo un excelente trabajo"

        for dt in tmp:
            data.append(tmp[dt])

        print data
        return data
