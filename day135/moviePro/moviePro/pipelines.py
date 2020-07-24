# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

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
        title = item['title']
        desc = item['desc']
        self.cursor = self.conn.cursor()
        sql = "insert into movie values('%s','%s')" % (title, desc)
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
