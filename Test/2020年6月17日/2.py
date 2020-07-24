from bs4 import BeautifulSoup
import requests

# bs4 = BeautifulSoup(,'lxml')


url = 'http://shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
page = requests.get(url=url, headers=headers)
page.encoding = 'utf-8'
fp = page.text
soup = BeautifulSoup(fp, 'lxml')
# print(soup.find('div',class_='book-mulu').text)
a_list = soup.select('.book-mulu > ul > li > a')


fb = open('./sanguo.txt','w',encoding='utf-8')

for a in a_list:
    title = a.string
    detail_url = 'http://shicimingju.com' + a['href']
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    detail_soup = BeautifulSoup(detail_page_text, 'lxml')
    div_tag = detail_soup.find('div',class_='chapter_content')
    content = div_tag.text
    fb.write(title+':'+content+'\n')
    print(title,'已经下载成功')
