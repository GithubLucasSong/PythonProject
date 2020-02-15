# 1，尝试不使用进程池，可否循环创建多个进程并调用
from multiprocessing import Process
import time

list = []
def func(arg):
    print(f'{arg}开始执行')
    time.sleep(1)
    print(f'{arg}执行完毕')

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=func,args=(f'进程{i}',))
        p.start()
        list.append(p)
    for i in list:
        i.join()
    print('主进程执行完毕')