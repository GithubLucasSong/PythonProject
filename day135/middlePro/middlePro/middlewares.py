# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class MiddleproDownloaderMiddleware:
    # 拦截请求
    # 参数request就是拦截所有的请求（正常的请求and异常的请求）
    def process_request(self, request, spider):
        print('拦截到的请求是：', request.url)
        request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36'
        return None

    # 拦截响应
    # request:拦截到的响应对象对应的请求对象
    # response:拦截到的响应对象
    def process_response(self, request, response, spider):
        print('拦截到的响应对象为：', response)
        return response

    # 拦截发生异常的请求对象
    # 参数request就是拦截到异常的请求对象
    # 拦截到异常的请求后需要对其进行修正，让其变成一个正常的请求，然后对其重新发送
    def process_exception(self, request, exception, spider):
        print('拦截到异常的请求对象为：', request.url)
        # 建议将代理的设置写道该方法内部
        # return request # 将修正后的请求进行重新发送