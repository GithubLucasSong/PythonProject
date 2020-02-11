from django.shortcuts import render, HttpResponse, redirect
from app01 import models

# Create your views here.
def login(request):
    print(request.GET)

    if request.method == 'POST':
        # 处理POST请求的逻辑
        user = request.POST.get('une')
        pwd = request.POST.get('pwd')
        # 进行校验
        # if user == 'alex' and pwd == '123':
        if models.User.objects.filter(username=user,password=pwd):
            # 校验成功 告知登录成功
            # return HttpResponse('登录成功')
            # return redirect('http://www.baidu.com')
            # return render(request, 'index.html')
            return redirect('/index/')
    return render(request, 'login.html')


def index(request):
    # orm的测试
    ret = models.User.objects.all()  #  获取表中所有的数据  QuerySet  对象列表
    for i in ret:
        print(i, i.username, i.password,type(i.username))

    # ret = models.User.objects.get(username='alex',password='1234') # 获取一条数据
    # ret = models.User.objects.get(password='123') # 获取一条数据  获取不到或者获取到多条数据 就报错了

    ret = models.User.objects.filter(password='1234') # 获取满足条件的对象


    print(ret, type(ret))

    return render(request, 'index.html')