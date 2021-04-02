#This is a simple password generator

#! /bin/python3

import random
import string
import sys

pw_length = int(input("Length of password: "))
run_again= ""

#Function/Method that creates the pool of characters for the password

def pool_gen(pw_length):
	chars=string.ascii_lowercase + string.ascii_uppercase
	pwPool = chars + string.digits + string.punctuation
	return pwPool

#Function that selects the characters from the pool and builds the password
def pw_build():
	counter = 0
	new_pw = ""
	while counter < pw_length:
		pw_pool = pool_gen(pw_length)
		position = random.randrange(len(pw_pool))
		value = pw_pool[position]
		new_pw = new_pw + value.__str__()
		counter +=1
	print(new_pw)
	return new_pw

try:
	pw_build()	

except KeyboardInterrupt:
	print("\nTerminating Password Generator")
