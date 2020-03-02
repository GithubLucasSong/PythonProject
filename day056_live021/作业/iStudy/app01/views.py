from django.shortcuts import render,HttpResponse,redirect,reverse
from app01 import models
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator #正则校验
# Create your views here.
import re
import hashlib
# Create your views here.

class RegFrom(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username','password','position','company','phone']
        # widgets = {'password':forms.PasswordInput}

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入用户名'
            }
        ),
        min_length=6,
        error_messages={
            'required': '用户名不能为空',
            'min_length': '用户名最少6位',
            'unique': '用户名已存在'
        }
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入密码'
            }
        ),
        min_length=6,
        error_messages={
            'required': '密码不能为空',
            'min_length': '密码最少6位'
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
            'required': '密码不能为空',
            'min_length': '密码最少6位'
        }
    )

    position = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入您的职位'
            }
        ),
        error_messages={
            'required': '职位不能为空',
        }
    )

    company = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入您的公司名'
            }
        ),
        error_messages={
            'required': '公司名不能为空',
        }
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '请输入您的手机号'
            }
        ),
        min_length=6,
        error_messages={
            'required': '手机号不能为空',
            'min_length': '手机号为11位'
        }
    )


    def clean_password(self):
        # 不符合校验规则 抛出异常
        print(self.cleaned_data)
        value = self.cleaned_data.get('password')
        if not re.search(r'^[A-Za-z]+', value):
            raise ValidationError('密码必须以字母开头')
        # 符合校验规则 返回该字段的值
        return value

    def clean_phone(self):
        # 不符合校验规则 抛出异常
        print(self.cleaned_data)
        value = self.cleaned_data.get('phone')
        if not re.search(r'^1[3-9]\d{9}$', value):
            raise ValidationError('你输入的不是手机号')
        return value

    def clean(self):
        self._validate_unique = True
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if re_password != password:
            # 将错误信息加入到某个字段中
            self.add_error('re_password', '两次密码不一致')
            raise ValidationError('两次密码输入不一致')
        self.cleaned_data['password'] = hashlib.md5(password.encode()).hexdigest()
        return self.cleaned_data

def register(request):
    form_obj = RegFrom()
    if request.method == 'POST':
        form_obj = RegFrom(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('login'))
        print(form_obj.cleaned_data)
    return render(request, 'register.html', {'form_obj': form_obj})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.User.objects.filter(username=username,password=hashlib.md5(password.encode()).hexdigest()).first()
        if user_obj:
            return render(request,'index.html')
        error = '登录失败，请检查用户名和密码'
        return render(request,'login.html',locals())
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

