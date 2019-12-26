# 1，尝试不使用进程池，可否循环创建多个进程并调用(实现同步)
from multiprocessing import Process
import time
names = locals()

lis = []
def func1(name):
    print(f'子进程func1正在执行，进程{name}')
    time.sleep(5)
    print(f'子进程func1执行结束，进程{name}')



if __name__ == '__main__':
    for i in range(20):
        names['p'+str(i)] = Process(target=func1,args=(f"p{i}",))
        lis.append(names['p'+str(i)])
    for i in lis:
        i.start()
        print(f'进程ID:{i.pid}')
    for i in lis:
        i.join()


# 2，改写下列程序，分别别实现下述打印效果
#
# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     print('-------->4')
# 效果一：保证最先输出-------->4
#
# -------->4
# -------->1
# -------->3
# -------->2
# 效果二：保证最后输出-------->4
#
# -------->2
# -------->3
# -------->1
# -------->4
# 效果三：保证按顺序输出
#
# -------->1
# -------->2
# -------->3
# -------->4

#效果一：保证最先输出-------->4
# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('--------->%s'%n)
#
# if __name__ =='__main__':
#     p1 = Process(target=task,args=(1,))
#     p2 = Process(target=task,args=(2,))
#     p3 = Process(target=task, args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     print('--------->4')

#效果二：保证最后输出-------->4
# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     print('--------->%s'%n)
#
# if __name__ =='__main__':
#     p1 = Process(target=task,args=(1,))
#     p2 = Process(target=task,args=(2,))
#     p3 = Process(target=task, args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     time.sleep(1)
#     print('--------->4')

#效果三：保证按顺序输出
# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     print('--------->%s'%n)
#
# if __name__ =='__main__':
#     p1 = Process(target=task,args=(1,))
#     p2 = Process(target=task,args=(2,))
#     p3 = Process(target=task, args=(3,))
#
#     p1.start()
#     time.sleep(1)
#     p2.start()
#     time.sleep(1)
#     p3.start()
#     time.sleep(1)
#     print('--------->4')