'''
Author: xiangyu
Time:2016/12/5
Function:use to get the server ip
'''
import socket
from time import ctime

def URLtoIP():
    start = input("Start:")
    end = input("End:")
    machineroom = raw_input("machineroom:")
    Dm = raw_input("Dm:")
    print ctime()
    for i in range(start, end + 1):
       oneurl= "vip" + str(i) + "." + str(machineroom) + "." + str(Dm)
       url=str(oneurl.strip())
       # print url
       try:
           ip =socket.gethostbyname(url)
           # print ip
           iplist.writelines(url + "\t\t" + str(ip)+"\n")
       except:
           # print "There is no IP these domain names "
           iplist.writelines(url + "\t\t" + " No IP " + "\n")
try:
    iplist=open("iplist.txt","w")
    URLtoIP()
    iplist.close()
    print "complete !"
except:
    print "ERROR !"

print ctime()







	


