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
from profiling.views import signUp


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^signup/$', signUp, name='signup'),
]
