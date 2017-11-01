#!/usr/bin/python
# coding=utf-8
import os
import time
import linecache

os.system('/home/d5000/jibei/var/QS/GetQS.sh > /home/d5000/jibei/var/QS/file.txt')
p = os.popen('grep "¹úµ÷_*" /home/d5000/jibei/var/QS/file.txt')
file = p.readline().strip()
os.environ['file'] = str(file)
os.system('scp jbs1-ewapp02:/home/comm/data/gd_sefiles/$file /home/d5000/jibei/var/QS;tar -zcf /home/d5000/jibei/var/QS/$file.tgz -C /home/d5000/jibei/var/QS/ $file')
p.close()


