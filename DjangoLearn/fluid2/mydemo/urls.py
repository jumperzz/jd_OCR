"""mydemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.myweb,name='myweb'),

    path('stu',views.stu,name='stu'),
    re_path('^stupage(?P<pIndex>[0-9]+)$',views.stupage,name='stupage'),
    path('stusearch',views.stusearch,name='stusearch'),
    re_path('^stuspages(?P<pIndex>[0-9]+)$',views.stuspages, name='stuspages'),

    path('ct',views.ct,name='ct'),
    path('setCt',views.setCt,name='setCt'),

    #session
    path('session',views.se,name='session'),


    #继承实例
    path('extends',views.extends,name='extends')
]
