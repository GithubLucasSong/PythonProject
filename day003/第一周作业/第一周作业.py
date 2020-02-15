# 有变量name = "aleX leNb" 完成如下操作：(20分钟)
#
# 1. 移除 name 变量对应的值两边的空格,并输出处理结果
# 2. 移除 name 变量对应的值两边的空格,并输出处理结果
# 3. 判断 name 变量是否以 "al" 开头,并输出结果
# 4. 判断name变量是否以"Nb"结尾,并输出结果
# 5. 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
# 6. 将name变量对应的值中的第一个"l"替换成"p",并输出结果
# 7. 将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
# 8. 将name变量对应的值根据第一个"l"分割,并输出结果。
# 9. 将 name 变量对应的值变大写,并输出结果
# 10. 将 name 变量对应的值变小写,并输出结果
# 11. 判断name变量对应的值字母"l"出现几次，并输出结果
# 12. 如果判断name变量对应的值前四位"l"出现几次,并输出结果
# 13. 请输出 name 变量对应的值的第 3 个字符?
# 14. 请输出 name 变量对应的值的前 4 个字符?
# 15. 请输出 name 变量对应的值的后 7 个字符?

# name = 'aleX leNb'
# print(name.strip()) #1
# print(name.strip()) #2
# print(name.startswith('al')) #3
# print(name.endswith('Nb')) #4
# print(name.replace('l','p')) #5
# print(name.replace('l','p',1)) #6
# print(name.split('l')) #7
# print(name.split('l',1)) #8
# print(name.upper()) #9
# print(name.lower()) #10
# print(name.count('l')) #11
# print(name[:4].count('l')) #12
# print(name[2]) #13
# print(name[:4]) #14
# print(name[-7:]) #15

# 有字符串s = "123a4b5c" (10分钟)
#
# 1. 通过对s切片形成新的字符串s1,s1 = "123"
# 2. 通过对s切片形成新的字符串s2,s2 = "a4b"
# 3. 通过对s切片形成新的字符串s3,s3 = "1345"
# 4. 通过对s切片形成字符串s4,s4 = "2ab"
# 5. 通过对s切片形成字符串s5,s5 = "c"
# 6. 通过对s切片形成字符串s6,s6 = "ba2"

# s = "123a4b5c"
# s1 = s[0:3]
# print(s1)
#
# s2 = s[3:-2]
# print(s2)
#
# s3 = s[::2]
# print(s3)
#
# s4 = s[1:-1:2]
# print(s4)
#
# s5 = s[-1::]
# print(s5)
#
# s6 = s[-3::-2]
# print(s6)


#使用while循环和for循环分别打印字符串s="asdfer"中每个元素(10分种)


# s="asdfer"
# num = 0
# while num < len(s):
#     print(s[num])
#     num +=1
#
# for i in s:
#     print(i)


#使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"(5分钟)
# s="asdfer"
# for i in s:
#     print(s)
#
# #使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb(10分钟)
# s="abcdefg"
# for i in s:
#     print(i+'sb')
#
# #使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发!"(15分钟)
# s="321"
# for i in s:
#     print(f'倒计时{i}秒')
# print('出发!')
#
# #实现一个整数加法计算器（多个数相加）：(20分钟)
# #如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算
# content = input('请输入内容：')
# lis = content.split('+')
# num = 0
# for i in lis:
#     num += int(i)
# print(num)

#计算用户输入的内容中有几个整数（以个位数为单位）。(15分钟)
#如：content = input("请输入内容：") # 如fhdal234slfh98769fjdla

# content = input("请输入内容：")
# count = 0
# for i in content:
#     if i.isdecimal():
#         count += 1
# print(f'有{count}个整数')

#判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海⾃来⽔来⾃海上(5分钟)
# coutent = input('请输入：')
# if coutent[::-1] == coutent:
#     print('这是回文')
# else:
#     print('这不是回文')

#实现一个整数加减法的计算器（3个数相加）：(20分钟)
# coutent = input('请输入：')
# new_coutent = coutent.replace('-','+-')
# lst = new_coutent.split('+')
# sum = int(lst[0]) + int(lst[1]) + int(lst[2])
# print(sum)

#实现一个整数加减法的计算器（多个数相加）：(30分钟)
# coutent = input('请输入:')
# new_coutene = coutent.replace('-','+-')
# lst = new_coutene.split('+')
# sum = 0
# for i in lst:
#     sum += int(i)
# print(sum)



