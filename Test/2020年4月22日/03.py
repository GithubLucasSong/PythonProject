import requests



# 在请求中使用params参数
# params = {
#     'user':'lucas',
#     'pwd':'666'
# }
# response = requests.get(url='http://httpbin.org/get',params=params)
# print(response.json())

# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
# }
# response = requests.get('https://zhuanlan.zhihu.com/p/107936166',headers=headers)
# print(response.status_code)
# print(response.text)


#1.登录

# response = requests.post(url='http://neeo.cc:6002/pinter/bank/api/login?userName=admin&password=1234')
# print(response.json())
# print(response.cookies)
# print(response.cookies.get_dict())

cookies = {
    'testfan-id':'ed66f10d-ede8-40ab-bead-0c8e877cab5c'
}

response = requests.get(url='http://neeo.cc:6002//pinter/bank/api/query?userName=admin',cookies=cookies)
print(response.status_code)
print(response.json())