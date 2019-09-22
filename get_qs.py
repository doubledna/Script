#!/usr/bin/python
# coding=utf-8
import os
import time
import linecache

os.system('/home/xxx/xxx//xxx/xxx.sh > /home/xxx/xxx/xxx/xx/file.txt')
p = os.popen('grep "xxx_*" /home/xxx/xxx/xxx/xxx/file.txt')
file = p.readline().strip()
os.environ['file'] = str(file)
os.system('scp xxx:/home/comm/data/xxx/$file /home/xxx/xxx/xxx/xxx;tar -zcf /home/d5000/xxx/xxx/xxx/$file.tgz -C /home/xxx/xxx/xxx/xxx/ $file')
p.close()


