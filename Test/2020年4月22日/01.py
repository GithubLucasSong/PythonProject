# import requests
# import time
# response = requests.get('https://www.baidu.com/img/dongdiqiu_e991bad6a2fe51ffcdaf1db6d5cb0e36.gif')
#
# with open('dongdiqiu_e991bad6a2fe51ffcdaf1db6d5cb0e36.gif','wb',) as f:
#     f.write(response.content)


import requests
# response = requests.get('https://www.cnblogs.com/neeo/articlEs/11511087.html')
# response = requests.get('http://www.neeo.cc:6002/pinter/com/getSku?id=1')
# response = requests.get('https://www.autohome.com.cn/beijing/')
# print(response) # 查看响应状态
# print(response.status_code) # 查看响应状态
# print(response.content) # 查看bytes类型的数据，通常是获取图片
# print(response.headers) # 查看响应头
# print(response.json()) # 获取Json类型的数据，要确保相应类型是json 不然报错
# print(response.text) # 文本类型的数据用text
# print(response.url.rsplit('/',1)[-1])
# response.encoding = 'gb2312' # 指定（修改）当前响应结果的编码类型
# print(response.text) # 文本类型的数据用text
# print(response.encoding) # 获取当前响应的编码类型
# print(response.request) # 请求类型
# print(response.request.method) # 请求类型
# print(response.cookies) # 查看cookies
# print(response.is_permanent_redirect) # 是否是重定向的响应
# print(response.iter_lines()) # 循环获取，一行一行的取 请忘掉这个方法
# print(response.iter_content(chunk_size=1024)) # 迭代取值，可以指定chunk_size


response = requests.request(method='get',url='https://www.autohome.com.cn/beijing/')
print(response.status_code)

