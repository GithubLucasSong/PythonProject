import xlrd


book = xlrd.open_workbook(r'./接口测试示例.xlsx')

sheet_by_name = book.sheet_by_name('自动化测试')

# 获取行数和列数
rows = sheet_by_name.nrows
# print(rows)
cols = sheet_by_name.ncols

# #读取每行的内容
# for row in range(rows):
#     # 使用 row方法读取
#     # print(sheet_by_name.row(row))
#     # 也可以使用row_values读取
#     print(sheet_by_name.row_values(row))

# # 读取每列的内容
# for col in range(cols):
#     # 下面两种方法都可以
#     # print(sheet_by_name.col(col))
#     print(sheet_by_name.col_values(col))

# 读取固定列的内容
# print(sheet_by_name.cell(0, 0))
# print(sheet_by_name.cell_value(0, 0))

# 将每行都和首行组成字典，存放在一个列表中
l = []
title = sheet_by_name.row_values(0)
# print(title)
for row in range(1, rows): # 123456
    l.append(dict(zip(title, sheet_by_name.row_values(row))))
# print(l)



import pytest
import requests
import allure
import json


def test_case():
    for item in l:
        allure.dynamic.title(item['case_title'])
        allure.dynamic.description(item['case_description'])
        response = requests.request(method=item['case_method'],url=item['case_url'])
        print(response.json()['success'])
        print(type(str(response.json()['success'])))
        print(json.loads(item['case_expect'])['success'].capitalize())



test_case()

