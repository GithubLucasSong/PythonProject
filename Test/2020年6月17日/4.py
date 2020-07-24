import requests
from lxml import etree
import os
from urllib import request
dirName = 'imgLibs'

if not os.path.exists(dirName):
    os.mkdir(dirName)

dirName = 'imgLibs'
url = "http://pic.netbian.com/4kmeinv/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

url_model = "http://pic.netbian.com/4kmeinv/index_{}.html"
page = 190


# 解析图片名称+图片链接
for i in range(1,page):
    if i !=1:
        url = url_model.format(i)
    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'
    page_text = response.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    for li in li_list:
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_path = dirName + '/' + img_name
        request.urlretrieve(img_src,img_path)
        print(img_name,'下载成功')