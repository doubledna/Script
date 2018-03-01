#!/bin/bash
# coding=utf8
#func:
HOST='192.168.1.2'
USER='aaa'
PASSWD='bbb'

backup(){
    date=`date +"%F"`
    file="mylog_$date.tgz"
    tar -zcvf mylog_$date.tgz /var/mylog/*
    ftp -vn $HOST <<EOF
    user USER PASSWD
    binary
    cd /var/mylog/
    lcd /var/mylog/
    prompt
    put $file
    bye
    EOF
}

time=`date +"%H:%M:%S"`
settime='05:00:00'
if [ $time = $settime ]
then
    backup
    echo "Start backup"
fi
