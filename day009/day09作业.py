# 1.都完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：
#
# 用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
# l=[{'name':'alex'},{'name':'y'}]
l=[{'name':'alex'},{'name':'y'}]
def func(s):
    return s['name']+'sb'
print(list(map(func,l)))
# 2)用filter来处理,得到股票价格大于20的股票名字
#
# shares={
#  'IBM':36.6,
#  'Lenovo':23.2,
#  'oldboy':21.2,
#  'ocean':10.2,
#          }
shares={
 'IBM':36.6,
 'Lenovo':23.2,
 'oldboy':21.2,
 'ocean':10.2,
         }
print(list(filter(lambda x:shares[x]>20,shares)))
# 用filter过滤出单价大于100的股票。
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]

portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]
print(list(filter(lambda x:x['price']>100,portfolio)))

# 4)有下列三种数据类型，
#
#  l1 = [1,2,3,4,5,6]
#  l2 = ['oldboy','alex','wusir','太白','日天']
#  tu = ('**','***','****','*******')
# 写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）
#
#  [(3, 'wusir', '****'), (4, '太白', '*******')]
# 这样的数据。
l1 = [1,2,3,4,5,6]
l2 = ['oldboy','alex','wusir','太白','日天']
tu = ('**','***','****','*******')
def func(s):
    if int(s[0])>2 and len(s[2])>=4:
        return s
print(list(filter(func,zip(l1,l2,tu))))
#
# 5)有如下数据类型(实战题)：
#
#  l1 = [{'sales_volumn': 0},
#        {'sales_volumn': 108},
#        {'sales_volumn': 337},
#        {'sales_volumn': 475},
#        {'sales_volumn': 396},
#        {'sales_volumn': 172},
#        {'sales_volumn': 9},
#        {'sales_volumn': 58},
#        {'sales_volumn': 272},
#        {'sales_volumn': 456},
#        {'sales_volumn': 440},
#        {'sales_volumn': 239}]
# 将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
l1 = [{'sales_volumn': 0},
   {'sales_volumn': 108},
   {'sales_volumn': 337},
   {'sales_volumn': 475},
   {'sales_volumn': 396},
   {'sales_volumn': 172},
   {'sales_volumn': 9},
   {'sales_volumn': 58},
   {'sales_volumn': 272},
   {'sales_volumn': 456},
   {'sales_volumn': 440},
   {'sales_volumn': 239}]
print(sorted(l1,key=lambda x:x['sales_volumn']))
#
# 2.过滤掉长度小于3的字符串列表
# lst = ["alex","wusir","太白","宝元"]
lst = ["alex","wusir","太白","宝元"]
print(list(filter(lambda x:len(x)>=4,lst)))

#
# 3.有如下数据结构,通过过滤掉年龄大于16岁的字典
#
# lst = [{'id':1,'name':'alex','age':18},
#         {'id':1,'name':'wusir','age':17},
#         {'id':1,'name':'taibai','age':16},]
lst = [{'id':1,'name':'alex','age':18},
        {'id':1,'name':'wusir','age':17},
        {'id':1,'name':'taibai','age':16},]
print(list(filter(lambda x:int(x['age'])<=16,lst)))
# 4.有如下列表,按照元素的长度进行升序
#
# lst = ['天龙八部','西游记','红楼梦','三国演义']
lst = ['天龙八部','西游记','红楼梦','三国演义']
print(sorted(lst,key=lambda x:len(x)))
# 5.有如下数据,按照元素的年龄进行升序
#
# lst = [{'id':1,'name':'alex','age':18},
#     {'id':2,'name':'wusir','age':17},
#     {'id':3,'name':'taibai','age':16},]
lst = [{'id':1,'name':'alex','age':18},
    {'id':2,'name':'wusir','age':17},
    {'id':3,'name':'taibai','age':16},]
print(sorted(lst,key=lambda x:x['age']))
# 6.看代码叙说,两种方式的区别
#
# lst = [1,2,3,5,9,12,4]
# lst.reverse()原句修改
# print(lst)
#
# print(list(reversed(lst))) 开辟新的空间修改
# 7.list(map(str,[1,2,3,4,5,6,7,8,9]))输出是什么? (面试题)
#输入列表里面都是字符串的123456789
#
# 8.有一个数组[34,1,2,5,6,6,5,4,3,3]请写一个函数，找出该数组中没有重复的数
# 的总和（上面数据的么有重复的总和为1+2+4+34=41)(面试题)
lst = [34,1,2,5,6,6,5,4,3,3]
print(sum(list(filter(lambda x:lst.count(x) ==1,lst))))