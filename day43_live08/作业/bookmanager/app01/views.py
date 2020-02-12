from django.shortcuts import render,redirect
from app01 import models
# Create your views here.
def publisher_list(request):
    # 逻辑
    # 获取所有的出版社的信息
    all_publishers = models.Publisher.objects.all()  # 对象列表
    # for i in all_publishers:
    #     print(i)
    #     print(i.id)
    #     print(i.name)
    # 返回一个页面，页面中包含出版社的信息
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})

# 新增出版社
def publisher_add(request):
    if request.method == 'POST':
        # post请求
        # 获取用户提交的数据
        pub_name = request.POST.get('pub_name')
        print(pub_name)
        if models.Publisher.objects.filter(name=pub_name):
            # 数据库中有重复的名字
            return render(request,'publisher_add.html',{'error':'出版社名字已存在'})
        #将数据新增加到数据库中
        ret = models.Publisher.objects.create(name=pub_name)
        # 返回一个重定向到展示出版社的页面
        return redirect('/publisher_list/')
        #get请求返回一个页面，页面中包含form表单

    return render(request,'publisher_add.html')

#删除出版社
def publisher_del(request):
    #获取要删除数据的id
    pk = request.GET.get('pk')
    print(pk)
    #根据ID到数据库进行删除
    models.Publisher.objects.filter(pk=pk).delete()
    #返回重定向
    return redirect('/publisher_list/')

def publisher_edit(request):

    pk = request.GET.get('pk')
    pub_obj = models.Publisher.objects.get(pk=pk)
    if request.method == 'GET':
        # get 返回一个页面 页面包含form表单 input有原始的数据
        return render(request,'publisher_edit.html',{'pub_obj':pub_obj})

    else:
        # post 修改数据库中对应的数据
        pub_obj.name = request.POST.get('pub_name')
        # 提交保存
        pub_obj.save()
        # 返回重定向到展示出版社的页面
        return redirect('/publisher_list/')



