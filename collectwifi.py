# coding:utf-8
# 收集windows电脑WiFi信息脚本
from _winreg import *


# 将十六进制值转换成实际的MAC地址
def va12addr(val):
    addr = ''
    for ch in val:
        addr += '%02x ' % ord(ch)
    addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr


# 提取出各个被列出来的网络名称与MAC地址
def printNets():
    net = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print '\n[*] Networks You have Joined.'
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            (n, addr, t) = EnumKey(netKey, 5)
            (n, name, t) = EnumValue(netKey, 4)
            macAddr = va12addr(addr)
            netName = str(name)
            print '[+] ' + netName + ' ' + macAddr
            CloseKey(netKey)
        except:
            break

if __name__ == '__main__':
    printNets()