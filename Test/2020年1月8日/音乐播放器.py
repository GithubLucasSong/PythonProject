import pymysql
import pygame
import os
import time
username = input('请输入用户名：')
password = input('请输入密码：')
dbname = input('请输入数据库名称：')
conn = pymysql.connect(host = 'localhost',user= username,password=password,db=dbname,charset = 'utf8')
print('连接数据库成功')
cur = conn.cursor()
music_name = input('请输入歌曲名称：')
sql = "select path from music where name='{}'".format(music_name)
cur.execute(sql)
content = cur.fetchall()
print(content)
for (i,) in content:
    content = i
os.startfile(content)

