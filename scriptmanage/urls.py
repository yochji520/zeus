#!/usr/bin/python3
#-*- coding: UTF-8 -*- 
#@Author:
#@Time:

from django.urls import path
from .views import ScriptListView, ScriptManageView

urlpatterns = [
    path(r'scriptmanage/', ScriptManageView, name='scriptmanage'),
    path(r'scriptlist/', ScriptListView, name='scriptlist'),
]