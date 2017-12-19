#!/usr/local/bin/python
# coding=utf-8
# func: 获取服务器信息并发到指定服务器指定目录中

import os
import psutil
import re
import json
import time
from threading import Timer
import socket
import sys
import paramiko


'''获取主机各类信息'''


def memory():  # 获取内存信息
    M = {}
    M['hostname'] = socket.gethostbyname(socket.gethostname())
    Mem = psutil.virtual_memory()
    FreeMem = int(Mem.free/1024/1024)
    UsedMem = int(Mem.used/1024/1024)
    M['free'] = FreeMem
    M['used'] = UsedMem
    return M


def cpu():  # 获取CPU使用率信息
    C = {}
    Cpu = psutil.cpu_percent(1)
    C['hostname'] = socket.gethostbyname(socket.gethostname())
    C['precent'] = Cpu
    return C


def user():
    P = {}
    N = []
    User = psutil.users()
    for suser in User:
        N.append(suser.name)
        # M.append({'name': suser.name})
    X = list(set(N))
    # M = [{'name': val} for val in X]
    M = [var for var in X]
    P['hostname'] = socket.gethostbyname(socket.gethostname())
    P['user'] = M
    return P


def process():
    with open('process.txt', 'r') as f:
        for i in f.readlines():
            O = {}
            P = {}
            ProgressName = i.strip('\r\n')
            P['name'] = ProgressName
            # 判断系统版本是CentOS6还是CentOS7
            System = str(os.popen('cat /etc/redhat-release').read())
            searchObj = re.search(r' 7.', System, re.M)
            if searchObj is None:
                progress = 'service ' + ProgressName + ' status'
                statid = str(os.popen(progress).read())
                Obj = re.search(r'running', statid, re.M)
                if Obj is not None:
                    P['status'] = Obj.group()
                else:
                    P['status'] = "stopping"
            else:
                progress1 = 'systemctl status ' + System + '.service'
                state = str(os.popen(progress1).read())
                if re.search(r'running', state, re.M) is not None:
                    P['status'] = re.search(r'running', state, re.M).group()
                else:
                    P['status'] = re.search(r'running', state, re.M)
            yield P


def formatprocess():
    Q = {}
    Q['hostname'] = socket.gethostbyname(socket.gethostname())
    Q['status'] = [x['status'] for x in process()]
    Q['process'] = [x['name'] for x in process()]
    return Q

# 获取剩余磁盘信息
def disk():
    E = {}
    Disk = psutil.disk_partitions()
    for i in Disk:
        F = {}
        # name = i.device  # 获取文件系统名称
        mountpoint = i.mountpoint  # 获取挂载点
        # total = psutil.disk_usage(i.mountpoint).total/1024/1024  # 总磁盘量
        free = psutil.disk_usage(i.mountpoint).free/1024/1024  # 已使用磁盘量
        # F.append(({'name': mountpoint},{'total': total},{'used': used}))
        F = {mountpoint: free}
        yield F


def formatdisk():
    G = {}
    G['hostname'] = socket.gethostbyname(socket.gethostname())
    for i in disk():
        G.update(i)
    return G


'''将获取的数据保存至文件'''
def outmemory():
    file_name = socket.gethostbyname(socket.gethostname()) + '_memory.txt'
    with open('memorydata/%s' % file_name, 'w') as f:
        f.write(str(memory()))


def outcpu():
    file_name = socket.gethostbyname(socket.gethostname()) + '_cpu.txt'
    with open('cpudata/%s' % file_name, 'w') as f:
        f.write(str(cpu()))


def outdisk():
    file_name = socket.gethostbyname(socket.gethostname()) + '_disk.txt'
    with open('diskdata/%s' % file_name, 'w') as f:
        f.write(str(formatdisk()))


def outuser():
    file_name = socket.gethostbyname(socket.gethostname()) + '_user.txt'
    with open('userdata/%s' % file_name, 'w') as f:
        f.write(str(user()))


