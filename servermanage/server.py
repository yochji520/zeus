#!/usr/bin/python3
#-*- coding: UTF-8 -*- 
#@Author:youchuanjiang
#@LastTime:2019-02-27
import random
from servermanage.models import ServerInfo
from common.logs import *

RESULT = 200
# 服务注册
class Server(object):
    '''
    主要是对所有服务的
    '''
    def __init__(self, server_id=None, pojo_name=None, dbname=None, host=None, port=None,server_type=None, build_type=None, role_type=None, env_type=None, createtime=None):
        self.server_id = server_id
        self.pojo_name = pojo_name
        self.dbname = dbname
        self.host = host
        self.port = port
        self.server_type = server_type
        self.build_type = build_type
        self.role_type = role_type
        self.env_type = env_type
        self.createtime = createtime
        self.serverdict = {pojo_name: pojo_name, dbname: dbname, host: host, port: port, server_type: server_type, build_type: build_type, role_type: role_type, env_type: env_type, createtime: createtime}


    @classmethod
    def RegisterServer(self, serverdict):
    #注册服务
        def serverid(num):
         # 生成server_id,随机生成6位正整数
            serverid = ""
            for i in range(num):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                serverid += ch
            return serverid

        # 处理数据
        server = ServerInfo()
        server.server_id = serverid(6)
        server.pojo_name = serverdict['pojo_name']
        server.dbname = serverdict['dbname']
        server.host = serverdict['host']
        server.port = serverdict['port']
        server.server_type = serverdict['server_type']
        server.build_type = serverdict['build_type']
        server.role_type = serverdict['role_type']
        server.env_type = serverdict['env_type']
        server.createtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log = LogtoLog().getlog()
        try:
            server.save()
            return RESULT
        except Exception as err:
            #待完成日志封装
            log.error("数据库操作异常", err)
            return "服务注册失败"
        except ConnectionError as err:
            log.error("数据库连接异常，请查看数据库服务是否正常运行或者网络是否存在异常", err)
            return "服务注册失败"


    #获取服务列表
    @classmethod
    def ServerList(self):
        try:
            serverlist = ServerInfo.objects.all().order_by('pojo_name').values()
            serverlist_dict = list(serverlist)
            return serverlist_dict
        except ConnectionError as err:
            log = LogtoLog().getlog()
            log.error(err)


    #修改服务信息
    @classmethod
    def ModifyInfo(self, serverdict):
        try:
            server = Server()
            serverid = serverdict['server_id']
            sinfo = server.objects.get(server_id=serverid)
            sinfo.server_id = serverid
            sinfo.dbname = serverdict['dbname']
            sinfo.host = serverdict['host']
            sinfo.pojo_name = serverdict['pojo_name']
            sinfo.port = serverdict['port']
            sinfo.server_type = serverdict['server_type']
            sinfo.build_type = serverdict['build_type']
            sinfo.declare = serverdict['declare']
            sinfo.createtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            sinfo.save()
        except Exception as err:
            log = LogtoLog().getlog()
            log.error("数据库连接异常，请查看数据库服务是否正常运行或者网络是否存在异常", err)
        return "修改成功"

    #删除服务信息
    @classmethod
    def DelSever(self,server_id):
        try:
            pass
        except Exception as err:
            log = LogtoLog().getlog()
            log.error("数据库连接异常", err)
        return "服务已删除"






