# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:33:03 2016

@author: dcompgriff
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    #Configure the projectlist url that returns a list of projects.
    url(r'^(?P<program>[a-z|_]+)/(?P<year>[0-9]+)/$', views.projectlist, name='projectlist')
]
