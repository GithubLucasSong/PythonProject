import asyncio
import requests
import time
import aiohttp

start = time.time()
urls = [
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/tom',
]


async def get_request(url):
    print('请在请求：', url)
    # requests是不支持异步，不可以出现在特殊函数内部
    # page_text = requests.get(url).text
    # 实例化一个请求对象
    async with aiohttp.ClientSession() as s:
        # get,post方法的使用和requests几乎一直
        # response = s.get(url)
        async with await s.get(url) as response:
            # text()字符串形式的响应数据
            # read()bytes类型的响应数据
            page_text = await response.text()
    return page_text




tasks = []
for url in urls:
    c = get_request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print('总耗时：', time.time() - start)
