#!/usr/bin/env python
# -*- coding: gbk -*-
import socket,time
while 1:
    file_obj = open('C:\\test8080\\list-5.txt')
    for line in file_obj:
        try:
            sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            ip = line.split()[0]
            port = int(line.split()[1])
            address = line.split()[2]
            print ip,port,address
            #设置超时时间（0.0）
            sc.settimeout(2)
            sc.connect((ip,port))
            timenow=time.localtime()
            datenow = time.strftime('%Y-%m-%d %H:%M:%S', timenow)
            logstr="%s:%s 连接成功->%s \n" %(ip,port,datenow)
            print logstr
            sc.close()
        except:
            file = open("log.txt", "a")
            timenow=time.localtime()
            datenow = time.strftime('%Y-%m-%d %H:%M:%S', timenow)
            logstr="%s:%s 连接失败->%s \n" %(ip,port,datenow)
            print logstr
            file.write(logstr)
            file.close()
    print "sleep 10....."
    time.sleep(10)