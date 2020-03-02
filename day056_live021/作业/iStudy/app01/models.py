from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32,unique=True,verbose_name='用户名')
    password = models.CharField(max_length=128,verbose_name='密码')
    position = models.CharField(max_length=32,verbose_name='职位')
    # company = models.CharField(
    #     max_length=32,
    #     choices=((1,'北京总公司'),(2,'上海分公司'),(3,'广州分公司')),
    #     verbose_name='公司')
    company = models.CharField(max_length=32,verbose_name='公司')
    phone = models.CharField(max_length=11,verbose_name='手机号')
    last_login_time = models.DateTimeField(null=True,blank=True,verbose_name='上次登录时间')
    register_time = models.DateTimeField(auto_now_add=True,verbose_name='注册时间')