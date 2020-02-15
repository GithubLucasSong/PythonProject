# 1.使用列表推导式求出50以内能被3整除的数的平方，并放入到一个列表中。
#
list = [i**2 for i in range(1,51) if i%3 == 0]
print(list)
# 2.使用列表推导式构建这样一个列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
#
list = [f'python{i}期' for i in range(1,11)]
print(list)
# 3.求结果(面试题)

# v = [lambda :x for x in range(10)]
# print(v) 列表中10个lambda函数地址
# print(v[0]) lambda:0
# print(v[0]()) 0

# 4.求结果(面试题)
#
# v = (lambda :x for x in range(10))
# print(v) 10个函数地址
# print(v[0]) 1个函数地址
# print(v[0]()) 9
# print(next(v)) 第二个函数地址
# print(next(v)()) 9
# 5.求结果：（面试题）
#
# def num():
#     return [lambda x:x**i for i in range(4)] #[lambda x:x**0,lambda x:x**1,lambda x:x**2,lambda x:x**3,]
# print([m(2)for m in num()]) #[0 2 4 8]

#
# 6.求结果 : (面试题)
#
# ret = [lambda x:x*i for i in range(5)] #[lambda x:x*4，lambda x:x*4，lambda x:x*4，lambda x:x*4，]
# ret1 = [em(2) for em in ret] # [8,8,8,8]
# print(ret1)
# 7.求结果 : (面试题)
#
# ret = (lambda x:x*i for i in range(5)) #
# ret1 = [em(2) for em in ret]
# print(ret1)
# 8.求结果 : (面试题)
#
# def wrapper(f):
#     def inner(*args, **kwargs):
#         print(111)
#         ret = f(*args, **kwargs)
#         print(222)
#         return ret
#
#     return inner
#
#
# def func():
#     print(333)
#
# func() #123
#
# ret = wrapper(func)
# ret() 111 123 222