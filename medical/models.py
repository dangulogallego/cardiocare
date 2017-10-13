# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profiling.models import Paciente, HabitsAntecedents

class PuntajeCategoria(models.Model):
    nombre = models.CharField(max_length=50, default="Default")
    minmala = models.IntegerField(default=1)
    maxmala = models.IntegerField(default=1)
    minbuena = models.IntegerField(default=1)
    maxbuena = models.IntegerField(default=1)
    def __unicode__(self):
        return self.nombre

class Observaciones(models.Model):
    categoria = models.ForeignKey(PuntajeCategoria)
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
            return 'Baja'
        elif self.resultado > 48 and self.resultado <= 72:
            return 'Media'
        elif self.resultado > 72 and self.resultado <= 96:
            return 'Buena'

    def calcularCategorias(self):
        data = {}
        answers = self.respuestas.order_by('pregunta__categoria')
        print data
        for answer in answers:
            key = str(answer.pregunta.categoria.pk)
            if key in data:
                points = data[key]['points'] + answer.valor
                data[key]['points'] = points
            else:
                adata = {
                    'category': answer.pregunta.categoria,
                    'points': answer.valor
                }
                data[key] = adata
        print data
        return data
