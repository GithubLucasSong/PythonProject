import requests

url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'

for page in range(400):
    data = {'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }

    json_data = requests.post(url=url,data=data,headers=headers).json()

    for i in json_data['list']:
        pageurl = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
        pagedata = {'id':i['ID']}
        page_json_data = requests.post(url=pageurl, data=pagedata, headers=headers).json()
        print(page_json_data['businessPerson'],)