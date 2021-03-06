from django.shortcuts import render, redirect
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
            return render(request, 'publisher_add.html', {'error': '出版社名字已存在'})
        elif not pub_name:
            # 出版社名字为空
            return render(request, 'publisher_add.html', {'error': '出版社名字不能为空'})
        # 将数据新增加到数据库中
        ret = models.Publisher.objects.create(name=pub_name)
        # 返回一个重定向到展示出版社的页面
        return redirect('/publisher_list/')
        # get请求返回一个页面，页面中包含form表单

    return render(request, 'publisher_add.html')


# 删除出版社
def publisher_del(request):
    # 获取要删除数据的id
    pk = request.GET.get('pk')
    print(pk)
    # 根据ID到数据库进行删除
    models.Publisher.objects.filter(pk=pk).delete()
    # 返回重定向
    return redirect('/publisher_list/')


def publisher_edit(request):
    pk = request.GET.get('pk')
    pub_obj = models.Publisher.objects.get(pk=pk)
    if request.method == 'GET':
        # get 返回一个页面 页面包含form表单 input有原始的数据
        return render(request, 'publisher_edit.html', {'pub_obj': pub_obj})

    else:
        # post 修改数据库中对应的数据
        if not request.POST.get('pub_name'):
            # 出版社名字不能为空
            return render(request, 'publisher_edit.html', {'error': '出版社名字不能为空', 'pub_obj': pub_obj})
        else:
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
            return render(request, 'book_add.html', {'error': '书籍名字已存在', 'pub_all': pub_all})
        elif not book_name:
            # 数据为空
            return render(request, 'book_add.html', {'error': '书籍名字不能为空', 'pub_all': pub_all})
        # 将数据新增加到数据库中
        models.Book.objects.create(name=book_name, publisher_id=pub_pk)
        # 返回一个重定向到展示书籍的页面
        return redirect('/book_list/')
        # get请求返回一个页面，页面中包含form表单

    # GET
    # 从数据库中查询所有的出版社
    pub_all = models.Publisher.objects.all()
    return render(request, 'book_add.html', {'pub_all': pub_all})


# 删除书籍
def book_del(request):
    # 获取要删除数据的id
    pk = request.GET.get('pk')
    # 根据ID到数据库进行删除
    models.Book.objects.filter(pk=pk).delete()
    # 返回重定向
    return redirect('/book_list/')


# 修改书籍信息
def book_edit(request):
    pk = request.GET.get('pk')
    book_obj = models.Book.objects.get(pk=pk)
    pub_all = models.Publisher.objects.all()
    if request.method == 'GET':
        # get 返回一个页面 页面包含form表单 input有原始的数据
        return render(request, 'book_edit.html', {'book_obj': book_obj, 'pub_all': pub_all})

    else:
        # post 修改数据库中对应的数据
        # 修改书籍名字
        if not request.POST.get('book_name'):
            return render(request, 'book_edit.html', {'book_obj': book_obj, 'pub_all': pub_all, 'error': '书籍名字不能为空'})

        else:
            book_obj.name = request.POST.get('book_name')
            # 重新选择出版社
            book_obj.publisher = models.Publisher.objects.get(pk=request.POST.get('pub_all'))
            # 提交保存
            book_obj.save()
            # 返回重定向到展示书籍的页面
            return redirect('/book_list/')


def index(request):
    return render(request, 'index.html')


def author_list(request):
    author_all = models.Author.objects.all()
    return render(request, 'author_list.html', {'author_all': author_all})


def author_add(request):
    if request.method == 'POST':
        # post请求
        # 获取用户提交的数据
        author_name = request.POST.get('author_name')
        book_id = request.POST.getlist('book_all')
        book_all = models.Book.objects.all()
        if models.Author.objects.filter(name=author_name):
            # 数据库中有重复的名字
            return render(request, 'author_add.html',
                          {'error': '作者名字已存在', 'author_name': author_name, 'book_all': book_all})
        elif not author_name:
            # 数据为空
            return render(request, 'author_add.html',
                          {'error': '作者名字不能为空', 'author_name': author_name, 'book_all': book_all})

        else:
            # 将数据新增加到数据库中
            author_obj = models.Author.objects.create(name=author_name)
            # author_obj.books = models.Book.objects.filter(pk=book_id)  #错误写法
            author_obj.books.set(book_id)
            # 返回一个重定向到展示作者的页面
            return redirect('/author_list/')

    else:
        # get请求返回一个页面，页面中包含form表单
        book_all = models.Book.objects.all()
        return render(request, 'author_add.html', {'book_all': book_all})


def author_del(request):
    # 获取要删除数据的id
    pk = request.GET.get('pk')
    # 根据ID到数据库进行删除
    models.Author.objects.filter(pk=pk).delete()
    # 返回重定向
    return redirect('/author_list/')


def author_edit(request):
    # 获取页面提交的作者ID
    pk = request.GET.get('pk')
    # 在作者表中通过id获得作者对象
    author_obj = models.Author.objects.get(pk=pk)
    # 获得所有的书籍
    book_all = models.Book.objects.all()
    if request.method == 'POST':
        # 判断输入的作者名是否为空
        if not request.POST.get('author_name'):
            return render(request, 'author_edit.html',
                          {'error': '作者名字不能为空', 'author_obj': author_obj, 'book_all': book_all})
        else:
            # 修改作者名字
            author_obj.name = request.POST.get('author_name')
            # 修改作者作品
            author_obj.books.set(request.POST.getlist('book_all')) # 注意获取列表要用getlist
            # 返回重定向到作者列表
            return redirect('/author_list/')

    else:
        # get请求返回一个页面，页面中包含form表单
        return render(request, 'author_edit.html', {'author_obj': author_obj, 'book_all': book_all})
