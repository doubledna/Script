#!/usr/bin/python
# coding=utf-8
#
import dpkt
import socket
import pygeoip
import optparse


gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')


# 分析IP的实际物理地址
def retGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city != '':
            geoLoc = city + ', ' + country
        else:
            geoLoc = country
    except Exception, e:
        return 'Unregistered'


# 分析数据包
def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print '[+] Src: ' + src + '--> Dst: ' + dst
            print '[+] Src: ' + retGeoStr(src) + '--> Dst: ' + retGeoStr(dst)
        except:
            pass


if __name__ == '__main__':
    parser = optparse.OptionParser('usage%prog -p <pcap file>')
    parser.add_option('-p', dest='pcapFile', type='string', help='specify pcap filename')
    (options, args) = parser.parse_args()
    if options.pcapFile == None:
        print parser.usage
        exit(0)
    pcapFile = options.pcapFile
    f = open(pcapFile)
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)

