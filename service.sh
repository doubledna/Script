#!/bin/bash
# coding=utf8
# startup script for the CollectServ
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

PROC_NAME="CollectServ"
start() {
    python CollectServ.py & > /dev/null 2>&1

}

stop() {
    echo -n $"Stopping ${PROC_NAME} service:"
    ps aux | grep -E 'CollectServ.py' | grep -v grep | awk '{print $2}' | xargs kill -9 &> /dev/null

}

status() {
    ps aux | grep -E 'CollectServ.py' | grep -v 'grep' &> /dev/null
    if [ $? == '0' ];then
        echo  "agent_server is running..."
    else
        echo  "agent_server is stopping..."
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
