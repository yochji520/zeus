#!/usr/bin/python3
#-*- coding: UTF-8 -*- 

from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index,),
]

