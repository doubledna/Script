#! /usr/bin/python
# -*- coding:utf-8 -*-
import paramiko
import fileinput

if __name__=='__main__':

    #  reading the server_list.txt
    serverlist = open("server_list.txt","r")

    for line in serverlist:
        # get ip,username,password
        ip = line.split()[0]
        username = line.split()[1]
        password = line.split()[2]

        #start connect
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname = ip,username = username ,password = password)

        # print split
        print('   Server : ' + ip)

        #reading cmd
        cmdlist = open("cmd_list.txt","r")

        #exec
        for line in cmdlist:
            print('        ' + line)
            stdin, stdout, stderr = s.exec_command(line)
            print stdout.read()

        #close line
        s.close()
    serverlist.close()







