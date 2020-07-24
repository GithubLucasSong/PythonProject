# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class MovieproDownloaderMiddleware:



    #拦截请求
    # 参数request就是拦截到的请求
    def process_request(self, request, spider):
        print('拦截到的请求是：',request.url)
        return None

    #拦截响应
    #request:拦截到的响应对象对应的请求对象
    #response:拦截到的响应对象
    def process_response(self, request, response, spider):
        print('拦截到的响应对象为：', response)
        return response

    # 拦截发生异常的请求对象
    # 参数request就是拦截到异常的请求对象
    def process_exception(self, request, exception, spider):
        print('拦截到异常的请求对象为：',request.url)
