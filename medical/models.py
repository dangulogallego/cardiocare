# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profiling.models import Paciente, HabitsAntecedents

class Examen(models.Model):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateField(auto_now=True)
    seguimiento = models.IntegerField(default=1)
    colesterolldl = models.FloatField(default=0)
    colesterolhdl = models.FloatField(default=0)
    trigliceridos = models.FloatField(default=0)
    pas = models.FloatField(default=0)
    def __unicode__(self):
        return self.paciente.nombre

class PuntajeCategoria(models.Model):
    categoria = models.IntegerField(default=1)
    nombre = models.CharField(max_length=50, default="Diego")
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

class TestAsa(models.Model):
    paciente = models.ForeignKey(Paciente)
    p1 = models.IntegerField(default=0)
    p2 = models.IntegerField(default=0)
    p3 = models.IntegerField(default=0)
    p4 = models.IntegerField(default=0)
    p5 = models.IntegerField(default=0)
    p6 = models.IntegerField(default=0)
    p7 = models.IntegerField(default=0)
    p8 = models.IntegerField(default=0)
    p9 = models.IntegerField(default=0)
    p10 = models.IntegerField(default=0)
    p11 = models.IntegerField(default=0)
    p12 = models.IntegerField(default=0)
    p13 = models.IntegerField(default=0)
    p14 = models.IntegerField(default=0)
    p15 = models.IntegerField(default=0)
    p16 = models.IntegerField(default=0)
    p17 = models.IntegerField(default=0)
    p18 = models.IntegerField(default=0)
    p19 = models.IntegerField(default=0)
    p20 = models.IntegerField(default=0)
    p21 = models.IntegerField(default=0)
    p22 = models.IntegerField(default=0)
    p23 = models.IntegerField(default=0)
    p24 = models.IntegerField(default=0)
    resultado = models.IntegerField(default=0)
    nombre = models.CharField(max_length=10, default="Baja")
    fecha = models.DateField(auto_now=True)
    seguimiento = models.IntegerField(default=0)
