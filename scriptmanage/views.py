from django.shortcuts import render

# Create your views here.


def ScriptManageView(request):
    if request.method == 'GET':
        return render(request, 'register-server.html')

def ScriptListView(request):
    if request.method == 'GET':
        return render(request, 'script_list.html')
