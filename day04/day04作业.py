# 1.写代码，有如下列表，按照要求实现每一个功能
#
#  li = ["alex", "WuSir", "meet","女神","太白"]
# ​ 1. 计算列表的长度并输出
# ​ 2.列表中追加元素"seven",并输出添加后的列表
# ​ 3.请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# ​ 4.请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# ​ 5.请删除列表中的元素"meet",并输出删除后的列表
# ​ 6.请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# ​ 7.请删除列表中的第2至4个元素，并输出删除元素后的列表

# li = ["alex", "WuSir", "meet","女神","太白"]
#
# # ​ 1. 计算列表的长度并输出
# print(len(li))
#
# # ​ 2.列表中追加元素"seven",并输出添加后的列表
# li.append('seven')
# print(li)
#
# # ​ 3.请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li.insert(0,'Tony')
# print(li)
#
# # ​ 4.请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li[1] = 'Kelly'
# print(li)
#
# # ​ 5.请删除列表中的元素"meet",并输出删除后的列表
# li.remove('meet')
# print(li)
#
# # ​ 6.请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# print(li.pop(1))
# print(li)
#
# # ​ 7.请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:4]
# print(li)


# 2.写代码，有如下列表，利用切片实现每一个功能
#
# ```
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# # 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# print(li[:3])
# # 通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
# print(li[::2])
# # 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# print(li[1:-1:2])
# # 通过对li列表的切片形成新的列表l5,l5 = ["c"]
# print(li[-1:])
# # 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
# print(li[-3:0:-2])


# 3.写代码，有如下列表，按照要求实现每一个功能。
#
# lis = [2, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
#
# # 将列表lis中的"tt"变成大写。
# lis[2][2][1][0] = lis[2][2][1][0].upper()
# print(lis)
# # 将列表中的数字3变成字符串"100"。
# lis[2][2][1][1] = '100'
# print(lis)
# # 将列表中的字符串"1"变成数字101。
# lis[2][2][1][2] = 101
# print(lis)

print(range(0,5))