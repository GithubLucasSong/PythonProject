import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}

url = 'http://xicidaili.com/nn/%d'


proxies={
    'http':'113.76.42.249:28803'
}
for page in range(1, 30):
    new_url = format(url % page)

    page_text = requests.get(new_url, headers=headers,proxies=proxies).text
    print(1,page_text)
    tree = etree.HTML(page_text)
    tr_list = tree.xpath('//*[@id="ip_list"]//tr')[1:]
    for tr in tr_list:
        ip = tr.xpath('./td[2]/text()')[0]
        print(1,ip)
