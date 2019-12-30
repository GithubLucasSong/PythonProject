#1，简述线程和协程的异同?
# 相同点：占用空间小，适合用来进行IO操作
# 不同点；协程是比线程更小的执行单元，一个线程可以创建多个协程

#2，什么是并行，什么是并发？
#并行是多个任务同时执行，并发实际为多个任务循环交由系统调度执行，但在同一时间只有一个任务被系统调度执行

#3，请解释同步和异步这两个概念？
#同步为多个任务按照一定顺序依次执行，执行完一个任务才会继续执行下一个任务
#异步为多个任务同时执行，不限制任务的执行顺序

#4，GIL锁是怎么回事?
# GIL锁是python解释器层面加的全局解释器锁，这个锁是互斥锁，导致同一时间只有一个线程在执行。所以python实际上不能使用多核

#5，什么叫死锁？如何产生？如何解决
# 多个线程同时争抢多把互斥锁，就可能发成阻塞，这就是死锁，
#解决方法：弄清逻辑

#6，写一个程序，利用queue实现进程间通信；
# from multiprocessing import Queue,Process
# def func1(q):
#     q.put('info')
#     print('放入一条数据')
# def func2(q):
#     i = q.get()
#     print(f'获取一条数据{i}')
#
# if __name__ == '__main__':
#     q = Queue(3)
#     p1 = Process(target=func1,args=(q,))
#     p2 = Process(target=func2, args=(q,))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()

#7，写一个程序，包含十个线程，同时只能有五个子线程并行执行
# import threading
# import time
# s = threading.Semaphore(5)
# def func1():
#     s.acquire()
#     print('正在执行')
#     time.sleep(2)
#     s.release()
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = threading.Thread(target=func1)
#         t.start()

#8，写一个程序，线程C在线程B后执行，线程B在线程A之后进行
# import threading,time
# def func1():
#     while True:
#         if lock1.acquire():
#             print('A')
#             lock2.release()
# def func2():
#     while True:
#         if lock2.acquire():
#             print('B')
#             lock3.release()
# def func3():
#     while True:
#         if lock3.acquire():
#             print('C')
#             lock1.release()
# if __name__ == '__main__':
#     A = threading.Thread(target=func1)
#     B = threading.Thread(target=func2)
#     C = threading.Thread(target=func3)
#     lock1 = threading.Lock()
#     lock2 = threading.Lock()
#     lock2.acquire()
#     lock3 = threading.Lock()
#     lock3.acquire()
#     A.start()
#     B.start()
#     C.start()


#9，编写一个程序，开启3个线程，这3个线程的name分别为A、B、C，每个线程将自己的name在屏幕上打印10遍，要求输出结果必须按ABC的顺序显示；如：ABCABC….依次递推
# import threading,time
# num = 0
# def func1():
#     global num
#     while True:
#         if num < 10:
#             if lock1.acquire():
#                 print(A.name)
#                 num += 1
#                 lock2.release()
#         else:
#             break
# def func2():
#     while True:
#         if num < 10:
#             if lock2.acquire():
#                 print(B.name)
#                 lock3.release()
#         else:
#             break
# def func3():
#
#     while True:
#         if num < 10:
#             if lock3.acquire():
#                 print(C.name)
#
#                 lock1.release()
#         else:
#             break
# if __name__ == '__main__':
#     lock1 = threading.Lock()
#     lock2 = threading.Lock()
#     lock2.acquire()
#     lock3 = threading.Lock()
#     lock3.acquire()
#     A = threading.Thread(target=func1,name='A')
#     B = threading.Thread(target=func2,name='B')
#     C = threading.Thread(target=func3,name='C')
#
#     A.start()
#     B.start()
#     C.start()



import threading
num = 0
def func1():
    while True:
        if num < 10:
            if lock1.acquire():
                print(A.name)
                lock2.release()
        else:
            break
def func2():
    while True:
        if num < 10:
            if lock2.acquire():
                print(B.name)
                lock3.release()
        else:
            break
def func3():
    global num
    while True:
        if num < 10:
            if lock3.acquire():
                print(C.name)
                num += 1
                lock1.release()
        else:
            break
if __name__ == '__main__':
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    lock2.acquire()
    lock3 = threading.Lock()
    lock3.acquire()
    A = threading.Thread(target=func1,name='A')
    B = threading.Thread(target=func2,name='B')
    C = threading.Thread(target=func3,name='C')

    A.start()
    B.start()
    C.start()


# 10，简述生产者与消费者模式（用自己的话默写）

# 生产者就是产生数据的线程，消费者就是消费数据的线程，因为生产数据的速度和消费数据的速度大部分情况下是不相等的
# 所以两者之间会产生强耦合关系
# 解决生产者和消费者之间强耦合状态的方法就是在两者中使用一个缓冲区来沟通数据。
# 缓冲区快满时，生产者可以暂停生产。