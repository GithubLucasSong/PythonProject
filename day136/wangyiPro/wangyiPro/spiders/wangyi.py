# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://news.163.com/']
    bro = webdriver.Chrome('D:\Python s28\PythonProject\day136\wangyiPro\chromedriver.exe')  # 实例化浏览器对象
    five_model_urls = []

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        # 解析出5个板块对应的url
        model_index = [3, 4, 6, 7, 8]
        for index in model_index:
            li = li_list[index]
            model_url = li.xpath('./a/@href').extract_first()
            self.five_model_urls.append(model_url)
            yield scrapy.Request(url=model_url, callback=self.parse_model)

    # 解析板块页面中的新闻标题新闻标题的urlu解析的这两个数据都是动态加载出来
    def parse_model(self, response):  # 用来解析每一个板块对应的页面内容

        div_list = response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            item = WangyiproItem()
            new_title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            item['title'] = new_title
            if new_detail_url:
                yield scrapy.Request(url=new_detail_url, callback=self.parse_new_detail, meta={'item': item})

    def parse_new_detail(self, response):
        item = response.meta['item']
        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)
        content = content.replace('\n','').replace('\r','').replace(' ','')
        item['content'] = content
        yield item

    # 重写父类的一个方法
    def closed(self,spider):
        print('closed方法会在整个爬虫结束后调用一次')
        self.bro.quit()
