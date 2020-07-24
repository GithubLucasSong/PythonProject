# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class ImgproPipeline:
#     def process_item(self, item, spider):
#         print(item['img_name'],item['img_src'])
#         return item


from scrapy.pipelines.images import ImagesPipeline
import scrapy


# 自定义管道类
class ImgproPipeline(ImagesPipeline):
    # 可以接收爬虫文件传递过来的item
    # 可以对图片的地址进行请求发送
    def get_media_requests(self, item, info):
        img_name = item['img_name']
        img_src = item['img_src']
        yield scrapy.Request(url=img_src, meta={'item': item})

    # 返回图片的名称  会自动拼接设置里的IMAGES_STORE路径存储
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        img_name = item['img_name']
        return img_name

    def item_completed(self, results, item, info):
        return item  # 可以将item传递给下一个即将被执行的管道类
