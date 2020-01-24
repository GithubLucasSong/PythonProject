# 1.有如下文件，a1.txt，里面的内容为：
#
# 老男孩是最好的学校，
# 全心全意为学生服务，
# 只为学生未来，不为牟利。
# 我说的都是真的。哈哈
# 分别完成以下的功能：
# a,将原文件全部读出来并打印。
# f = open('a1.txt',mode='r',encoding='utf-8')
# print(f.read())

# b,在原文件后面追加一行内容：信不信由你，反正我信了。
# f = open('a1.txt',mode='a',encoding='utf-8')
# f.write('\n信不信由你，反正我信了')
# f = open('a1.txt',mode='w',encoding='utf-8')

# c,将原文件全部清空，换成下面的内容：
# 每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你会发现，
# 你的进步越来越大。
# f = open('a1.txt',mode='w',encoding='utf-8')
# f.write('''每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你就会发现，
# 你的进步越来越大。''')


# 2.有如下文件，t1.txt,里面的内容为：
#
# 葫芦娃，葫芦娃，
# 一根藤上七个瓜
# 风吹雨打，都不怕，
# 啦啦啦啦。
# 我可以算命，而且算的特别准:
# 上面的内容你肯定是心里默唱出来的，对不对？哈哈
# 分别完成下面的功能：
# a,以r的模式打开原文件，利用for循环遍历文件句柄。
# f = open('t1.txt',mode='r',encoding='utf-8')
# for i in f:
#     print(i)

# b,以r模式读取‘葫芦娃，’前四个字符。
# f = open('t1.txt',mode='r',encoding='utf-8')
# print(f.read(4))

# c,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
# f = open('t1.txt',mode='r',encoding='utf-8')
# print(f.readline().strip())

# d,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将原内容全部读取出来。
# f = open('t1.txt',mode='a+',encoding='utf-8')
# f.write('\n老男孩教育')
# f.seek(0)
# print(f.read())



# 3.文件a.txt内容：每一行内容分别为商品名字，价钱，个数。 (20分钟)
#
# apple 10 3
# tesla 100000 1
# mac 3000 2
# lenovo 30000 3
# chicken 10 3
# 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
# f = open('a.txt',mode='r',encoding='utf-8')
# content = []
# money = 0
# for i in f:
#     lis = []
#     dic = {}
#     i = i.strip()
#     lis = i.split(' ')
#     print(lis)
#     dic['name'] = lis[0]
#     dic['price'] = int(lis[1])
#     dic['amount'] = int(lis[2])
#     money += dic['price'] * dic['amount']
#     content.append(dic)
# print(content)
# print(f'总价是：{money}')



#
# 4.有如下文件：
#
# alex是老男孩python发起人，创建人。
# alex其实是人妖。
# 谁说alex是sb？
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
# 将文件中所有的alex都替换成大写的SB（文件的改的操作）。
# f = open('4.txt',mode='r',encoding='utf-8')
# data = f.read()
# new_data = data.replace('alex','sb')
# f1 = open('4.txt',mode='w',encoding='utf-8')
# f1.write(new_data)



#
# 5.文件a1.txt内容,建议写的支持扩展 (35分钟)
#
# name:apple price:10 amount:3 year:2012
# name:tesla price:100000 amount:1 year:2013
# 通过代码，将其构建成这种数据类型：
# [{'name':'apple','price':10,'amount':3,year:2012},
# {'name':'tesla','price':1000000,'amount':1}]
# 并计算出总价钱。
# f = open('5.txt',mode='r',encoding='utf-8')
# lis = []
# for i in f:
#     dic = {}
#     i_lis = i.split(' ')
#     for i in i_lis:
#         dic[i.split(':')[0]] = i.split(':')[1]
#     lis.append(dic)
#
# print(lis)




# 6.文件a1.txt内容,建议写的支持扩展 (40分钟)
#
# # 序号     部门      人数      平均年龄      备注
# # 1       python    30         26         单身狗
# # 2       Linux     26         30         没对象
# # 3       运营部     20         24         女生多
# 通过代码，将其构建成这种数据类型：
# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},
# # ......]



f = open('6.txt',mode='r',encoding='utf-8')
lis = []
f1 = f.readline()
a,b,c,d,e = f1.split()
for i in f:
    dic = {}
    a1,b1,c1,d1,e1 = i.split()
    # dic[a] = a1
    # dic[b] = b1
    # dic[c] = c1
    # dic[d] = d1
    # dic[e] = e1
    dic = {a:a1,b:b1,c:c1,d:d1,e:e1}
    lis.append(dic)
print(lis)
