# 1.请实现一个装饰器，限制该函数被调用的频率，如10秒一次（面试题）
#
import time
list = []
def wrapper(func):
    def inner():
        t = time.time()
        if len(list) == 0:
            func()
            list.append(t)
        else:
            t = time.time()
            if t - list[-1] >10:
                func()
                list.append(t)
            else:
                print('间隔不能少于10S')
        print(list)
    return inner
@wrapper
def func():
    print('执行函数')

while True:
    time.sleep(2)
    func()




# 2.请写出下列代码片段的输出结果：
# def say_hi(func):
#   def wrapper(*args,**kwargs):
#       print("HI")
#       ret=func(*args,**kwargs)
#       print("BYE")
#       return ret
#   return wrapper
#
# def say_yo(func):
#   def wrapper(*args,**kwargs):
#       print("Yo")
#       return func(*args,**kwargs)
#   return wrapper
# @say_hi
# @say_yo
# def func():
#   print("ROCK&ROLL")
# func()


# 3.编写装饰器完成下列需求:
# 用户有两套账号密码,一套为京东账号密码，一套为淘宝账号密码分别保存在两个文件中。
# 设置四个函数，分别代表 京东首页，京东超市，淘宝首页，淘宝超市。
# 启动程序后,呈现用户的选项为:
# 1,京东首页
# 2,京东超市
# 3,淘宝首页
# 4,淘宝超市
# 5,退出程序
# 四个函数都加上认证功能，用户可任意选择,用户选择京东超市或者京东首页,只要输入一次京东账号和密码并成功,则这两个函数都可以任意访问;用户选择淘宝超市或者淘宝首页,只要输入一次淘宝账号和密码并成功,则这两个函数都可以任意访问.
# 相关提示：用带参数的装饰器。装饰器内部加入判断，验证不同的账户密码。
#

# 4.给l1 = [1,1,2,2,3,3,6,6,5,5,2,2]去重，不能使用set集合（面试题）。
l1 = [1,1,2,2,3,3,6,6,5,5,2,2]
new_l1 = []
def x(s):
    for i in l1:
        if i not in new_l1:
            new_l1.append(i)

    print(new_l1)

x(l1)