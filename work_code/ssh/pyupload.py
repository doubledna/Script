#! /usr/bin/python
# -*- coding:utf-8 -*-
import paramiko,datetime,os,sys,fileinput

if __name__=='__main__':
    #reading server_list
    serverlist = open("server_list.txt","r")

    for line in serverlist:
        ip = line.split()[0]
        username = line.split()[1]
        password = line.split()[2]

        port = 22
        #localpath
        l_dir = '/ssh/upload/'
        #telnetpath
        r_dir='/tmp/'

        #printsplit
        print ('   Server : '+ ip)

        #start connect
        t = paramiko.Transport((ip,int(port)))
        t.connect(username=username,password=password,)
        sftp = paramiko.SFTPClient.from_transport(t)

        #differ uploading
        files = os.listdir(l_dir)
        for f in files:

            l_file = os.path.join(l_dir,f)

            r_file = os.path.join(r_dir,f)
            print('   '+l_file+' ---> '+r_file)

            sftp.put(l_file,r_file)
        t.close()
    serverlist.close()
