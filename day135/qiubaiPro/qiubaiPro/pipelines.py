# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from redis import Redis
import json


class QiubaiproPipeline:
    fp = None

    def open_spider(self, spider):
        print('i an open_spider,我只会在爬虫开始的时候被执行一次')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    # 会被调用多次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' + content)
        return item

    def close_spider(self, spider):
        print('i am close_spider,我只会在爬虫结束的时候被执行一次')
        self.fp.close()


# 将数据存储到mysql数据库
class MysqlPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            database='spider',
            charset='utf8',
        )
        print(self.conn)

    # 会被调用多次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.cursor = self.conn.cursor()
        sql = "insert into qiushibaike values('%s','%s')" % (author, content)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


# 将数据存储到redis数据库
class RedisPipeline:
    conn = None

    def open_spider(self, spider):
        self.conn = Redis(
            host='localhost',
            port=6379,
            password='foobared',
        )
        print(self.conn)

    # 会被调用多次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.conn.lpush('qiubaiData', item['content'])
        return item

    def close_spider(self, spider):
        self.conn.close()
