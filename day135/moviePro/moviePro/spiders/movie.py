# -*- coding: utf-8 -*-
import scrapy
from moviePro.items import MovieproItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.4567kan.com/frim/index1.html']
    url_model = 'https://www.4567kan.com/frim/index%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            item = MovieproItem()  # item对象可以当作是个字典

            title = li.xpath('./div/a/@title').extract_first()
            item['title'] = title
            detail_url = 'https://www.4567kan.com' + li.xpath('./div/a/@href').extract_first()

            # 对详情页的url发起请求
            # meta是一个字典，可以在请求的过程中将meta传递给callback
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})
        if self.page_num < 6:
            new_url = format(self.url_model % self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)

    # 解析详情页的数据
    def parse_detail(self, response):
        item = response.meta['item']
        item['desc'] = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        yield item
