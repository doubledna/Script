import urllib2
import os
url="http://vip80.edb07.com/WFPWS_DataSource.asmx"
try:
    response=urllib2.urlopen(url)
except urllib2.URLError,e:
    if hasattr(e,"reason"):
        os.system('iisreset')
        print "Failed to reach the server"
        print "The reason:",e.reason
    elif hasattr(e,"code"):
        os.system('iisreset')
        print "The server couldn't fulfill the request"
        print "Error code:",e.code
        print "Return content:",e.read()
else:
    pass