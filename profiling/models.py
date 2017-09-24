# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

GENERO = (
    ('F', 'Femenino'),
    ('M', 'Masculino'),
)

ESTADO_CIVL = (
    ('Unión Libre', 'Unión Libre'),
    ('Casado', 'Casado'),
    ('Soltero', 'Soltero'),
    ('Divorciado', 'Divorciado'),
    ('Viudo', 'Viudo'),
)

ESTRATO = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)

class RegimenSalud(models.Model):
    nombre = models.TextField(max_length=50)
    def __unicode__(self):
        return self.nombre

class Facultad(models.Model):
    nombre = models.TextField(max_length=50)
    def __unicode__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=50, default="Diego")
    primer_apellido = models.CharField(max_length=50, default="Angulo")
    segundo_apellido = models.CharField(max_length=50, default="Perez")
    cod_paciente = models.CharField(max_length=50, default="123456789")
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO)
    telefono = models.CharField(max_length=30)
    estado_civil = models.CharField(max_length=35, choices=ESTADO_CIVL)
    estrato = models.CharField(max_length=1, choices=ESTRATO)
    facultad = models.ForeignKey(Facultad, null=True)
    regimen_salud = models.ForeignKey(RegimenSalud, null=True)
    fecha_creacion = models.DateField(auto_now=True)
    def __unicode__(self):
        return self.cod_paciente

class HabitsAntecedents(models.Model):
    paciente = models.ForeignKey(Paciente)
    tabaquismo = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    hipertension = models.BooleanField(default=False)
    iam = models.BooleanField(default=False)
    seguimiento = models.IntegerField(default=1)
    fecha = models.DateField(auto_now=True)
