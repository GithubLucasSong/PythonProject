# from multiprocessing import Process
# def run(name):
#     print('子进程在运行中，name = %s'%(name))
# if __name__ == '__main__':
#     print('父进程启动')
#     p = Process(target = run ,args = ('test',))
#     #target表示调用对象，args表示调用对象的位置参数元组
#     # 注意：元组中只有一个元组时结尾要加，
#     print('子进程将要执行')
#     p.start()
#     print(p.name)
#     p.join()
#     print('子进程执行结束')


# 进程池
from multiprocessing import Pool
import random,time
def func1():
    print(1)
if __name__ =='__main__':
    po = Pool()
    for i in range(10):
        po.apply_async(func1())
    po.close()
    po.join()


