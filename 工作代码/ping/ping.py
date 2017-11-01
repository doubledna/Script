import os
import socket

start = input("Start:")
end = input("End:")
machineroom = raw_input("machineroom:")
Dm = raw_input("Dm:")
for i in range(start,end + 1):
    Domain = "vip" + str(i) + "." + str(machineroom) + "." + str(Dm)
    print Domain


