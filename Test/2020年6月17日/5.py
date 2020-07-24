# url = 'https://m.vmall.com/help/hnrstoreaddr.htm'
import requests
for i in range(1,100):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }
    data = {"portal": 2, "lang": "zh-CN", "country": "CN", "brand": 1, "province": "北京市", "city": "北京市", "pageNo": i,
            "pageSize": 20}

    main_url = 'https://openapi.vmall.com/mcp/offlineshop/getShopList'
    main_json_data = requests.post(main_url, headers=headers, json=data).json()
    for dic in main_json_data['shopInfos']:
        id_ = dic['id']
        url = 'https://openapi.vmall.com/mcp/offlineshop/getShopById'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
        params = {
            'portal': '2',
            'version': '10',
            'country': 'CN',
            'shopId': id_,
            'lang': 'zh-CN',
        }
        json_data = requests.get(url=url, headers=headers, params=params).json()
        name = json_data['shopInfo']['name']
        address = json_data['shopInfo']['address']
        serviceTime = json_data['shopInfo']['serviceTime']
        print('店名：',name, '地址：',address, '营业时间：',serviceTime)
