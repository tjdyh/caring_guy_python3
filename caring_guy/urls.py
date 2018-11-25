"""caring_guy URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from zabbixapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^host/$', views.get_host, name='host'),
    url(r'^template/$', views.get_template, name='template'),
    url(r'^hostgroup/$', views.get_hostgroup, name='hostgroup'),
    url(r'^echarts/', views.echarts, name='echarts'),
    url(r'^$', views.index),
    url(r'^form/$', views.form_post, name='ab'),
]
