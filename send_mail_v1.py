# coding=utf8

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
# sender是邮件发送人邮箱，passWord是服务器授权码，mail_host是服务器地址（这里是QQsmtp服务器）
sender = '1297010324@qq.com'
passWord = ''
mail_host = 'smtp.qq.com'
#receivers是邮件接收人，用列表保存，可以添加多个
receivers = ['1214663294@qq.com']

#设置email信息
msg = MIMEMultipart()
#邮件主题
msg['Subject'] = "test"
#发送方信息
msg['From'] = sender
#邮件正文是MIMEText:
msg_content = "test email"
msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))
#登录并发送邮件
try:
    #QQsmtp服务器的端口号为465或587
    s = smtplib.SMTP("smtp.qq.com", 587)
    s.starttls()
    s.set_debuglevel(1)
    s.login(sender,passWord)
    #给receivers列表中的联系人逐个发送邮件
    for i in range(len(receivers)):
        to = receivers[i]
        msg['To'] = to
        s.sendmail(sender,to,msg.as_string())
        print('Success!')
    s.quit()
    print ("All emails have been sent over!")
except smtplib.SMTPException as e:
    print ("Falied,%s",e)
