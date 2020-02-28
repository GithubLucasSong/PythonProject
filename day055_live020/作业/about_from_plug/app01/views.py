from django.shortcuts import render,HttpResponse
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator #正则校验
# Create your views here.
import re

# def cheack_user(value):
#     # 不符合校验规则
#     if 'alex' in value:
#         raise ValidationError('alex的名字不符合社会主义价值观')
#     # 符合校验规则不做任何操作

class RegForm(forms.Form):
    user = forms.CharField(
        label='用户名',
        min_length=8,
        # validators=[cheack_user]
        error_messages={
            'required':'用户名不能为空',
            'min_length':'用户名最少8位'
        }
    )
    pwd = forms.CharField(label='密码',min_length=8)
    re_pwd = forms.CharField(label='确认密码',min_length=8)
    phone = forms.CharField(
        label='手机号',
        min_length=8,
        # validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号不符合规范')]
    )
    name = forms.CharField(label='中文姓名')
    id = forms.CharField(label='身份证号', min_length=8)

    def clean_user(self):
        #不符合校验规则 抛出异常
        print(self.cleaned_data)
        value = self.cleaned_data.get('user')
        if 'alex' in value:
            raise ValidationError('用户名中不能包含alex')
        #符合校验规则 返回该字段的值
        return value

    def clean_pwd(self):
        # 不符合校验规则 抛出异常
        print(self.cleaned_data)
        value = self.cleaned_data.get('pwd')
        if not re.search(r'^[A-Za-z]+', value):
            raise ValidationError('密码必须以字母开头')
        # 符合校验规则 返回该字段的值
        return value


    def clean_phone(self):
        #不符合校验规则 抛出异常
        print(self.cleaned_data)
        value = self.cleaned_data.get('phone')
        if not re.search(r'^1[3-9]\d{9}$',value):
            raise ValidationError('你输入的不是手机号')
        return value

    def clean_name(self):
        #不符合校验规则 抛出异常
        print(self.cleaned_data)
        value = self.cleaned_data.get('name')
        if not re.search(r'^[\u4e00-\u9fa5]{2,3}$',value):
            raise ValidationError('你输入的不是中文姓名，格式要求为两个或三个汉字')
        return value

    def clean_id(self):
        # 不符合校验规则 抛出异常
        print(self.cleaned_data)
        value = self.cleaned_data.get('id')
        if not re.search(r'^[1-9]\d{5}(?:18|19|20)\d{2}(?:(?:0[1-9])|(?:1[0-2]))(?:(?:[0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$', value):
            raise ValidationError('你输入的不是身份证号')
        return value

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')
        if re_pwd != pwd:
            #将错误信息加入到某个字段中
            self.add_error('re_pwd','两次密码不一致')
            raise ValidationError('两次密码输入不一致')
        return self.cleaned_data











def reg(request):
    form_obj = RegForm() # 空的form
    if request.method == 'POST':
        # 对提交的数据做校验
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse('注册成功')
        print(form_obj.cleaned_data)  # 经过校验没有问题的数据
    return render(request,'reg.html',{'form_obj':form_obj})

def regcss(request):
    form_obj = RegForm() # 空的form
    if request.method == 'POST':
        # 对提交的数据做校验
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse('注册成功')
        print(form_obj.cleaned_data)  # 经过校验没有问题的数据
    return render(request,'regcss.html',{'form_obj':form_obj})