# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']
    # 实例化的链接提取器的对象
    # 参数allow='正则'：提取规则
    # 使用LinkExtractor提取所有的页面链接
    link = LinkExtractor(allow=r'id=1&page=\d+')
    # link = LinkExtractor(allow=r'') # 可以取到网站中所有的链接
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            title = li.xpath('./span[3]/a/text()').extract_first()
            print(title)
