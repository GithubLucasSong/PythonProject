# import threading
# def func1():
#     while True:
#         if q1.acquire():
#             print('1')
#             q2.release()
#
# def func2():
#     while True:
#         if q2.acquire():
#             print('2')
#             q3.release()
#
#
# def func3():
#     while True:
#         if q3.acquire():
#             print('3')
#             q1.release()
#
# if __name__ == '__main__':
#     q1 = threading.Lock()
#     q2 = threading.Lock()
#     q2.acquire()
#     q3 = threading.Lock()
#     q3.acquire()
#     t1 = threading.Thread(target=func1)
#     t2 = threading.Thread(target=func2)
#     t3 = threading.Thread(target=func3)
#     t1.start()
#     t2.start()
#     t3.start()


# from multiprocessing import Process
# def run(name):
#     print('子进程正在运行，name= %s'%(name))
# if __name__ == '__main__':
#     print('父进程启动')
#     p = Process(target = run,args = ('test',))
#     print('子进程将要执行')
#     p.start()
#     print(p.name)
#     p.join()
#     print('子进程结束')

# from multiprocessing import Process
# num = 1
# def run1():
#     global num
#     num += 5
#     print('子进程1运行中，num = %d'%(num))
# def run2():
#     global num
#     num += 10
#     print('子进程2运行中，num = %d'%(num))
# if __name__ == '__main__':
#     print('父进程启动')
#     p1 = Process(target= run1)
#     p2 = Process(target= run2)
#     print('子进程将要执行')
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print('子进程结束')

# import multiprocessing
# import time
# class ClockProcess(multiprocessing.Process):
#     def run(self):
#         n = 5
#         while n > 0:
#             print(n)
#             time.sleep(1)
#             n -= 1
# if __name__ == '__main__':
#     p = ClockProcess()
#     p.start()
#     p.join()

# from multiprocessing import Pool
# import random,time
# def work(num):
#     print(random.random()*num)
#     time.sleep(3)
# if __name__ == '__main__':
#     po = Pool(3) #定义一个进程池，最大进程数为3，默认大小为CPU核数
#     for i in range(10):
#         po.apply_async(work,(i,)) # apply_async选择要调用的目标，每次循环会用空出来的子进程去调用目标
#     po.close() # 进程池关闭之后不会再接受新的请求
#     po.join() # 等待po中所有子进程结束，必须放在close后面
# # 在多进程中，主进程一般用来等待，真正的任务都在子进程中执行