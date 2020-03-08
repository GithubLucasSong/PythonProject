from django.shortcuts import render, HttpResponse, redirect, reverse
from app01 import models
from app01.forms import RegFrom,ArticleForm,ArticleDetailForm
import hashlib


# Create your views here.

def register(request):
    form_obj = RegFrom()
    if request.method == 'POST':
        form_obj = RegFrom(request.POST,request.FILES)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('login'))
        print(form_obj.cleaned_data)
    return render(request, 'register.html', {'form_obj': form_obj})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        keep = request.POST.get('keep')
        user_obj = models.User.objects.filter(username=username, password=hashlib.md5(password.encode()).hexdigest(),
                                              is_active=True).first()
        if user_obj:
            ret = redirect(reverse('index'))
            if not keep:
                request.session['is_login'] = True
                request.session['username'] = user_obj.username
                request.session.set_expiry(60)
            elif keep == '1':
                request.session['is_login'] = True
                request.session['username'] = user_obj.username
                request.session.set_expiry(3600)
            return redirect(request.GET.get('url')) if request.GET.get('url') else redirect(reverse('index'))
        error = '登录失败，请检查用户名和密码'
        return render(request, 'login.html', locals())
    return render(request, 'login.html')


def logout(request):
    request.session.delete()
    return redirect(reverse('index'))


def index(request):
    # 查询所有的文章
    article_all = models.Article.objects.all()
    # user_obj = models.User.objects.filter(username=request.session.get('username')).first()
    # is_login = request.session.get('is_login')
    # username = request.session.get('username')
    return render(request, 'index.html', locals())


def article(request, pk):
    if request.method == 'POST':
        if request.session.get('is_login'):
            username = request.session.get('username')
            user_id = models.User.objects.get(username=username).pk
            comment = request.POST.get('comment')
            models.Comment.objects.create(author_id=user_id, content=comment, article_id=pk)
        else:
            return redirect(reverse('login'))
    article_obj = models.Article.objects.get(pk=pk)
    comment_all = models.Comment.objects.filter(article_id=pk)
    return render(request, 'article.html', locals())


#
# def personal(request, pk):
#     if request.session.get('username'):
#         username = request.session.get('username')
#         user_id = models.User.objects.get(username=username).pk
#         if int(pk) == models.User.objects.get(username=username).pk:
#             user_article_all = models.Article.objects.filter(author_id=pk)
#             return render(request, 'personal.html', locals())
#     return redirect(reverse('login'))
#
#
# def personal_article(request, pk):
#     if request.session.get('user'):
#         user = request.session.get('user')
#         user_id = models.User.objects.get(username=user).pk
#         if int(pk) == models.User.objects.get(username=user).pk:
#             user_article_all = models.Article.objects.filter(author_id=pk)
#             return render(request, 'personal_article.html', locals())
#     return redirect(reverse('login'))
#
#
# def personal_comment(request, pk):
#     if request.session.get('user'):
#         user = request.session.get('user')
#         user_id = models.User.objects.get(username=user).pk
#         if int(pk) == models.User.objects.get(username=user).pk:
#             user_comment_all = models.Comment.objects.filter(author_id=pk)
#             return render(request, 'personal_comment.html', locals())
#     return redirect(reverse('login'))
#
#
# def article_edit(request, pk):
#     user = request.session.get('user')
#     user_id = models.User.objects.get(username=user).pk
#     if request.method == 'POST':
#         article_detail = request.POST.get('article_detail')
#         article_obj = models.Article.objects.get(pk=pk)
#         article_obj.detail.content = article_detail
#         article_obj.detail.save()
#         return redirect(reverse('index'))
#
#     else:
#         if models.Article.objects.get(pk=pk).author_id == models.User.objects.get(username=user).pk:
#             article_obj = models.Article.objects.get(pk=pk)
#             return render(request, 'article_edit.html', locals())
#         return redirect(reverse('index'))


def backend(request):
    return render(request, 'dashboard.html')


def article_list(request):
    all_article = models.Article.objects.filter(author=request.user_obj)
    return render(request, 'article_list.html', locals())


def article_add(request):
    article_obj = models.Article(author=request.user_obj)
    form_obj = ArticleForm(instance=article_obj)
    articledetail_form_obj = ArticleDetailForm()
    if request.method == 'POST':
        form_obj = ArticleForm(request.POST,instance=article_obj)
        articledetail_form_obj = ArticleDetailForm(request.POST)
        if form_obj.is_valid() and articledetail_form_obj.is_valid():
            # detail = request.POST.get('detail')
            # detail_obj = models.ArticleDetail.objects.create(content=detail)
            detail_obj = articledetail_form_obj.save()
            form_obj.cleaned_data['detail_id'] = detail_obj.pk
            models.Article.objects.create(**form_obj.cleaned_data)
            return redirect(reverse('article_list'))
    return render(request, 'article_add.html',locals())

def article_edit(request,pk):
    article_obj = models.Article.objects.filter(pk=pk).first()
    form_obj = ArticleForm(instance=article_obj,)
    articledetail_form_obj = ArticleDetailForm(instance=article_obj.detail)
    if request.method == 'POST':
        form_obj = ArticleForm(request.POST,instance=article_obj)
        articledetail_form_obj = ArticleDetailForm(request.POST,instance=article_obj.detail)
        if form_obj.is_valid() and articledetail_form_obj.is_valid():
            # form_obj.instance.detail.content = request.POST.get('detail')
            # form_obj.instance.detail.save()
            articledetail_form_obj.save()
            form_obj.save()
            return redirect(reverse('article_list'))
    return render(request,'article_edit.html',locals())


users = [{'name':f'alex-{i}','password':'123'} for i in range(1,446)]
def user_list(request):
    try:
        page = int(request.GET.get('page',1))
        if page <= 0:
            page = 1
    except Exception:
        page = 1
    print(page,type(page))
    # 每页显示的数据条数
    per_num = 10

    # 总的页码数
    total_num,more = divmod(len(users),per_num,)
    if more:
        total_num +=1
    # 要显示的页码数
    max_show = 11
    half_show = max_show //2

    if total_num <= max_show:
        # 页码的起始值
        page_start = 1
        # 页码的终止值
        page_end = total_num

    else:
        # 处理左边的极值
        if page - half_show <= 0:
            page_start = 1
            page_end = max_show

        elif page + half_show >= total_num:
            page_start = total_num - max_show + 1
            page_end = total_num

        else:
            # 页码的起始值
            page_start = page - half_show
            # 页码的终止值
            page_end = page + half_show


    page_list = []
    page_list.append('<li><a href="?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(page-1))
    for i in range(page_start,page_end + 1):
        if i == page:
            page_list.append('<li class="active"><a href="?page={}">{}</a></li>'.format(i, i))
        else:
            page_list.append('<li><a href="?page={}">{}</a></li>'.format(i,i))
    page_list.append(
        '<li><a href="?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(page + 1))

    page_html = ''.join(page_list)


    start = (page-1)*per_num
    end = page*per_num

    return render(request,'user_list.html',{'users':users[start:end],'total_num':range(page_start,page_end+1),'page_html':page_html})
