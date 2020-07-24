import asyncio
import time


start = time.time()

async def get_request(url):
    print('请在请求：', url)
    time.sleep(2)
    print('请求结束：', url)


urls = [
    'www.1.com',
    'www.2.com',
    'www.3.com',
]

tasks = []  # 任务列表

for url in urls:
    # 返回了三个协程对象
    c = get_request(url)
    # 获取了三个任务对象
    task = asyncio.ensure_future(c)
    # 事件循环对象的创建
    tasks.append(task)

loop = asyncio.get_event_loop()
# 将多个任务注册到了事件循环中
loop.run_until_complete(asyncio.wait(tasks))

print('总耗时：',time.time()-start)