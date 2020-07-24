

from multiprocessing.dummy import Pool
import requests
import time
from lxml import etree


# 封装一个函数：数据爬取操作

def get_request(url):
    page_text = requests.get(url).text
    return page_text

def parse(page_text):
    tree = etree.HTML(page_text)
    data= tree.xpath('//div[1]//text()')
    print(data)

if __name__ == '__main__':
    start = time.time()
    urls = [
        'http://127.0.0.1:5000/jay',
        'http://127.0.0.1:5000/bobo',
        'http://127.0.0.1:5000/tom',
    ]
    pool = Pool(3)
    # 让get_request去处理urls列表中的每一个列表元素（基于异步处理）
    page_text_list = pool.map(get_request,urls)
    # 实现异步的数据解析
    pool.map(parse,page_text_list)
    print('总耗时：',time.time()-start)
