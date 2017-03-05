#-*- coding:utf8 -*-
company = raw_input("Please enter the company name:")
f = open("a.txt","r")
lines = f.readlines()
a = []
for line in lines:
    a.append(line[0:-1])
if company in a:
    print (company + ' ' + "is a training institution,fuck!")
else:
    print (company +  ' ' + "is a serious company,A good interview!")
f.close()


