from django.shortcuts import render, HttpResponse, redirect
from app01 import models

# Create your views here.
def login(request):
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
    return render(request, 'index.html')