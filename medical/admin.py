# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(TipoExamen)
admin.site.register(OpcionPregunta)
admin.site.register(CategoriaPregunta)
admin.site.register(Pregunta)
admin.site.register(Examen)
admin.site.register(PuntajeCategoria)
admin.site.register(Observaciones)
