from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse
import re
from app01 import models


class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        # 需要登陆后访问的地址 需要判断登陆状态
        # 默认所有的地址都要登录才能访问
        # 校验登陆状态
        is_login = request.session.get('is_login')
        if is_login:
            # 已经登录 可以访问
            user_obj = models.User.objects.filter(username=request.session.get('username')).first()
            request.user_obj = user_obj
            return
        # 设置一个白名单 不登陆就能访问
        url = request.path_info
        # 白名单
        white_url_list = [
            r'^/register/$',
            r'^/login/$',
            r'^/index/$',
            r'^/article/\d+$',
        ]
        for i in white_url_list:
            if re.match(i, url):
                return

        # 没有登录 需要登录
        return redirect('{}?url={}'.format(reverse('login'), request.path_info))
        # return redirect(reverse('login'))
