# -*- coding: utf-8 -*-
import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['www.baidu.com']
    start_urls = [
        'https://www.baidu.com/',
        'https://www.sogou.com/',
        'https123://www.baiddu.com/',
    ]

    def parse(self, response):
        pass
