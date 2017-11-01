#!/usr/bin/expect
spawn ssh 192.16.1.52
expect "jbs1-ewapp02:" {send "ls -lc /home/comm/data/gd_sefiles/ | tail -n1 | cut -d ' ' -f 10\r"}
expect "jbs1-ewapp02:" {send "exit\r"}
interact

