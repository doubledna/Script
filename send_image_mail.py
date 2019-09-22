# -*- coding:utf8 -*-
#!/usr/local/bin/python
#creater: doubledna
#creatertime: 2017/07/12

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

HOST = "smtp.doubledna.cn"
SUBJECT = u"流量监控"
TO = "1214663294@qq.com"
FROM = "gao@doubledna.cn"

def addimg(src,imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage

msg = MIMEMultipart('related')

msgtext = MIMEText("""
<table width="600" border="0" cellspacing="0" cellpadding="4">
  <tr bgcolor="#CECFAD" heigth="20" style="font-size:14px">
    <td colspan=2> * data <a href=""> more</a></td>
  </tr>
  <tr bgcolor="EFEBDE" height="100" style="font-size:13px">
    <td>
      <img src="cid:Flow"></td>
  </tr>
</table>""","html","utf-8")

msg.attach(msgtext)
msg.attach(addimg("/root/service/Netraffic/Flow.png", "Flow"))

msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
try:
    server = smtplib.SMTP()
    server.connect("104.160.44.13","25")
    server.starttls()
    server.login("gao@doubledna.cn","ling1015")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print "send mail success!"
except Exception, e:
    print "defeate:" + str(e)
