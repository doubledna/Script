# coding:utf-8
# usage: python scanport.py -H host -P port1,port2,port3
import optparse
import socket
from socket import *


# 扫描可连接主机
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')   # 发送测试信息
        results = connSkt.recv(100)
        print '[+]%d/tcp open' % tgtPort
        connSkt.close()
    except:
        print '[-]%d/tcp closed' % tgtPort


# 扫描打开的端口
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host" % tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIP
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, int(tgtPort))


# 获取主机名和端口
def main():
    parser = optparse.OptionParser("usage%prog " + "-H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-P', dest='tgtPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print '[-] You must specify a target host and port[s]. '
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()






