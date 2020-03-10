from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator  # 正则校验
import re
import hashlib
from app01 import models


class BSForm(forms.ModelForm):
    '''拥有bootstrapd的样式'''
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # 自定义的操作
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class RegFrom(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'position', 'company', 'phone','avatar']
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


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = '__all__'
        exclude = ['detail']

    def __init__(self,*args,**kwargs):
        # 获取到用户传来的其他参数 request 不要继续往下面的__init__方法里传了
        super().__init__(*args,**kwargs)
        # 自定义的操作
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['author'].choices = [(self.instance.author_id,self.instance.author.username)]


class ArticleDetailForm(forms.ModelForm):
    class Meta:
        model = models.ArticleDetail
        fields = '__all__'


class CategoryForm(BSForm):
    class Meta:
        model = models.Category
        fields = '__all__'