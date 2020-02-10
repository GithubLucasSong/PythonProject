# from multiprocessing import Process
# def run(name):
#     print('子进程正在运行，name= %s'%(name))
# if __name__ == '__main__':
#     print('父进程启动')
#     p = Process(target = run,args = ('test',))
#     #target表示调用对象，args表示调用对象的位置参数元组
#     #注意：元组中只有一个元素时结尾要加逗号
#     print('子进程将要执行')
#     p.start()
#     print(p.name)
#     p.join()
#     print('子进程结束')
#

from multiprocessing import Process
import time
def run():
    time.sleep(1)
    print('子进程正在运行')
    print(__name__)

if __name__ == '__main__':
    print('父进程启动')
    p = Process(target = run)
    #target表示调用对象，args表示调用对象的位置参数元组
    #注意：元组中只有一个元素时结尾要加逗号
    print('子进程将要执行')
    p.start()
    print(p.name)
    p.join()
    print('子进程结束')