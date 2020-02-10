# from multiprocessing import Process
# num = 5
# def func1():
#     global num
#     num += 5
#     print(num)
#
# def func2():
#     global num
#     num +=10
#     print(num)
#
# if __name__ == '__main__':
#     p1 = Process(target=func1)
#     p2 = Process(target=func2)
#     p1.start()
#     p2.start()
#
# import multiprocessing
# import time
# class ClockProcess(multiprocessing.Process):
#     def run(self):
#         print('hello word')
#         print(__name__)
#
# if __name__ == '__main__':
#     p = ClockProcess()
#     p.start()

# import multiprocessing
# import random,time
#
#
# def func():
#     print(time.time())
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     po = multiprocessing.Pool(3)
#     for i in range(100):
#         po.apply_async(func)
#     po.close()
#     po.join()

import multiprocessing
q = multiprocessing.Queue(3)
q.put('1')
q.put('2')
q.put('3')
print(q.get())
