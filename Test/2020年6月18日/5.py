import asyncio
import time


def callback(task):
    print('i am callback',task)
    print(task.result())

# 协程的基本使用
# 特殊的函数
# 协程
# 任务
# 事件循环

async def get_request1(url):
    print('正在下载：', url)
    time.sleep(2)
    print('下载完成：', url)
    return url

#
# async def get_request2(url):
#     print('正在下载：', url)
#     time.sleep(2)
#     print('下载完成：', url)


c1 = get_request1('www.baidu.com')
# c2 = get_request2('www.baidu.com')

print(c1)  # 协程对象

# 对协程c进行进一步封装,返回一个任务对象
task1 = asyncio.ensure_future(c1)  # 获得了一个任务对象
# 给任务对象绑定回调函数
task1.add_done_callback(callback)
# task2 = asyncio.ensure_future(c2)  # 获得了一个任务对象


# 创建事件循环对象
loop = asyncio.get_event_loop() # 创建了一个事件循环对象
# 将任务对象注册装载到事件循环对象中
loop.run_until_complete(task1)



