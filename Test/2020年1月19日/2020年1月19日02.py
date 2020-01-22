from selenium import webdriver
import time
import re

#找到 输入库 按钮
# 元素 定位


def search_product():
    driver.find_element_by_xpath('//*[@id="q"]').send_keys(search_name)
    driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    time.sleep(15)
    pageTotal = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    pageTotal = int(re.compile('(\d+)').search(pageTotal).group(1))
    return pageTotal


def drop_down():
    # 一次拉一部分，拉的时候有暂停
    for x in range(1,11,2):
        time.sleep(0.5)
        # j代表滑动条的位置
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


dic = {}


def get_product():
    #获取所有的div 遍历所有的div 得到一个div 再去一个div里面寻找我们要的数据
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        name = div.find_element_by_xpath('.//div[@class="pic"]/a/img').get_attribute('alt')
        img = div.find_element_by_xpath('.//div[@class="pic"]/a/img').get_attribute('src')
        numbers = div.find_element_by_xpath('.//div[@class="row row-1 g-clearfix"]/div[@class="deal-cnt"]').text
        price = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').get_attribute('trace-price')
        shopname = div.find_element_by_xpath('.//div[@class="shop"]/a/span[2]').text
        location = div.find_element_by_xpath('.//div[@class="row row-3 g-clearfix"]/div[2]').text
        dic['商品名称'] = name[0:20]
        dic['商品价格'] = price
        dic['商品销量'] = numbers
        dic['店铺名称'] = shopname
        dic['店铺地址'] = location
        # dic['商品图片'] = img
        # print(dic)
        with open('{}.txt'.format(search_name),'a') as f:
            f.write(str(dic) + '\n')
            f.close
# 淘宝的反爬太严重


def next_page():
    pageTotal = search_product()
    drop_down()
    get_product()
    num = 1
    while num != pageTotal:
        driver.get('https://s.taobao.com/search?q={}&s={}'.format(search_name,num*44))
        # 隐士等待 智能等待  最高等待10S时间 如果等待时间10S 抛出异常
        driver.implicitly_wait(10)
        num += 1
        drop_down()
        get_product()
        print('\r当前进度：{:.2f}%'.format(num * 100 / pageTotal), end='')  # end = ''(不自动换行)


if __name__ == '__main__':
    search_name = input('请输入您想要查询的商品：')
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com/')
    next_page()