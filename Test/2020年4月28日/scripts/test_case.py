import xlrd
import os
import unittest
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from HTMLTestRunner import HTMLTestRunner
from email import encoders  # 转码
from datetime import date
import pytest
import requests
import allure
import json
import logging

logging.basicConfig(
    filename='test.log',
    filemode='w',
    level=logging.DEBUG,
    datefmt='%Y/%m/%d %H:%M:%S',
    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s'
)

book = xlrd.open_workbook(r'../接口测试示例.xlsx')

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
for row in range(1, rows):  # 123456
    l.append(dict(zip(title, sheet_by_name.row_values(row))))


# print(l)


@pytest.mark.parametrize('item', l)
def test_case(item):
    allure.dynamic.title(item['case_title'])
    allure.dynamic.description(item['case_description'])
    response = requests.request(method=item['case_method'], url=item['case_url'])
    assert str(response.json()['success']) == json.loads(item['case_expect'])['success'].capitalize()


def teardown_module():
    import subprocess
    subprocess.call("allure generate report/result -o report/allure_html --clean", shell=True)

    import zipfile  # 导入模块
    BASE_DIR = 'report'
    base_dir = os.path.join(BASE_DIR, 'allure_html')  # 要压缩文件夹的根路径
    zip_file_name = 'case.zip'
    f = zipfile.ZipFile(os.path.join(BASE_DIR, zip_file_name), 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_name, file_names in os.walk(base_dir):
        # 要是不replace，就从根目录开始复制
        file_path = dir_path.replace(base_dir, '')
        # 实现当前文件夹以及包含的所有文件
        file_path = file_path and file_path + os.sep or ''
        for file_name in file_names:
            f.write(os.path.join(dir_path, file_name), file_path + file_name)
    f.close()

    # 发送邮件
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器   # 勿动
    mail_user = "1433880147@qq.com"  # 用户名
    mail_pass = "#fictfnyfncnihhbj"  # 口令
    # 设置收件人和发件人
    sender = '1433880147@qq.com'
    receivers = ['8@qq.com', ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例对象
    message = MIMEMultipart()

    # 邮件主题、收件人、发件人
    subject = '宋煜'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("{}".format(sender), 'utf-8')  # 发件人
    message['To'] = Header("{}".format(';'.join(receivers)), 'utf-8')  # 收件人

    # 构造附件
    file_path = './report/case.zip'
    f = open(file_path, 'rb')
    send_content = f.read()
    att = MIMEBase('zip', 'zip', filename='测试.zip')
    att.set_payload(send_content)
    # 用Base64编码
    encoders.encode_base64(att)
    att["Content-Type"] = 'application/octet-stream'
    file_name = 'result.zip'
    att["Content-Disposition"] = 'attachment; filename="{}"'.format(file_name)  # # filename 为邮件附件中显示什么名字
    message.attach(att)

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        smtp_obj.quit()
        logging.debug('debug level: 10')

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
        logging.debug('邮件发送失败')


if __name__ == '__main__':
    pytest.main(['test_case.py'])
