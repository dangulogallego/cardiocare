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
from django.contrib.auth.views import login, logout, password_change, password_change_done
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from profiling.views import *
from medical.views import observaciones, test_asa, new_test_asa

urlpatterns = [
    url(r'^$', home, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^signup/$', signUp, name='signup'),
    url(r'^paciente/nuevo$', nuevo_paciente, name='nuevopaciente'),
    url(r'^paciente/(?P<paciente_pk>[0-9]+)/$', detalle_paciente, name='editarpaciente'),
    url(r'^observaciones/$', observaciones, name='observaciones'),
    url(r'^asa/$', test_asa, name='asaform'),
    url(r'^asa/nuevo/$', new_test_asa, name='nuevoasaform'),

]
