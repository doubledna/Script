#!/bin/bash
# coding=utf8
# startup script for the zabbix_server
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

PROC_NAME="zabbix_server"
start() {
     /etc/init.d/zabbix_server > /dev/null 2>&1

}

stop() {
    echo -n $"Stopping ${PROC_NAME} service:"
    ps aux | grep -E 'zabbix_server' | grep -v grep | awk '{print $2}' | head -n1 | xargs kill -9 &> /dev/null

}

status() {
    ps aux | grep -E 'zabbix_server' | grep -v 'grep' &> /dev/null
    if [ $? == '0' ];then
        echo  "zabbix_server is running..."
    else
        echo  "zabbix_server is stopping..."
    fi
}

restart() {
    stop
    start
}

case "$1" in
    start)
        start
	;;
    stop)
        stop
	;;
    restart)
        restart
	;;
    status)
        status
	;;
    *)
        echo $"Usage: $0 {start|stop|restart|status}"
	exit 2
esac
