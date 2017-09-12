from django.contrib import admin

from .models import *

admin.site.register(Paciente)
admin.site.register(RegimenSalud)
admin.site.register(Facultad)

# class ProfilesAdmin(admin.ModelAdmin):
#   list_display = ('display_name','id_user','id_user_category', 'id_status')
