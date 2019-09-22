#!/usr/local/bin/python
# coding=utf-8
# func:

import MySQLdb


class inputdata:

    def __init__(self):
        pass

    def con(self):
        conn = MySQLdb.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='',
            db='test',
        )
        return conn

    def inputmem(self):
        cur = self.con().cursor()
        cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
        cur.close()
        self.con().commit()
        self.con().close()
        
inputdata().inputmem()
