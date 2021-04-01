#!/bin/python3

import sys
import os

print("Welcome to the Ping Sweep tool. \n"
        "This script will identify live hosts on a network.\n")

network_range = input("Please enter a network range: ")
print(network_range)
print("scanning: {}".format(network_range))

def nix_sweeper():
    for x in range(255):
        print (x)
        network = network_range[:-4]
        network = network + x.__str__()
        os.system("ping -c 1 {} |grep '64 bytes' | cut -d ' ' -f 4 | tr -d ':'".format(network))
        #print(network)
    return

try:
	nix_sweeper()
	
except KeyboardInterrupt:
	print("\nAborting Scan")


