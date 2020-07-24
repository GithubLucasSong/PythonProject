#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 环境安装：pip install flask

from flask import Flask,render_template
from time import sleep

#1.实例化一个flask的实例对象
app = Flask(__name__)

@app.route('/jay')
def index_1():
    sleep(2)
    return render_template('test.html')

@app.route('/bobo')
def index_2():
    sleep(2)
    return render_template('test.html')

@app.route('/tom')
def index_3():
    sleep(2)
    return render_template('test.html')


if __name__ == "__main__":
    #开启服务，使用的是调试模式（代码保存后会自动重启服务）
    app.run(debug=True)