def outprogress():
    file_name = socket.gethostbyname(socket.gethostname()) + '_progress.txt'
    with open('progressdata/%s' % file_name, 'w') as f:
        f.write(str(formatprocess()))


''' 整合接收的数据'''
def combmemory():
    # 遍历memorydata文件夹中文件
    path = os.path.join(os.path.abspath('.'), 'memorydata')
    filelist = os.listdir(path)
    file = open('json/memory.json', 'w')
    a = []
    for fr in filelist:
        for txt in open('memorydata/%s' % fr, 'r'):  # 用于读取memorydata中数据
            eval(txt)  # 将字符串转成字典
        # b = [eval(txt) for txt in open('data/%s' % fr, 'r')]
        a.append(eval(txt))
    g = {}
    g['hostname'] = [x['hostname'] for x in a]
    g['free'] = [x['free'] for x in a]
    g['used'] = [x['used'] for x in a]
    json.dump(g, file)
    file.close()


def combcpu():
    # 遍历cpudata文件夹中文件
    path = os.path.join(os.path.abspath('.'), 'cpudata')
    filelist = os.listdir(path)
    file = open('json/cpu.json', 'w')
    a = []
    for fr in filelist:
        for txt in open('cpudata/%s' % fr, 'r'):  # 用于读取cpudata中数据
            eval(txt)  # 将字符串转成字典
        # b = [eval(txt) for txt in open('data/%s' % fr, 'r')]
        a.append(eval(txt))
    g = {}
    g['hostname'] = [x['hostname'] for x in a]
    g['precent'] = [x['precent'] for x in a]
    json.dump(g, file)
    file.close()


def combdisk():
    # 遍历diskdata文件夹中文件
    path = os.path.join(os.path.abspath('.'), 'diskdata')
    filelist = os.listdir(path)
    file = open('json/disk.json', 'w')
    a = []
    for fr in filelist:
        for txt in open('diskdata/%s' % fr, 'r'):  # 用于读取diskdata中数据
            eval(txt)  # 将字符串转成字典
        b = eval(txt) # 用于将字典key取出
        a.append(eval(txt))
    g = {}
    for key in b.keys():  # 迭代字典的key
        g[key] = [x[key] for x in a]
    json.dump(g, file)
    file.close()


def combuser():
    # 遍历userdata文件夹中文件
    path = os.path.join(os.path.abspath('.'), 'userdata')
    filelist = os.listdir(path)
    file = open('json/user.json', 'w')
    a = []
    for fr in filelist:
        for txt in open('userdata/%s' % fr, 'r'):  # 用于读取userdata中数据
            eval(txt)  # 将字符串转成字典
        # b = eval(txt) # 用于将字典key取出
        a.append(eval(txt))
    json.dump(a, file)
    file.close()


def combprocess():
    # 遍历progressdata文件夹中文件
    path = os.path.join(os.path.abspath('.'), 'progressdata')
    filelist = os.listdir(path)
    file = open('json/process.json', 'w')
    a = []
    for fr in filelist:
        for txt in open('progressdata/%s' % fr, 'r'):  # 用于读取userdata中数据
            eval(txt)  # 将字符串转成字典
        # b = eval(txt) # 用于将字典key取出
        a.append(eval(txt))
    json.dump(a, file)
    file.close()

# 批量运行各类输出
x = 1
while x <= 2:
    Timer(2, outmemory).start()
    Timer(2, outcpu).start()
    time.sleep(2)
    Timer(2, outdisk).start()
    Timer(2, outprogress).start()
    time.sleep(2)
    Timer(2, outuser).start()
    Timer(2, combmemory).start()
    time.sleep(2)
    Timer(2, combcpu).start()
    Timer(2, combdisk).start()
    time.sleep(2)
    Timer(2, combuser).start()
    Timer(2, combprocess).start()
    time.sleep(2)
