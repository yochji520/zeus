from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import AddForm


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

