from selenium import webdriver
from lxml import etree
from time import sleep



bro = webdriver.Chrome(executable_path='chromedriver')
# bro = webdriver.Edge(executable_path='./msedgedriver')
bro.get('http://125.35.6.84:81/xk/')
sleep(1)
# 获取页面源码内容
page_text = bro.page_source

all_page_text = [page_text]

for i in range(5):
    next_page_btn = bro.find_element_by_xpath('//*[@id="pageIto_next"]')
    next_page_btn.click()
    sleep(1)
    all_page_text.append(bro.page_source)

for page_text in all_page_text:
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="gzlist"]/li')
    for li in li_list:
        title = li.xpath('./dl/@title')[0]
        print(title)

bro.quit()
