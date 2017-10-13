# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime

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
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    nombre = models.CharField(max_length=50, default="Diego")
    primer_apellido = models.CharField(max_length=50, default="Angulo")
    segundo_apellido = models.CharField(max_length=50, null=True, blank=True)
    cod_paciente = models.CharField(max_length=50, default="123456789", unique=True)
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

    def age(self):
        return int((datetime.date.today() - self.fecha_nacimiento).days / 365.25  )

    def age_points(self):
        if self.age() < 40:
            return 0
        elif self.age() > 39 and self.age() < 45:
            return 6
        elif self.age() > 44 and self.age() < 50:
            return 11
        elif self.age() > 49 and self.age() < 55:
            return 16
        elif self.age() > 54 and self.age() < 60:
            return 21
        else:
            return 26

    def smoke_points(self):
        last_habit = self.habits.order_by('seguimiento').first()
        if last_habit:
            return 8 if last_habit.tabaquismo else 0
        return 0

    def has_diabetes(self):
        last_habit = self.habits.order_by('seguimiento').first()
        if last_habit:
            return last_habit.diabetes
        return False

    def diabetes_points(self):
        last_habit = self.habits.order_by('seguimiento').first()
        if last_habit:
            return 6 if last_habit.diabetes else 0
        return 0

    def iam_points(self):
        last_habit = self.habits.order_by('seguimiento').first()
        if last_habit:
            return 8 if last_habit.iam else 0
        return 0

    def test_question_val(self, key, answers):
        for answer in answers:
            if answer.pregunta.slug == key:
                return answer.valor
        return False

    def ldl_points(self):
        lipid_test = self.examenes.filter(tipo__nombre="Examen Lipídico").order_by('seguimiento').first()
        if lipid_test:
            value = self.test_question_val('ldl', lipid_test.respuestas.all())
            if value < 100:
                return 0
            elif value > 99 and value < 130:
                return 5
            elif value > 129 and value < 160:
                return 10
            elif value > 159 and value < 190:
                return 14
            else:
                return 20
        return 0

    def hdl_points(self):
        lipid_test = self.examenes.filter(tipo__nombre="Examen Lipídico").order_by('seguimiento').first()
        if lipid_test:
            value = self.test_question_val('hdl', lipid_test.respuestas.all())
            if value < 35:
                return 11
            elif value > 34 and value < 45:
                return 8
            elif value > 44 and value < 55:
                return 10
            else:
                return 0
        return 0

    def trigliceridos_points(self):
        lipid_test = self.examenes.filter(tipo__nombre="Examen Lipídico").order_by('seguimiento').first()
        if lipid_test:
            value = self.test_question_val('trigliceridos', lipid_test.respuestas.all())
            if value < 100:
                return 0
            elif value > 99 and value < 150:
                return 2
            elif value > 149 and value < 200:
                return 3
            else:
                return 4
        return 0

    def pas_points(self):
        lipid_test = self.examenes.filter(tipo__nombre="Examen Lipídico").order_by('seguimiento').first()
        if lipid_test:
            value = self.test_question_val('pas', lipid_test.respuestas.all())
            if value < 120:
                return 0
            elif value > 119 and value < 130:
                return 2
            elif value > 129 and value < 140:
                return 3
            elif value > 139 and value < 160:
                return 5
            else:
                return 8
        return 0

    def calculateRCVCount(self):
        points = self.age_points() + self.smoke_points() + self.diabetes_points() + self.iam_points() + self.ldl_points() + self.hdl_points() + self.trigliceridos_points() + self.pas_points()
        return points

    def calculateRCVF(self):
        if self.calculateRCVCount() < 20:
            return 0
        if self.calculateRCVCount() == 20:
            return 1
        if self.calculateRCVCount() == 21:
            return 1.1
        if self.calculateRCVCount() == 22:
            return 1.2
        if self.calculateRCVCount() == 23:
            return 1.3
        if self.calculateRCVCount() == 24:
            return 1.4
        if self.calculateRCVCount() == 25:
            return 1.6
        if self.calculateRCVCount() == 26:
            return 1.7
        if self.calculateRCVCount() == 27:
            return 1.8
        if self.calculateRCVCount() == 28:
            return 1.9
        if self.calculateRCVCount() == 29:
            return 2.3
        if self.calculateRCVCount() == 30:
            return 2.4
        if self.calculateRCVCount() == 31:
            return 2.8
        if self.calculateRCVCount() == 32:
            return 2.9
        if self.calculateRCVCount() == 33:
            return 3.3
        if self.calculateRCVCount() == 34:
            return 3.5
        if self.calculateRCVCount() == 35:
            return 4
        if self.calculateRCVCount() == 36:
            return 4.2
        if self.calculateRCVCount() == 37:
            return 4.8
        if self.calculateRCVCount() == 38:
            return 5.1
        if self.calculateRCVCount() == 39:
            return 5.7
        if self.calculateRCVCount() == 40:
            return 6.1
        if self.calculateRCVCount() == 41:
            return 7.0
        if self.calculateRCVCount() == 42:
            return 7.4
        if self.calculateRCVCount() == 43:
            return 8.0
        if self.calculateRCVCount() == 44:
            return 8.8
        if self.calculateRCVCount() == 45:
            return 10.2
        if self.calculateRCVCount() == 46:
            return 10.5
        if self.calculateRCVCount() == 47:
            return 10.7
        if self.calculateRCVCount() == 48:
            return 12.8
        if self.calculateRCVCount() == 49:
            return 13.2
        if self.calculateRCVCount() == 50:
            return 15.5
        if self.calculateRCVCount() == 51:
            return 16.8
        if self.calculateRCVCount() == 52:
            return 17.5
        if self.calculateRCVCount() == 53:
            return 19.6
        if self.calculateRCVCount() == 54:
            return 21.7
        if self.calculateRCVCount() == 55:
            return 22.2
        if self.calculateRCVCount() == 56:
            return 23.8
        if self.calculateRCVCount() == 57:
            return 25.1
        if self.calculateRCVCount() == 58:
            return 28.0
        if self.calculateRCVCount() == 59:
            return 29.4
        if self.calculateRCVCount() >= 60:
            return 30
        return 0

    def getRisk(self, points):
        if points < 10:
            return 'Riesgo Bajo'
        elif points >= 10 and points < 20:
            return 'Riesgo Medio'
        else:
            return 'Riesgo Alto'

    def calculateRCV(self):
        data = {}
        if self.genero == 'F' and self.has_diabetes():
            rnum = self.calculateRCVF() * 0.25
        else:
            rnum = self.calculateRCVF()
        data['numeric'] = str(self.calculateRCVCount()) + '/91 (' + str(rnum) + ')'
        data['conceptual'] = self.getRisk(rnum)
        data['percentage'] = rnum
        return data


class HabitsAntecedents(models.Model):
    paciente = models.ForeignKey(Paciente, related_name="habits")
    tabaquismo = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    hipertension = models.BooleanField(default=False)
    iam = models.BooleanField(default=False)
    seguimiento = models.IntegerField(default=1)
    fecha = models.DateField(auto_now=True)
    def __unicode__(self):
        return self.paciente.cod_paciente
