# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FirstbloodPipeline:
    # 是用来接受item对象的，并且每次调用只可以接受一个item类型对象
    # 参数item就是接受到的item对象
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        print('我是管道',author+':'+content+'\n')
        return item
