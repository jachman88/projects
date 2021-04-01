#This is a python script that will scan for open ports on a host

#!/bin/python3

import socket
import sys

from datetime import datetime

#Target host defined
target = input("please enter in a target: ")
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]
else:
	print("Invalid amount of arguments.")

print(target)

#Banner
print('-' * 50)
print("Scanning: "+target)
print("Time Started: "+str(datetime.now))

try:
	for port in range(1,1023):
		#print(port)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print("Port {} is open".format(port))
			s.colse()
except KeyboardInterrupt:
	print("\nExiting Scan")
except soccket.error:
	print("Could not connect to server.")
	sys.exit()
