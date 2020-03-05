from django.shortcuts import render, HttpResponse, redirect, reverse
from app01 import models
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator  # 正则校验
import re
import hashlib


# Create your views here.

class RegFrom(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'position', 'company', 'phone']
        # widgets = {'password':forms.PasswordInput}

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入用户名'
            }
        ),
        min_length=6,
        error_messages={
            'required': '用户名不能为空,请重新输入',
            'min_length': '用户名最少6位,请重新输入',
            'unique': '用户名已存在,请重新输入'
        }
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入密码',
            }
        ),
        min_length=6,
        error_messages={
            'required': '密码不能为空,请重新输入',
            'min_length': '密码最少6位,请重新输入'
        }
    )
    re_password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '请再次输入密码'
            }
        ),
        min_length=6,
        error_messages={
            'required': '确认密码不能为空,请重新输入',
            'min_length': '确认密码最少6位,请重新输入'
        }
    )

    position = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入您的职位'
            }
        ),
        error_messages={
            'required': '职位不能为空,请重新输入',
        }
    )

    # company = forms.CharField(
    #
    #     error_messages={
    #         'required': '公司名不能为空,请重新输入',
    #     }
    # )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入您的手机号'
            }
        ),
        min_length=6,
        error_messages={
            'required': '手机号不能为空,请重新输入',
            'min_length': '手机号为11位,请重新输入'
        }
    )

    def clean_password(self):
        # 不符合校验规则 抛出异常
        print(self.cleaned_data)
        value = self.cleaned_data.get('password')
        if not re.search(r'^[A-Za-z]+', value):
            raise ValidationError('密码必须以字母开头,请重新输入')
        # 符合校验规则 返回该字段的值
        return value

    def clean_phone(self):
        # 不符合校验规则 抛出异常
        print(self.cleaned_data)
        value = self.cleaned_data.get('phone')
        if not re.search(r'^1[3-9]\d{9}$', value):
            raise ValidationError('你输入的不是手机号,请重新输入')
        return value

    def clean_company(self):
        # 不符合校验规则 抛出异常
        print(self.cleaned_data)
        value = self.cleaned_data.get('company')
        if not value:
            # 自定义的操作
            field = self.fields['company']
            choices = field.choices
            choices[0] = ('', '公司是必选项,请重新选择')
            field.choices = choices
            raise ValidationError('公司是必选项,请重新选择')
        return value

    def clean(self):
        self._validate_unique = True
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if re_password != password:
            # 将错误信息加入到某个字段中
            self.add_error('re_password', '两次密码不一致,请重新输入')
            raise ValidationError('两次密码输入不一致')
        if password:
            self.cleaned_data['password'] = hashlib.md5(password.encode()).hexdigest()
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义的操作
        field = self.fields['company']
        choices = field.choices
        choices[0] = ('', '请选择公司')
        field.choices = choices


def register(request):
    form_obj = RegFrom()
    if request.method == 'POST':
        form_obj = RegFrom(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('login'))
        print(form_obj.cleaned_data)
    return render(request, 'register.html', {'form_obj': form_obj})


def login_required(func):
    def inner(request, *args, **kwargs):
        user = request.session.get('username')
        if user:
            ret = func(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))
        return ret

    return inner


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
            return redirect(reverse('index'))
        error = '登录失败，请检查用户名和密码'
        return render(request, 'login.html', locals())
    return render(request, 'login.html')


def index(request):
    # 查询所有的文章
    article_all = models.Article.objects.all()
    # is_login = request.session.get('is_login')
    # username = request.session.get('username')
    return render(request, 'index.html', locals())


@login_required
def article(request, pk):
    username = request.session.get('username')
    user_id = models.User.objects.get(username=username).pk
    if request.method == 'POST':
        comment = request.POST.get('comment')
        models.Comment.objects.create(author_id=user_id, content=comment, article_id=pk)
    article_obj = models.Article.objects.get(pk=pk)
    comment_all = models.Comment.objects.filter(article_id=pk)
    return render(request, 'article.html', locals())


@login_required
def personal(request, pk):
    if request.session.get('username'):
        username = request.session.get('username')
        user_id = models.User.objects.get(username=username).pk
        if int(pk) == models.User.objects.get(username=username).pk:
            user_article_all = models.Article.objects.filter(author_id=pk)
            return render(request, 'personal.html', locals())
    return redirect(reverse('login'))


@login_required
def personal_article(request, pk):
    if request.session.get('user'):
        user = request.session.get('user')
        user_id = models.User.objects.get(username=user).pk
        if int(pk) == models.User.objects.get(username=user).pk:
            user_article_all = models.Article.objects.filter(author_id=pk)
            return render(request, 'personal_article.html', locals())
    return redirect(reverse('login'))


@login_required
def personal_comment(request, pk):
    if request.session.get('user'):
        user = request.session.get('user')
        user_id = models.User.objects.get(username=user).pk
        if int(pk) == models.User.objects.get(username=user).pk:
            user_comment_all = models.Comment.objects.filter(author_id=pk)
            return render(request, 'personal_comment.html', locals())
    return redirect(reverse('login'))


@login_required
def article_edit(request, pk):
    user = request.session.get('user')
    user_id = models.User.objects.get(username=user).pk
    if request.method == 'POST':
        article_detail = request.POST.get('article_detail')
        article_obj = models.Article.objects.get(pk=pk)
        article_obj.detail.content = article_detail
        article_obj.detail.save()
        return redirect(reverse('index'))

    else:
        if models.Article.objects.get(pk=pk).author_id == models.User.objects.get(username=user).pk:
            article_obj = models.Article.objects.get(pk=pk)
            return render(request, 'article_edit.html', locals())
        return redirect(reverse('index'))


def dashboard(request):
    return render(request, 'dashboard.html')
