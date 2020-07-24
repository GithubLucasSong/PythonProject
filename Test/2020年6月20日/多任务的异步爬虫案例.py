import aiohttp
import asyncio
import time
from lxml import etree

start = time.time()
urls = [
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/tom',
]


def parse(task):
    page_text = task.result()
    tree = etree.HTML(page_text)
    data = tree.xpath('//a[@id="feng"]/text()')
    print('解析到的数据为：',data)

async def get_request(url):
    async with aiohttp.ClientSession() as s:
        async with await s.get(url) as response:
            page_text = await response.text()
    return page_text

tasks =[]
for url in urls:
    c = get_request(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(parse)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print('总耗时：',time.time()-start)
