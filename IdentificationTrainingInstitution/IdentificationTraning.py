#!/usr/local/bin/python
# coding=utf-8

company = raw_input("请输入公司名称:")
f = open("a.txt", "r")
lines = f.readlines()
a = []
for line in lines:
    a.append(line[0:-1])
if company in a:
    print (company + "是个培训公司,小心被骗!")
else:
    print (company + "是个正常企业,祝面试成功!")
f.close()


