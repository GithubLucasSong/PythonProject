# 首先把昨天没有写完的作业继续写,今天没有写完的明天可以继续写
#
# 1.有如下
# v1 = {'郭宝元','alex','板哥','王二麻子'}
# v2 = {'alex','王二麻子'}
# 请得到 v1 和 v2 的交集并输出
# 请得到 v1 和 v2 的并集并输出
# 请得到 v1 和 v2 的 差集并输出
# 请得到 v2 和 v1 的 差集并输出

# v1 = {'郭宝元','alex','板哥','王二麻子'}
# v2 = {'alex','王二麻子'}
# print(v1 & v2)  # 请得到 v1 和 v2 的交集并输出
# print(v1 | v2)  # 请得到 v1 和 v2 的并集并输出
# print(v1 - v2)  # 请得到 v1 和 v2 的 差集并输出
# print(v2 - v1)  # 请得到 v2 和 v1 的 差集并输出

#
# 2.循环提示用户输入，如果输入的内容在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
# v1 = []
# v2 = []
# while True:
#     i = input('请输入：')
#     if i.upper() == 'N':
#         print(v1,v2)
#         exit()
#     else:
#         v2.append(i) if i in v1 else v1.append(i)


#
# 3.is 和 == 的区别？
# is是判断两边的内存地址是否一致   ==是判断两边的值是否一致


#
# 4.type和id的作用？
# type是查看类型  id是查看内存地址
#


# 5.看代码写结果并解释原因
#
# v1 = {'k1':'v1','k2':[1,2,3]}
# v2 = {'k1':'v1','k2':[1,2,3]}
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)  #true
# print(result2)  #false


# 6.看代码写结果并解释原因
#
# v1 = {'k1':'v1','k2':[1,2,3]}
# v2 = v1
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)  # true
# print(result2)  # true


# 7.看代码写结果并解释原因
#
# v1 = {'k1':'v1','k2':[1,2,3]}
# v2 = v1
# v1['k1'] = 'meet'
# print(v2)



# 8.看代码写结果并解释原因
#
# v1 = '人生苦短，我用Python'
# v2 = [1,2,3,4,v1]
# v1 = "人生苦短，用毛线Python"
# print(v2)


# 9.看代码写结果并解释原因
#
# info = [1,2,3]
# userinfo = {'account':info, 'num':info, 'money':info}
# info.append(9)
# print(userinfo)  # {'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}
# info = "题怎么这么多"
# print(userinfo)  # {'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}


# 10.看代码写结果并解释原因
#
# info = [1,2,3]
# userinfo = [info,info,info,info,info]
# info[0] = '不仅多，还特么难呢'
# print(info,userinfo)


# 11.看代码写结果并解释原因
#
# info = [1,2,3]
# userinfo = [info,info,info,info,info]
# userinfo[2][0] = '他扒拉我'
# print(info,userinfo)



# 12.看代码写结果并解释原因
#
# data = {}
# for i in range(10):
#     data['user'] = i
# print(data)


# 13.看代码写结果并解释原因
#
# data_list = []
# data = {}
# for i in range(10):
#     data['user'] = i
#     data_list.append(data)
# print(data_list)


# 14.看代码写结果并解释原因
#
# data_list = []
# for i in range(10):
#     data = {}
#     data['user'] = i
#     data_list.append(data)
# print(data_list)


# 15.看代码写结果(以下内容如果不是很清楚的多画画图)
#
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
# v1.append(6)
# print(v1)
# print(v2)


# 16.看代码写结果
#
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)
# print(v2)


# 17.看代码写结果，并解释每一步的流程。
#
# v1 = [1,2,3,4,5,6,7,8,9]
# v2 = {}
# for item in v1:
#     if item < 6:
#         continue
#     if 'k1' in v2:
#         v2['k1'].append(item)
#     else:
#         v2['k1'] = [item]
# print(v2)


# 18.看代码写结果
#
# import copy
# v1 = "alex"
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2)  #true
# print(v1 is v3)  #true

# 19.看代码写结果
#
# import copy
# v1 = [1,2,3,4,5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2) # false
# print(v1 is v3) # false


# 20.看代码写结果
#
# import copy
# v1 = [1,2,3,4,5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[0] is v2[0]) # true
# print(v1[0] is v3[0]) # true
# print(v2[0] is v3[0]) # true


# 21.看代码写结果
#
# import copy
# v1 = [1,2,3,4,[11,22]]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[-1] is v2[-1]) # true
# print(v1[-1] is v3[-1]) # false
# print(v2[-1] is v3[-1]) # false


# 22.看代码写结果
#
# import copy
#
# v1 = [1,2,3,{"name":'宝元',"numbers":[7,77,88]},4,5]
# v2 = copy.copy(v1)
#
# print(v1 is v2) # false
#
# print(v1[0] is v2[0]) # ture
# print(v1[3] is v2[3]) # ture
#
# print(v1[3]['name'] is v2[3]['name']) # true
# print(v1[3]['numbers'] is v2[3]['numbers']) # true
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1]) #true


# 23.看代码写结果
#
# import copy
# v1 = [1,2,3,{"name":'宝元',"numbers":[7,77,88]},4,5]
# v2 = copy.deepcopy(v1)
# print(v1 is v2) # false
# print(v1[0] is v2[0]) # ture
# print(v1[3] is v2[3]) # false
#
# print(v1[3]['name'] is v2[3]['name']) #ture
# print(v1[3]['numbers'] is v2[3]['numbers']) # false
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1]) #true