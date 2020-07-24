# -*- coding: utf-8 -*-
import scrapy
from firstblood.items import FirstbloodItem


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称
    name = 'first'
    # 允许的域名
    # allowed_domains = ['www.baidu.com']

    # 起始的url列表：
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # 数据解析:解析出段子的作者和内容
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')

        for div in div_list:
            # scrapy实现数据解析，取文本或者取属性返回的不再是字符串，而是一个selector对象
            # 我们想要的数据都存在了selector对象的data参数中
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a/div/span//text()').extract()
            content = ''.join(content)
            # print(author, content)

            # Item对象的实例化
            item = FirstbloodItem()
            item['author'] = author
            item['content']=content

            yield item # 将item提交给管道



