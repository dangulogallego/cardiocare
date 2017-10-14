"""dtesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout, password_change, password_change_done, LoginView
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from profiling.views import *
from medical.views import *

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^admin/', admin.site.urls),
    # url(r'^login$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^signup/$', signUp, name='signup'),
    url(r'^paciente/nuevo$', nuevo_paciente, name='nuevopaciente'),
    url(r'^paciente/(?P<paciente_pk>[0-9]+)/$', detalle_paciente, name='detallepaciente'),
    url(r'^paciente/(?P<paciente_pk>[0-9]+)/editar/$', editar_paciente, name='editarpaciente'),
    url(r'^observaciones/$', observaciones, name='observaciones'),
    url(r'^asa/$', test_asa, name='testsasa'),
    url(r'^asa/paciente/(?P<paciente_pk>[0-9]+)/$', new_test_asa, name='nuevoasaform'),
    url(r'^paciente/habitos-antecedentes/$', habitos_antecedentes, name='habitsantecedents'),
    url(r'^paciente/(?P<paciente_pk>[0-9]+)/habitos-antecedentes/$', nuevo_habitos_antecedentes, name='newhabitsantecedents'),
    url(r'^paciente/examenes/lipidicos/$', test_fatty, name='lipidicos'),
    url(r'^examen/lipidico/paciente/(?P<paciente_pk>[0-9]+)/$', new_test_fatty, name='nuevolipidicoform'),
    url(r'^examen/asa/(?P<test_pk>[0-9]+)/$', get_single_test, name='single_asa'),
    url(r'^examen/lipidico/(?P<test_pk>[0-9]+)/$', get_single_test, name='single_lipidico'),


]
