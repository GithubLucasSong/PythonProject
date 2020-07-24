# import re
# import json
# sss = '{"testfan-token": "${neeo_001>data>data}$"}'
#
# find = re.findall('\${.*?}\$',sss)
#
# for i in find:
#     find = i
# print(find)
#
# print(re.sub(find,'1',sss))


import requests
# response = requests.request(method='get', url='http://www.neeo.cc:6002/pinter/bank/api/query2',params={"userName": "admin"},headers={"testfan-token": "c818ced87fb94411a5c1db99672ec3d7"})
# print(response.json())


response = requests.request(method='post', url='http://www.neeo.cc:6002/pinter/bank/api/login',data={"userName": "admin", "password": "1234"})


print(response.j)