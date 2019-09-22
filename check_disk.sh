#/bin/sh
#this script is used to check the disk's use
#author
#file check_d.sh
#date 2017/4/1

#create log
TODAY=$(date "+%Y-%m-%d")
log_file=/home/xxx/task/log/log."$TODAY"
#errlog=/root/task/log/errlog."$TODAY"
exec 1>> $log_file
exec 2>> $log_file

result=$(df -Ph | grep /dev/sda5  | awk '{print $5}' | awk -F "%" '{if($1>=96){print $1}}')
mon=$(ls -lc /home/xxx/task/data | head -n 2 | tail -n 1 | awk '{print $9}')
data=$(ls -lc /home/xxx/task/data/* | head -n 3 | tail -n 1 | awk '{print $9}')
dict=/home/xxx/task/data/$mon/$data
dict2=/home/xxx/task/data/

if [ "$mon" != "" ]
then
    if [ "$result" = "" ]
    then
	echo '磁盘用量安全'
    else
	rm -rf $dict
        echo '已删'$dict
    fi
else
    echo '不可删'$dict2
fi

