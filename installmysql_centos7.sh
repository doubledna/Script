#!/bin/bash
# centos7 install mysql5.5
# method: ./installmysql_centos7.sh mysql-5.5.tar.gz

#修改数据库安装位置和数据位置
BASEDIR=/usr/local/mysql
DATADIR=/data/mysql

#yum install vim libaio net-tools

#创建mysql组与用户
var1=`grep mysql /etc/group`
var2=`grep mysql /etc/passwd`
if [ -z $var1 ] && [ -z $var2 ]
then
    groupadd mysql
    useradd -r -g mysql mysql
fi

#解压安装包
tar -zxf $1
file=$1
file1=${file%.*}
file2=${file1%.*}
echo $file2
echo ${file2}
#file3=/usr/local/mysql
rm -rf $file2/data/
cp -rf $file2 /usr/local/
rm -rf $file2
ln -s /usr/local/${file2} /usr/local/mysql
cp $BASEDIR/support-files/my-medium.cnf /etc/my.cnf
mkdir ${DATADIR} -p
chown mysql.mysql ${DATADIR}

cd $BASEDIR
chown -R mysql .
chgrp -R mysql .
./scripts/mysql_install_db --user=mysql --basedir=${BASEDIR} --datadir=${DATADIR}
cp $BASEDIR/support-files/mysql.server /etc/init.d/mysqld

#修改启动脚本：
sed -i '46c basedir=/usr/local/mysql' /etc/init.d/mysqld
sed -i '47c datadir=/data/mysql' /etc/init.d/mysqld
chkconfig --add /etc/init.d/mysqld
sed -i '$a PATH=$PATH:/usr/local/mysql/bin' /etc/profile
sed -i '$a export PATH' /etc/profile
source /etc/profile
service mysqld start

#初始化密码
#mysqladmin -u root password 'mmp'







