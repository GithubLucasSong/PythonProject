#1，写一个程序，实现3个进程间通信，传递一个字符串
# from multiprocessing import Queue
# from multiprocessing import Process
#
#
# def func1(q):
#     info = '这是一个字符串'
#     q.put(info)
#     print(f'func1：{info}')
#
#
# def func2(q):
#    info = q.get()
#    print(f'func2：{info}')
#    q.put(info)
#
#
#
# def func3(q):
#     i = q.get()
#     print(f'func3: {i}')
#
# if __name__ == '__main__':
#     q = Queue(3)
#     P1 = Process(target=func1, args=(q,))
#     P2 = Process(target=func2, args=(q,))
#     P3 = Process(target=func3, args=(q,))
#     P1.start()
#     P1.join()
#     P2.start()
#     P2.join()
#     P3.start()
#     P3.join()

#2，写一个包含10个线程的程序，，每一个子线程执行的时候都需要打印当前线程名、当前活跃线程数量
# import threading
# import time
# names = locals()
# lis = []
#
# def func(name):
#     print(f'进程{name}开始执行，当前活跃进程数量{len(threading.enumerate())}')
#     time.sleep(0.1)
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         names['t' + str(i)] = threading.Thread(target=func,args=(f"p{i}",))
#         lis.append(names['t' + str(i)])
#     for i in lis:
#         i.start()
#     for i in lis:
#         i.join()
#

#3，已知列表 info = [1,2,3,4,55,233]生成6个线程对象,每次线程输出一个值，最后输出："the end"
# import threading
#
# info = [1,2,3,4,55,233]
# s = ['t','h','e ','e','n','d']
#
# def func(i):
#     print(i,end='')
#
# if __name__ == '__main__':
#     for i in s:
#         t = threading.Thread(target=func,args=(i,))
#         t.start()

#4，有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，每个刷卡机每天一共刷100次。账户原有500块。所以当天最后的总账应该为1500

import threading
num = 500
mutex = threading.Lock()

def func():
    mutex.acquire()
    global num
    for i in range(100):
        num += 1
    mutex.release()

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()
        t.join()
print(f'账户中有{num}元')



