#!/usr/local/bin/python
import os
import win32com.client
import time


def CheckProcExistByPN(process_name):
    try:
        WMI = win32com.client.GetObject('winmgmts:')
        processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    except Exception, e:
        print process_name + "error : ", e;
    if len(processCodeCov) > 0:
        print process_name + " exist";
        return 1
    else:
        os.system('sc start  WFPRemotingServer')
        ##print process_name + " is not exist";
        file = open('log.txt', 'a')
        timenow = time.localtime()
        datenow = time.strftime('%Y-%m-%d %H:%M:%S', timenow)
        errlog = process_name + " is not exist" + datenow
        file.write(errlog + '\n')
        file.close()
        return 0


if __name__ == '__main__':
    CheckProcExistByPN('WFPOSService.exe')