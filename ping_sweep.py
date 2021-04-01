#This is a Ping Sweep tool to identify live hosts on a network

#!/bin/python3

import os
import sys

#Banner
print('-' * 50)
print("Welcome to the Ping Sweep tool. \n"
	"This script will identify live hosts on a network\n")
print('-' * 50)

network_range = input("Please enter a network range: ")

print("scanning: {}".format(network_range))

try:
	for x in range(255):
		network = network_range[:-4]
		network = network + x.__str__()
		os.system("ping -c 1 {} | grep '64 bytes' | cut -d ' ' -f 4 | tr -d ':'".format(network))
		#print("{} is up.".format(network))
				
except KeyboardInterrupt:
	print("\nAborting Scan")
	
