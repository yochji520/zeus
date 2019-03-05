#!/usr/bin/python3
#-*- coding: UTF-8 -*- 

from django import forms


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()