# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from time import sleep

from scrapy.http import HtmlResponse # scrapy封装好的响应对象

class WangyiproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    # 拦截到所有的响应对象
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        # 共当前代码一共产生了几个响应对象一共有6个响应对象其中有指定的5个为不满足需求的
        # 通过process respanse将5个不满足需求的响应对象找出
        # 可以通过url来定位到这5个响应对象
        # 参数spider：表示爬虫类实例化对象
        if request.url in spider.five_model_urls:
            # request.url 就是每一个响应对象对应的url
            # 将响应数据篡改成满足需求的响应数据
            # 如何获取满足需求的响应数据：通过selenium
            bro = spider.bro  # 爬虫类中实例化好的浏览器对象
            bro.get(request.url)
            sleep(2)
            # execute_script让selenium是的页面滚轮下滑，加载出更多的数据
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(2)
            page_text = bro.page_source  # 获取了满足需求的响应数据
            # 将page_text篡改到当前的响应对象中
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            return new_response
        else:
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
