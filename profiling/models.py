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

    def getRecomendations(self, seguimiento):
        tmp = {}
        observaciones = ""
        asa_test = self.examenes.filter(tipo__nombre="Test Asa", seguimiento=seguimiento).first()
        if asa_test:
            answers = asa_test.respuestas.order_by('pregunta__categoria')
        else:
            asa_test = self.examenes.filter(tipo__nombre="Test Asa").order_by("seguimiento").last()
            answers = asa_test.respuestas.order_by('pregunta__categoria')
        for answer in answers:
            if answer.pregunta.categoria:
                key = str(answer.pregunta.categoria.pk)
                if key in tmp:
                    points = tmp[key]['points'] + answer.valor
                    tmp[key]['points'] = points
                else:
                    adata = {
                        'points': answer.valor,
                        'cat': answer.pregunta.categoria,
                        'cat_nombre': answer.pregunta.categoria.nombre,
                        'cat_minmala': answer.pregunta.categoria.minmala,
                        'cat_maxmala': answer.pregunta.categoria.maxmala,
                        'cat_minbuena': answer.pregunta.categoria.minbuena,
                        'cat_maxbuena': answer.pregunta.categoria.maxbuena,
                    }
                    tmp[key] = adata

        for cat in tmp:
            keyCat = str(tmp[cat]['cat'].pk)
            if tmp[cat]['points'] >= tmp[cat]['cat_minmala'] and tmp[cat]['points'] <= tmp[cat]['cat_maxmala']:
                tmp[keyCat]['observaciones'] = ""
                for recomendation in tmp[cat]['cat'].observaciones.all():
                    observaciones += recomendation.observacion + ". \n"

        return observaciones

    def smoke_points(self, seguimiento):
        last_habit = self.habits.filter(seguimiento=seguimiento).first()
        if last_habit:
            return 8 if last_habit.tabaquismo else 0
        else:
            last_habit = self.habits.order_by('seguimiento').last()
            return 8 if last_habit.tabaquismo else 0
        return 0

    def has_diabetes(self, seguimiento):
        last_habit = self.habits.filter(seguimiento=seguimiento).first()
        if last_habit:
            return last_habit.diabetes
        else:
            last_habit = self.habits.order_by('seguimiento').last()
            return last_habit.diabetes
        return 0

    def diabetes_points(self, seguimiento):
        last_habit = self.habits.filter(seguimiento=seguimiento).first()
        if last_habit:
            return 6 if last_habit.diabetes else 0
        else:
            last_habit = self.habits.order_by('seguimiento').last()
            return 6 if last_habit.diabetes else 0
        return 0

    def iam_points(self, seguimiento):
        last_habit = self.habits.filter(seguimiento=seguimiento).first()
        if last_habit:
            return 8 if last_habit.iam else 0
        else:
            last_habit = self.habits.order_by('seguimiento').last()
            return 8 if last_habit.iam else 0
        return 0

    def test_question_val(self, key, answers):
        for answer in answers:
            if answer.pregunta.slug == key:
                return answer.valor
        return False

    def ldl_points(self, seguimiento):
        lipid_test = self.examenes.get(tipo__nombre="Examen Lipídico", seguimiento=seguimiento)
        if lipid_test:
            value = self.test_question_val('ldl', lipid_test.respuestas.all())
        else:
            lipid_test = self.examenes.filter(tipo__nombre="Examen Lipídico").order_by('seguimiento').last()
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

    def hdl_points(self, seguimiento):
        lipid_test = self.examenes.get(tipo__nombre="Examen Lipídico", seguimiento=seguimiento)
        if lipid_test:
            value = self.test_question_val('hdl', lipid_test.respuestas.all())
        else:
            lipid_test = self.examenes.filter(tipo__nombre="Examen Lipídico").order_by('seguimiento').last()
            value = self.test_question_val('hdl', lipid_test.respuestas.all())
        if value < 35:
            return 11
        elif value > 34 and value < 45:
            return 8
        elif value > 44 and value < 55:
            return 5
        else:
            return 0

    def trigliceridos_points(self, seguimiento):
        lipid_test = self.examenes.get(tipo__nombre="Examen Lipídico", seguimiento=seguimiento)
        if lipid_test:
            value = self.test_question_val('trigliceridos', lipid_test.respuestas.all())
        else:
            lipid_test = self.examenes.filter(tipo__nombre="Examen Lipídico").order_by('seguimiento').last()
            value = self.test_question_val('trigliceridos', lipid_test.respuestas.all())
        if value < 100:
            return 0
        elif value > 99 and value < 150:
            return 2
        elif value > 149 and value < 200:
            return 3
        else:
            return 4

    def pas_points(self, seguimiento):
        lipid_test = self.examenes.get(tipo__nombre="Examen Lipídico", seguimiento=seguimiento)
        if lipid_test:
            value = self.test_question_val('pas', lipid_test.respuestas.all())
        else:
            lipid_test = self.examenes.filter(tipo__nombre="Examen Lipídico").order_by('seguimiento').last()
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

    def calculateRCVCount(self, seguimiento):
        points = self.age_points() + self.smoke_points(seguimiento) + self.diabetes_points(seguimiento) + self.iam_points(seguimiento) + self.ldl_points(seguimiento) + self.hdl_points(seguimiento) + self.trigliceridos_points(seguimiento) + self.pas_points(seguimiento)
        return points

    def calculateRCVF(self, seguimiento):
        value = self.calculateRCVCount(seguimiento)
        if value < 20:
            return 1
        if value == 21:
            return 1.1
        if value == 22:
            return 1.2
        if value == 23:
            return 1.3
        if value == 24:
            return 1.4
        if value == 25:
            return 1.6
        if value == 26:
            return 1.7
        if value == 27:
            return 1.8
        if value == 28:
            return 1.9
        if value == 29:
            return 2.3
        if value == 30:
            return 2.4
        if value == 31:
            return 2.8
        if value == 32:
            return 2.9
        if value == 33:
            return 3.3
        if value == 34:
            return 3.5
        if value == 35:
            return 4
        if value == 36:
            return 4.2
        if value == 37:
            return 4.8
        if value == 38:
            return 5.1
        if value == 39:
            return 5.7
        if value == 40:
            return 6.1
        if value == 41:
            return 7.0
        if value == 42:
            return 7.4
        if value == 43:
            return 8.0
        if value == 44:
            return 8.8
        if value == 45:
            return 10.2
        if value == 46:
            return 10.5
        if value == 47:
            return 10.7
        if value == 48:
            return 12.8
        if value == 49:
            return 13.2
        if value == 50:
            return 15.5
        if value == 51:
            return 16.8
        if value == 52:
            return 17.5
        if value == 53:
            return 19.6
        if value == 54:
            return 21.7
        if value == 55:
            return 22.2
        if value == 56:
            return 23.8
        if value == 57:
            return 25.1
        if value == 58:
            return 28.0
        if value == 59:
            return 29.4
        if value >= 60:
            return 30
        return 0

    def getRisk(self, points):
        if points < 10:
            return 'Riesgo Leve'
        elif points >= 10 and points < 20:
            return 'Riesgo Moderado'
        else:
            return 'Riesgo Alto'

    def calculateRCV(self, seguimiento):
        data = {}
        if self.genero == 'F' and not self.has_diabetes(seguimiento):
            rnum = self.calculateRCVF(seguimiento) * 0.25
        else:
            rnum = self.calculateRCVF(seguimiento)
        data['numeric'] = str(self.calculateRCVCount(seguimiento)) + '/91 (' + str(rnum) + ')'
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
