#!/bin/bash
# coding=utf8
# startup script for the zabbix_agent
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

PROC_NAME="zabbix_agent"
start() {
    /etc/init.d/zabbix_agentd > /dev/null 2>&1

}

stop() {
    echo -n $"Stopping ${PROC_NAME} service:"
    ps aux | grep -E 'zabbix_agentd' | grep -v grep | awk '{print $2}' | head -n1 | xargs kill -9 &> /dev/null

}

status() {
    ps aux | grep -E 'zabbix_agentd' | grep -v 'grep' &> /dev/null
    if [ $? == '0' ];then
        echo  "zabbix_agent is running..."
    else
        echo  "zabbix_agent is stopping..."
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
