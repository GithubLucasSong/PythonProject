import requests
from parsel import Selector
import os


urls = []

#获取一页的URL
def download_one_page_urls(page_number):

    # 拿到网页数据
    response = requests.get('https://www.fabiaoqing.com/biaoqing/lists/page/{}.html'.format(page_number))
    html = response.text
    #解析网页数据
    #把字符串内容转换为对象
    sel = Selector(html)
    #提取对象里面的内容
    divs = sel.css('.tagbqppdiv')

    for div in divs:
        img_url = div.css('img.ui::attr(data-original)').extract_first() #'https://blog.csdn.net/cats_miao/article/details/79580736'
        title = div.css('img.ui::attr(title)').extract_first()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~\n':
            title =title.replace(ch,' ')
        urls.append((img_url,title))


#循环获取1-100页的URL
count0 = 0
pages = 100
for i in range(pages):
    download_one_page_urls(i)
    count0 += 1
    print('\r当前获取url进度：{:.2f}%'.format(count0 * 100 / pages), end='')  # end = ''(不自动换行)



#下载每一个url
os.makedirs('表情包',exist_ok = True)
count = 0
for url in urls:
    #部分网站无法访问 所以此处使用异常处理
    try:
        response = requests.get(url[0])
    except:
        continue

    #因为部分文件名太长无法创建文件 所有此处使用异常处理
    try:
        with open(r'表情包\{}'.format(url[1])+'.gif','wb') as f:
            f.write(response.content)
            f.close()
        count += 1
        print('\r当前下载进度：{:.2f}%'.format(count * 100 / len(urls)), end='')  # end = ''(不自动换行)
    except:
        continue