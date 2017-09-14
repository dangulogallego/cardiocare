# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profiling.models import Paciente, HabitsAntecedents

CHOICES = (
    (1, 'Nunca'),
    (2, 'Casi Nunca'),
    (3, 'Casi Siempre'),
    (4, 'Siempre'),
)

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
    p1 = models.IntegerField(choices=CHOICES)
    p2 = models.IntegerField(choices=CHOICES)
    p3 = models.IntegerField(choices=CHOICES)
    p4 = models.IntegerField(choices=CHOICES)
    p5 = models.IntegerField(choices=CHOICES)
    p6 = models.IntegerField(choices=CHOICES)
    p7 = models.IntegerField(choices=CHOICES)
    p8 = models.IntegerField(choices=CHOICES)
    p9 = models.IntegerField(choices=CHOICES)
    p10 = models.IntegerField(choices=CHOICES)
    p11 = models.IntegerField(choices=CHOICES)
    p12 = models.IntegerField(choices=CHOICES)
    p13 = models.IntegerField(choices=CHOICES)
    p14 = models.IntegerField(choices=CHOICES)
    p15 = models.IntegerField(choices=CHOICES)
    p16 = models.IntegerField(choices=CHOICES)
    p17 = models.IntegerField(choices=CHOICES)
    p18 = models.IntegerField(choices=CHOICES)
    p19 = models.IntegerField(choices=CHOICES)
    p20 = models.IntegerField(choices=CHOICES)
    p21 = models.IntegerField(choices=CHOICES)
    p22 = models.IntegerField(choices=CHOICES)
    p23 = models.IntegerField(choices=CHOICES)
    p24 = models.IntegerField(choices=CHOICES)
    resultado = models.IntegerField(default=0)
    nombre = models.CharField(max_length=10, default="Baja")
    fecha = models.DateField(auto_now=True)
    seguimiento = models.IntegerField(default=0)
