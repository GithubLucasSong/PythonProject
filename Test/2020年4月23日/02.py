




import requests
response = requests.get('https://www.baidu.com/',timeout=5)


try:
    assert response.status_code == 200
    print('断言成功')
except AssertionError as e:
    print('断言失败')






