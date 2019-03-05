#!/usr/bin/python3
#-*- coding: UTF-8 -*- 
#@Author:

from django.urls import path,re_path
from servermanage.views import RegisterServerView, ServerListView


urlpatterns = [
    path(r'servermanage/', RegisterServerView,),
    path(r'serverlist/', ServerListView,),
]