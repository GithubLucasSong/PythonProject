import threading
import requests
from lxml import etree
import os
from urllib import request
from queue import Queue
#案例：
    #需要将多个页码对应页面中的图片进行爬取。
    #两个队列：
        #page_queue：存储每一个页面的页码链接
        #img_queue：存储的是每一张图片的链接
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36"
}
class Producer(threading.Thread):

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url=url, headers=headers)
        text = response.text
        html = etree.HTML(text)
        a_list = html.xpath('//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a')
        for a in a_list:
            img_url = a.xpath('./img/@data-original')[0]
            img_name = a.xpath('./p/text()')[0]+'.jpg'
            print(img_name,img_url)
            self.img_queue.put((img_url, img_name))


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                break
            img_url, img_name = self.img_queue.get()
            request.urlretrieve(img_url, "imgs/" + img_name)
            print(img_name + " 下载完成！")


# 定义一个主方法，该方法向处理方法中传值
def main():
    page_queue = Queue(1000)
    img_queue = Queue(1000)
    #将前5页的页码链接存储到page_queue中
    for x in range(1, 6):
        url = "https://www.doutula.com/photo/list/?page=%d" % x
        print('页码url：',url)
        page_queue.put(url)
    #创建了三个线程生产数据
    for x in range(3):
        t = Producer(page_queue, img_queue)
        t.start()
    #创建三个线程消费数据
    for x in range(3):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()