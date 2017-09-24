# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profiling.models import Paciente, HabitsAntecedents

class PuntajeCategoria(models.Model):
    categoria = models.IntegerField(default=1)
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

class CategoriaPregunta(models.Model):
    texto = models.CharField(max_length=50, default="Categoría")
    def __unicode__(self):
        return self.texto

class Pregunta(models.Model):
    texto = models.TextField(default="Default")
    opciones = models.ManyToManyField(OpcionPregunta, blank=True)
    categoria = models.ForeignKey(CategoriaPregunta, blank=True, null=True)
    def __unicode__(self):
        return self.texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, blank=True)
    valor = models.FloatField(blank=True, null=True)

class TipoExamen(models.Model):
    nombre = models.CharField(max_length=50, default="Test Asa")
    preguntas = models.ManyToManyField(Pregunta, blank=True)
    def __unicode__(self):
        return self.nombre

class Examen(models.Model):
    tipo = models.ForeignKey(TipoExamen, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, blank=True, null=True)
    resultado = models.IntegerField(default=0)
    fecha = models.DateField(auto_now=True)
    respuestas = models.ManyToManyField(Respuesta, blank=True)
    def __unicode__(self):
        return self.tipo.nombre + " - " + self.cod_paciente
