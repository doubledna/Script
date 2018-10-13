import socket
from time import ctime

start = input("Start:")
end = input("End:")
machineroom = raw_input("machineroom:")
Dm = raw_input("Dm:")
print ctime()
for i in range(start, end + 1):
    oneurl= "vip" + str(i) + "." + str(machineroom) + "." + str(Dm)
    url = str(oneurl.strip())
    print  url

print ctime()