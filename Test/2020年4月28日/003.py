# #这里附件的MIME和文件名，这里是xls类型
#         mime = MIMEBase('zip','zip',filename='周末日报.zip')
#         #加上必要的头信息
#         mime.add_header('Content-Disposition','attachment',filename=('gb2312', '', '周末日报.zip'))
#         mime.add_header('Content-ID','<0>')
#         mime.add_header('X-Attachment-Id','0')
#         #把附件的内容读进来
#         mime.set_payload(f.read())
#         #用Base64编码
#         encoders.encode_base64(mime)
#         msg_list.attach(mime)
#     server_pre(msg_list)
#     print(">>>发送邮件成功！")
# ————————————————
# 版权声明：本文为CSDN博主「cyber_1987」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_42029733/java/article/details/86559612