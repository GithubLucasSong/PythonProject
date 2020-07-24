# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from zlsPro.items import ZlsproItem

class ZlsSpider(CrawlSpider):
    name = 'zls'
    conn = Redis(host='127.0.0.1',port=6379,password='foobared')
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.4567kan.com/index.php/vod/show/id/5/lang/%E5%9B%BD%E8%AF%AD/page/1.html']

    rules = (
        Rule(LinkExtractor(allow=r'page/\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            item = ZlsproItem()
            title = li.xpath('./div/a/@title').extract_first()
            item['title'] = title
            #detail_url标识一部电影
            detail_url = 'https://www.4567kan.com/' + li.xpath('./div/a/@href').extract_first()
            ex = self.conn.sadd('movie_url',detail_url)
            if ex ==1: # 插入的电影的url在movie_url在这个redis的集合中不存在
                yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
            else:
                print('当前无最新更新的数据')
    def parse_detail(self,response):
        item = response.meta['item']
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        item['desc'] = desc
        yield item
