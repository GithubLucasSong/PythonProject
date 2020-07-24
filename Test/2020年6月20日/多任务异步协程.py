import asyncio
import time

start = time.time()

async def get_request(url):
    print('正在请求：', url)
    # time.sleep(2) # 不支持异步的模块会中断整个异步效果
    # asyncio.sleep(2) # 没被async修饰的阻塞操作会被跳过
    await asyncio.sleep(2)
    print('请求结束', url)


urls = [
    'www.1.com',
    'www.2.com',
    'www.3.com',
]

tasks = []
for url in urls:
    # 返回了三个协程对象
    c = get_request(url)
    # 获取了三个任务对象
    task = asyncio.ensure_future(c)
    tasks.append(task)
# 事件循环对象的创建
loop = asyncio.get_event_loop()
# 将多个任务注册到了事件循环中
loop.run_until_complete(asyncio.wait(tasks))
# wait方法的参数只能是任务列表。作用就是说wait可以将任务列表中的每一个任务对象进行可挂起操作
# 挂起：可以让当前被挂起的任务对象交出cpu的使用权。
'''
实现异步的原理：当任务列表被wait方法修饰且已经被注册到事件循环中后，loop就会先去执行第一个任务对象，
在执行任务对象的过程中，如果遇到了阻塞操作，则当前任务对象会被挂起，然后loop会执行下一个任务对象，
每当在执行任务对象时，只要遇到阻塞操作当前的任务对象都会被挂起，loop去执行下一个任务对象。当一个挂起的任务对象的阻塞操作结束后，
loop会回头执行其阻塞操作后面的操作

# 重要点：在特殊函数内部不可以出现不支持异步的模块代码，否则会中断整个异步效果
# 关键字await，是需要修饰特殊函数内部阻塞操作的操作，loop一定会执行阻塞操作，在阻塞时间内可以执行其他操作
'''
print('总耗时：',time.time()-start)