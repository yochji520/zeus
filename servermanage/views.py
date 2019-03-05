from django.shortcuts import render, HttpResponse
from servermanage.server import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

#服务注册视图
def RegisterServerView(request):
    if request.method == 'GET':
        return render(request, 'register-server.html')
    elif request.method == 'POST':
        pojoname = request.POST['pojoname']
        dbname = request.POST['dbname']
        host = request.POST['hostaddrss']
        port = request.POST['port']
        #判断服务类型
        if request.POST['server_type'] == 'MySQL':
            server_type = 1
        elif request.POST['server_type'] == 'Redis':
            server_type = 2
        else:
            server_type = 3
        #判断部署类型
        if request.POST['build_type'] == '阿里云服务':
            build_type = 1
        else:
            build_type = 2
        #判断角色类型
        if request.POST['role_type'] == '主键':
            role_type = 1
        elif request.POST['role_type'] == '从库':
            role_type = 2
        else:
            role_type = 3
        #判断环境
        if request.POST['env_type'] == '测试环境':
            env_type = 1
        elif request.POST['env_type'] == '预发布环境':
            env_type = 2
        else:
            env_type = 3

        serverdict = {'pojo_name': pojoname, "dbname": dbname, "host": host, "port": port, "server_type": server_type, "build_type": build_type, "role_type": role_type, "env_type": env_type}
        print(serverdict)
        result = str(Server.RegisterServer(serverdict))
        return HttpResponse(json.dumps({"result": result}))
        #return render(request, 'register-server.html', {'result':result}, content_type='application/json')
    else:
        pass

#服务列表,分页查询
def ServerListView(request):
    if request.method == 'GET':
        serverlist = Server.ServerList()
        paginator = Paginator(serverlist, 10, 2)
        page = request.GET.get('page', 1)
        try:
            reulstlist = paginator.page(page)
        except PageNotAnInteger:
            reulstlist = paginator.page(1)
        except EmptyPage:
            reulstlist = paginator.page(paginator.num_pages)
        return render(request, 'server_list.html', context={"reulstlist": reulstlist})
    elif request.method == 'POST':
         return render(request, 'server_list.html')
    else:
        pass


#删除server
def DelServer(request):
    if request.method == "POST":
        serverid = request.GET['server_id']
        server = Server()
        delserver = server.objects.filter(pojo_name__contains=serverid)
        delserver.delete()
    else:
        pass


#修改server信息
def ModifyServer(request):
    if request.method == 'POST':
        pass
    else:
        pass







