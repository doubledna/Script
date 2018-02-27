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
from conffile import HOSTNAME, USERNAME, PASSWORD, PORT

'''获取主机各类信息'''
def memory():
    M = {}
    M['hostname'] = socket.gethostbyname(socket.gethostname())
    Mem = psutil.virtual_memory()
    FreeMem = int(Mem.free/1024/1024)
    UsedMem = int(Mem.used/1024/1024)
    M['free'] = FreeMem
    M['used'] = UsedMem
    return M


def cpu():
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
                progress1 = 'systemctl status ' + ProgressName + '.service'
                state = str(os.popen(progress1).read())
                if re.search(r'running', state, re.M) is not None:
                    P['status'] = re.search(r'running', state, re.M).group()
                else:
                    P['status'] = re.search(r'running', state, re.M)
            yield P


def formatprocess():
    Q = {}
    Q['hostname'] = socket.gethostbyname(socket.gethostname())
    Q['status'] = [x['status'] for x in process()]  # 将迭代的status放入到一个数组里
    Q['process'] = [x['name'] for x in process()]
    return Q


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
    with open(file_name, 'w') as f:
        f.write(str(memory()))


def outcpu():
    file_name = socket.gethostbyname(socket.gethostname()) + '_cpu.txt'
    with open(file_name, 'w') as f:
        f.write(str(cpu()))


def outdisk():
    file_name = socket.gethostbyname(socket.gethostname()) + '_disk.txt'
    with open(file_name, 'w') as f:
        f.write(str(formatdisk()))


def outuser():
    file_name = socket.gethostbyname(socket.gethostname()) + '_user.txt'
    with open(file_name, 'w') as f:
        f.write(str(user()))


def outprogress():
    file_name = socket.gethostbyname(socket.gethostname()) + '_progress.txt'
    with open(file_name, 'w') as f:
        f.write(str(formatprocess()))


''' 将数据发到指定主机'''
def Sendmemory():
    filename = socket.gethostbyname(socket.gethostname()) + '_memory.txt'
    hostname = HOSTNAME
    username = USERNAME
    password = PASSWORD
    port = PORT
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(os.path.join(os.path.abspath('.'), '%s' % filename), os.path.join(os.path.abspath('.'), 'memorydata/%s' % filename))
    t.close()

def Sendcpu():
    filename = socket.gethostbyname(socket.gethostname()) + '_cpu.txt'
    hostname = HOSTNAME
    username = USERNAME
    password = PASSWORD
    port = PORT
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(os.path.join(os.path.abspath('.'), '%s' % filename), os.path.join(os.path.abspath('.'), 'cpudata/%s' % filename))
    t.close()

def Senddisk():
    filename = socket.gethostbyname(socket.gethostname()) + '_disk.txt'
    hostname = HOSTNAME
    username = USERNAME
    password = PASSWORD
    port = PORT
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(os.path.join(os.path.abspath('.'), '%s' % filename), os.path.join(os.path.abspath('.'), 'diskdata/%s' % filename))
    t.close()


def Senduser():
    filename = socket.gethostbyname(socket.gethostname()) + '_user.txt'
    hostname = HOSTNAME
    username = USERNAME
    password = PASSWORD
    port = PORT
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(os.path.join(os.path.abspath('.'), '%s' % filename), os.path.join(os.path.abspath('.'), 'userdata/%s' % filename))
    t.close()


def Sendprogress():
    filename = socket.gethostbyname(socket.gethostname()) + '_progress.txt'
    hostname = HOSTNAME
    username = USERNAME
    password = PASSWORD
    port = PORT
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(os.path.join(os.path.abspath('.'), '%s' % filename), os.path.join(os.path.abspath('.'), 'progressdata/%s' % filename))
    t.close()

"""
'''修改版发送数据'''
class SendData:

    def __init__(self):
        self.hostname = '192.168.229.129'
        self.username = 'root'
        self.password = 'ling1015'
        self.port = 22

    def Sendmemory(self):
        filename = socket.gethostbyname(socket.gethostname()) + '_memory.txt'
        hostname = self.hostname
        username = self.username
        password = self.password
        port = self.port
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(os.path.join(os.path.abspath('.'), '%s' % filename),
                 os.path.join(os.path.abspath('.'), 'memorydata/%s' % filename))
        t.close()

    def Sendcpu(self):
        filename = socket.gethostbyname(socket.gethostname()) + '_cpu.txt'
        hostname = self.hostname
        username = self.username
        password = self.password
        port = self.port
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(os.path.join(os.path.abspath('.'), '%s' % filename),
                 os.path.join(os.path.abspath('.'), 'cpudata/%s' % filename))
        t.close()

    def Senddisk(self):
        filename = socket.gethostbyname(socket.gethostname()) + '_disk.txt'
        hostname = self.hostname
        username = self.username
        password = self.password
        port = self.port
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(os.path.join(os.path.abspath('.'), '%s' % filename), os.path.join(os.path.abspath('.'), 'diskdata/%s' % filename))
        t.close()

    def Senduser(self):
        filename = socket.gethostbyname(socket.gethostname()) + '_user.txt'
        hostname = self.hostname
        username = self.username
        password = self.password
        port = self.port
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(os.path.join(os.path.abspath('.'), '%s' % filename), os.path.join(os.path.abspath('.'), 'userdata/%s' % filename))
        t.close()

    def Sendprogress(self):
        filename = socket.gethostbyname(socket.gethostname()) + '_progress.txt'
        hostname = self.hostname
        username = self.username
        password = self.password
        port = self.port
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(os.path.join(os.path.abspath('.'), '%s' % filename), os.path.join(os.path.abspath('.'), 'progressdata/%s' % filename))
        t.close()
"""

x = 1
while x <= 2:
    Timer(2, outmemory).start()
    Timer(2, outcpu).start()
    time.sleep(2)
    Timer(2, outdisk).start()
    Timer(2, outprogress).start()
    time.sleep(2)
    Timer(2, outuser).start()
    Timer(2, Sendcpu).start()
    time.sleep(2)
    Timer(2, Sendmemory).start()
    Timer(2, Senduser).start()
    time.sleep(2)
    Timer(2, Senddisk).start()
    Timer(2, Sendprogress).start()
    time.sleep(2)
