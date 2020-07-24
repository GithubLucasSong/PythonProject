# import pandas as pd
# import tushare as ts
# #读取本地数据
# df = pd.read_csv('./maotai.csv')
# df.head(5)
# print(df.info())
# print('分割')
# #每一列的数据类型
# #哪些列中存在空值
# df['date'] = pd.to_datetime(df['date'])
# print(df.info())
# #将date列作为源数据的行索引
# df.set_index('date',inplace=True)
# print('分割')
# print(df.info())
# print(df)

# class Abx():
#     xxx=666
#     def func(self,):
#         print(self.xxx)
#
#
#
# Abx.func(Abx)

# a =  ['a','s','d','f','g','h','j','k']
# print(a[0:-1])

#
# s='yyyyyyyyy'
# print(s)
#
# s = str()
# s.
# print(s)


class Foo():
    name = '456'


f = Foo()
# print(Foo.name)
print(f.name)