import os
##os.system('iisreset')
os.system('taskkill /f /im WFPOSService.exe')
os.system('sc start  WFPRemotingServer')
