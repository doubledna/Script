#!/usr/bin/env python
# -*-coding = utf-8 -*-

import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='****',db='test')

cursor = conn.cursor()
effect_row = cursor.execute("update cheng set age=21 where name='sha'")
effect_row = cursor.executemany("insert into cheng (id,name) values (%s,%s)",[(3,"doubledna"),(4,"cheng")])

new_id = cursor.lastrowid
cursor.execute("select * from cheng")
row_1 = cursor.fetchone()
row_2 = cursor.fetchmany(3)
row_3 = cursor.fetchall()

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
conn.commit()
cursor.close()
conn.close()
