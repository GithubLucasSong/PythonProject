# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # 将一页数据请求爬取
    # def parse(self, response):
    #     # 数据解析:解析出段子的作者和内容
    #     div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
    #
    #     for div in div_list:
    #         # scrapy实现数据解析，取文本或者取属性返回的不再是字符串，而是一个selector对象
    #         # 我们想要的数据都存在了selector对象的data参数中
    #         author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         content = div.xpath('./a/div/span//text()').extract()
    #         content = ''.join(content)
    #         # 解析出来几个字段，就需要在item类中定义几个属性
    #         item = QiubaiproItem() # item对象可以当作是个字典
    #         item['author'] = author
    #         item['content'] = content
    #         yield item

    # 将多个页码对应的数据进行爬取+解析
    url_model = 'https://www.qiushibaike.com/text/page/%d/'
    page_num = 2

    def parse(self, response):
        # 数据解析:解析出段子的作者和内容
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')

        for div in div_list:
            # scrapy实现数据解析，取文本或者取属性返回的不再是字符串，而是一个selector对象
            # 我们想要的数据都存在了selector对象的data参数中
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a/div/span//text()').extract()
            content = ''.join(content)
            # 解析出来几个字段，就需要在item类中定义几个属性
            item = QiubaiproItem()  # item对象可以当作是个字典
            item['author'] = author
            item['content'] = content
            print(item)
            yield item
        # 手动请求代码
        if self.page_num < 6: # 结束递归的条件
            url = format(self.url_model % self.page_num)
            self.page_num += 1
            yield scrapy.Request(url, callback=self.parse)
