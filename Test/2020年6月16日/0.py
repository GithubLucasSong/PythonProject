import requests
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
city = input('enter a city name:')
data = {
    'cname': '',
    'pid': '',
    'keyword': city,
    'pageIndex': '1',
    'pageSize': '100',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}

data_dict = requests.post(url=url,data=data,headers=headers).json()

for i in data_dict['Table1']:
    print(i['storeName'],i['addressDetail'])
