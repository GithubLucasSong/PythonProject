from django.shortcuts import render,HttpResponse
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator #正则校验
# Create your views here.

def cheack_user(value):
    # 不符合校验规则
    if 'alex' in value:
        raise ValidationError('alex的名字不符合社会主义价值观')
    # 符合校验规则不做任何操作

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
    phone = forms.CharField(label='手机号',min_length=8,validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号不符合规范')])
    name = forms.CharField(label='姓名')
    id = forms.CharField(label='身份证号', min_length=18)

    # def clean_user(self):
    #     #不符合校验规则 抛出异常
    #     if 'alex' in value:
    #         raise ValidationError('alex的名字不符合社会主义价值观')
    #     #符合校验规则 返回该字段的值




def reg(request):
    form_obj = RegForm() # 空的form
    if request.method == 'POST':
        # 对提交的数据做校验
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse('注册成功')
        print(form_obj.cleaned_data)  # 经过校验没有问题的数据
    return render(request,'reg.html',{'form_obj':form_obj})