# import threading
# mulex = threading.Lock()
# num = 0
# def func1():
#     mulex.acquire()
#     global num
#     for i in range(1000000):
#         num +=1
#     print('func1',num)
#     mulex.release()
#
#
# def func2():
#     mulex.acquire()
#     global num
#     for i in range(1000000):
#         num +=1
#     print('func2',num)
#     mulex.release()
#
# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('主线程',num)

# from multiprocessing import Process
#
# def func1():
#     print()
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=func1)
#         print(p.name)
#         p.start()
#         p.join()



class A():
    def func(self):
        print(self.xxx)

a = A()
a.xxx = '123'
a.func()


# def func():
#     print(xxx)
# func.xxx = '123'
