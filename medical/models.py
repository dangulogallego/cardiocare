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
            return 'Muy baja'
        elif self.resultado > 24 and self.resultado <= 48:
            return 'Baja'
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
                    tmp[keyCat]['observaciones'] += recomendation.observacion + ". "
            else:
                tmp[keyCat]['observaciones'] = "Estás haciendo un excelente trabajo."

            data.append(tmp[cat])

        return data

    def calcularByLipidCategorias(self):
        data = []
        tmp = {}
        asa_test = self.paciente.examenes.filter(tipo__nombre="Test Asa", seguimiento=self.seguimiento).first()
        if asa_test:
            answers = asa_test.respuestas.order_by('pregunta__categoria')
        else:
            asa_test = self.paciente.examenes.filter(tipo__nombre="Test Asa").order_by("seguimiento").last()
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
                    tmp[keyCat]['observaciones'] += recomendation.observacion + ". "
            else:
                tmp[keyCat]['observaciones'] = "Estás haciendo un excelente trabajo."

            data.append(tmp[cat])

        return data
