#! /usr/bin/python
# -*- coding: utf-8 -*-

import paramiko,datetime,os,sys,fileinput
# path = os.path.abspath('.')

if __name__=='__main__':
    # reading server_list
    serverlist = open("server_list.txt","r")

    for line in serverlist:
        #
        ip = line.split()[0]
        username = line.split()[1]
        password = line.split()[2]
        port = 22

        filelist = open("file_list.txt","r")

        # localpath
        # l_dir = './download/'
        path = os.path.abspath('.')
        l_dir = '/ssh/download/'            # question:can not change Home directory name
        os.chdir(l_dir)

        if os.path.exists(ip) != True:
            os.mkdir(ip)
        l_dir = os.path.join(l_dir,ip)

        print('   Server : '+ ip)
        #connect
        t = paramiko.Transport((ip, int(port)))
        t.connect(username=username,password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        #
        for r_file in filelist:
            r_file = r_file.strip('\n')
            l_file = os.path.join(l_dir,os.path.basename(r_file))
            print('    '+r_file+' ---> '+l_file)

            sftp.get(r_file,l_file)
        t.close()

    serverlist.close()
    filelist.close()