#!/usr/local/bin/python
# -*- coding:utf8 -*-
# creater: doubledna
# createtime: 2017/07/11
# versions: 1
# function: send email

import smtplib
import string
# from email.mime.text import MIMEText
import psutil

# collect server information
# memory
m = psutil.virtual_memory()
mem = ("剩余内存量: " + str(int(m.free/1024/1024)) + "M")
# cpu
cpu = ("CPU使用量: " + str(psutil.cpu_percent(1)) + "%")
# disk
d = psutil.disk_usage('/')
root = ("根目录磁盘剩余量: " + str(d.used/1024/1024) + "M")
h = psutil.disk_usage('/dev/shm')
shm =  ("/dev/shm/磁盘剩余量: " + str(h.used/1024/1024) + "M")



# sendmail
HOST = "stmp.doubledna.cn"
SUBJECT = "Doubledna server system information"
TO = "1214663294@qq.com"
FROM = "gao@doubledna.cn"
'''
msg = MIMEText(
    """
    <table width="800" border="0" cellspacing="0" cellpadding="4">
      <tr>
          <td bgcolor="#CECFAD" height="20" style="font-size:14px">*

    """
)
'''
text = mem
text2 = cpu
text3 = root
text4 = shm

BODY = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text,text2,text3,text4
), "\r\n")

server = smtplib.SMTP()
server.connect("104.160.44.13","25")
server.login("gao@doubledna.cn", "ling1015")
server.sendmail(FROM, [TO], BODY)
server.quit()
