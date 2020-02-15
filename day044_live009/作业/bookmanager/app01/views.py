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

def book_list(request):
    # 逻辑
    # 获取所有的书籍的信息
    all_books = models.Book.objects.all()  # 对象列表
    # for i in all_publishers:
    #     print(i)
    #     print(i.id)
    #     print(i.name)
    # 返回一个页面，页面中包含出版社的信息
    return render(request, 'book_list.html', {'all_books': all_books})

# 新增书籍
def book_add(request):
    if request.method == 'POST':
        # post请求
        # 获取用户提交的数据
        book_name = request.POST.get('book_name')
        pub_pk = request.POST.get('pub_all')
        pub_all = models.Publisher.objects.all()
        if models.Book.objects.filter(name=book_name):
            # 数据库中有重复的名字
            return render(request,'book_add.html',{'error':'书籍名字已存在','pub_all':pub_all})
        #将数据新增加到数据库中
        models.Book.objects.create(name=book_name,publisher_id=pub_pk)
        # 返回一个重定向到展示书籍的页面
        return redirect('/book_list/')
        #get请求返回一个页面，页面中包含form表单

    # GET
    # 从数据库中查询所有的出版社
    pub_all = models.Publisher.objects.all()
    return render(request,'book_add.html',{'pub_all':pub_all})

#删除书籍
def book_del(request):
    #获取要删除数据的id
    pk = request.GET.get('pk')
    #根据ID到数据库进行删除
    models.Book.objects.filter(pk=pk).delete()
    #返回重定向
    return redirect('/book_list/')


# 修改书籍信息
def book_edit(request):
    pk = request.GET.get('pk')
    book_obj = models.Book.objects.get(pk=pk)
    pub_all = models.Publisher.objects.all()
    if request.method == 'GET':
        # get 返回一个页面 页面包含form表单 input有原始的数据
        return render(request, 'book_edit.html', {'book_obj': book_obj,'pub_all': pub_all})

    else:
        # post 修改数据库中对应的数据
        # 修改书籍名字
        book_obj.name = request.POST.get('book_name')
        # 重新选择出版社
        book_obj.publisher = models.Publisher.objects.get(pk=request.POST.get('pub_all'))
        # 提交保存
        book_obj.save()
        # 返回重定向到展示书籍的页面
        return redirect('/book_list/')

