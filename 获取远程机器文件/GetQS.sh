#!/usr/bin/expect
spawn ssh 192.xxx.xxx.xxx
expect "xxx:" {send "ls -lc /home/xxx/xxx/xxx/ | tail -n1 | cut -d ' ' -f 10\r"}
expect "xxx:" {send "exit\r"}
interact

