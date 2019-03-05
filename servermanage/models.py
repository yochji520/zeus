from django.db import models


#服务记录表

class ServerInfo(models.Model):
    server_id = models.IntegerField(primary_key=True,null= False, default=0)
    pojo_name = models.CharField(max_length=50, null=False, default='')
    dbname = models.CharField(max_length=60, null=False, default='')
    host = models.CharField(max_length=100, null=False, default='')
    port = models.IntegerField(null=False, default=0)
    server_type = models.IntegerField(null=False, default=0)
    build_type = models.IntegerField(null=False, default=0)
    role_type = models.IntegerField(null=False, default=0)
    env_type = models.IntegerField(null=False, default=0)
    createtime = models.DateTimeField(null=False, default='2222-12-12 12:12:12')




