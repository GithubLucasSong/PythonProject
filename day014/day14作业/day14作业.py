# 1.请编写一个函数实现将IP地址转换成一个整数。
# 如 10.3.9.12 转换规则为：
# 10 00001010
# 3 00000011
# 9 00001001
# 12 00001100
# 再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？

# ip = input('请输入IP地址')
# count = 0
#
# ip_lis = ip.split('.')
# ip_intlis = []
# for i in ip_lis:
#     ip_intlis.append(bin(int(i)))
# ip_str = ''.join(ip_intlis)
# ip_str = ip_str.replace('0b','')
# print(int(ip_str,2))


# def IP_to_int(ip):
#     li = [int(sub) for sub in ip.split(".")]
#
#     li = [format(s, "08b") for s in li]
#
#     binary = "".join(li)
#     return int(binary, base=2)
#
#
# if __name__ == "__main__":
#     print(IP_to_int("10.3.9.12"))


#
# 2.把aaabbcccd这种形式的字符串压缩成{"a":3,"b":2,"c":3,"d":1}这种形式。
# def func(str):
#     for i in str:
#         dic[i] = str.count(i)
#     return dic
#
#
# if __name__ == "__main__":
#     dic = {}
#     print(func("aaabbcccd"))



#
# 3.有 0 < x <= 10, 10 < x <= 20, 20 < x <= 30, .，190 < x〈= 200,200 < x 这样的
# 21个区间分别对应 1-21 二十一个级别，请编写一个函数 level (x)根据输
# 入数值返回对应级别。
# def level(x):
#     for i in range(21):
#         dic[f'level{i+1}'] = i*10 < int(x) <= (i+1)*10
#         if dic[f'level{i+1}'] == True:
#             print(f'level{i+1}')
#             continue
#
# if __name__ == "__main__":
#     dic = {}
#     level(input('请输入：'))
#######################################################
# def level(x):
#     for i in range(21):
#         if i*10 < int(x) <= (i+1)*10:
#             print(f'level为：{i+1}')
#             continue
#
# if __name__ == "__main__":
#     level(input('请输入：'))


#
# 4.使用re匹配验证码，验证码由字母，数学组成。
# import re
# s = 'a3sf ass3 sf3w sr3a WS2S s3F3 ssa sdf2f adsa_'
# print(re.findall('[a-zA-Z0-9]{4,}',s))


# 5.写一个正则表达式,匹配身份证号


# 6.写一个正则表达式，使其能同时识别下面所有的字符串：'bat', 'bit', 'but', 'hat', 'hit', 'hut‘

s = "bat bta atb bii bit but btu bt2 hit hat hut htu"
import re
print(re.findall("\w{2}t", s))