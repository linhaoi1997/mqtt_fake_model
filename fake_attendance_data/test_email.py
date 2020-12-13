#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "15774518534@163.com"  # 用户名
mail_pass = "shanbuzaigao123"  # 口令

sender = '15774518534@163.com'
receivers = ["15774518534@163.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('报警测试', 'plain', 'utf-8')
message['From'] = Header("15774518534@163.com", 'utf-8')
message['To'] = Header("林", 'utf-8')

subject = '测试邮件发送报警，没错，有数据错误'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")