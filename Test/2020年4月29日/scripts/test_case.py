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
import subprocess
import zipfile
from jsonpath_rw import parse
import re


def origin_data():
    book = xlrd.open_workbook(r'./接口测试示例-2.xlsx')

    sheet_by_name = book.sheet_by_name('Sheet1')

    # 获取行数和列数
    rows = sheet_by_name.nrows
    # print(rows)
    cols = sheet_by_name.ncols

    # 将每行都和首行组成字典，存放在一个列表中
    l = []
    title = sheet_by_name.row_values(0)
    # print(title)
    for row in range(1, rows):  # 123456
        l.append(dict(zip(title, sheet_by_name.row_values(row))))
    return l


def zip_file():
    subprocess.call("allure generate report/result -o report/allure_html --clean", shell=True)
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


def send_email():
    logging.basicConfig(
        filename='test.log',
        filemode='w',
        level=logging.DEBUG,
        datefmt='%Y/%m/%d %H:%M:%S',
        format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s'
    )
    # 发送邮件
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器   # 勿动
    mail_user = "1433880147@qq.com"  # 用户名
    mail_pass = "##"  # 口令
    # 设置收件人和发件人
    sender = '1433880147@qq.com'
    receivers = ['#1206180814#@qq.com', ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

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
        print("已发送邮件")
        logging.debug('已发送邮件')

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
        logging.debug('无法发送邮件')


@pytest.mark.parametrize('item', origin_data())
def test_case(item):
    allure.dynamic.title(item['title'])
    # allure.dynamic.description(item['case_description'])
    if item['case_num'] == 'neeo_001':
        response = requests.request(method=item['method'], url=item['url'], data=json.loads(item['data']))
        assert response.json()['code'] == str(json.loads(item['except'])['code'])
        if response.json()['code'] == str(json.loads(item['except'])['code']):
            with open('{}.txt'.format(item['case_num']), 'w', encoding='utf-8') as f:
                f.write(response.json()['data'])
                f.close()

    elif item['case_num'] == 'neeo_002':
        with open('neeo_001.txt', 'r', encoding='utf-8') as f:
            token = f.read()
        headers = item['headers']
        headers_dict = json.loads(headers)
        headers_dict["testfan-token"] = token
        headers = json.dumps(headers_dict)
        response = requests.request(method=item['method'], url=item['url'], params=json.loads(item['params']),
                                    headers=json.loads(headers))
        assert response.json()['code'] == str(json.loads(item['except'])['code'])

    elif item['case_num'] == 'neeo_003':
        response = requests.request(method=item['method'], url=item['url'], data=json.loads(item['data']))
        assert response.json()['code'] == str(json.loads(item['except'])['code'])
        if response.json()['code'] == str(json.loads(item['except'])['code']):
            with open('{}.txt'.format(item['case_num']), 'w', encoding='utf-8') as f:
                f.write(json.dumps(response.cookies.get_dict()))
                f.close()

    elif item['case_num'] == 'neeo_004':
        allure.dynamic.title(item['title'])
        with open('neeo_003.txt', 'r', encoding='utf-8') as f:
            cookie = f.read()
        cookie = json.loads(cookie)
        response = requests.request(method=item['method'], url=item['url'], params=json.loads(item['params']),
                                    cookies=cookie)
        assert response.json()['code'] == str(json.loads(item['except'])['code'])


def teardown_module():
    zip_file()
    send_email()


if __name__ == '__main__':
    pytest.main(['test_case.py'])

print(origin_data())
