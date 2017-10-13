# -*- coding: utf-8 -*-
from django import forms
from .models import TipoExamen, Examen, Pregunta, Paciente

class ASATestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        paciente = kwargs.pop("paciente")
        super(ASATestForm, self).__init__(*args, **kwargs)
        asa = TipoExamen.objects.get(nombre="Test Asa")
        if asa:
             for x in asa.preguntas.order_by('categoria__pk'):
                 opts = [(opt.pk, opt.texto) for opt in x.opciones.all()]
                 self.fields[str(x.pk)] = forms.ChoiceField(choices=opts, label=x.texto, widget=forms.Select(attrs={'class':'form-control'}))


class FattyTestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        paciente = kwargs.pop("paciente")
        super(FattyTestForm, self).__init__(*args, **kwargs)
        fatty = TipoExamen.objects.get(nombre="Examen Lipídico")
        if fatty:
             for x in fatty.preguntas.all():
                 self.fields[str(x.pk)] = forms.FloatField(label=x.texto, widget=forms.NumberInput(attrs={'class':'form-control'}))
