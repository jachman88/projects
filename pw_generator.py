#Password Generator

import random
import string

pw_length = int(raw_input("Length of password: "))
run_again =""
#method that generates the password pool
def pool_gen (pw_length):
   chars=string.ascii_lowercase + string.ascii_uppercase
   pwPool = chars + string.digits + string.punctuation
   return pwPool

#method that selects characters from the pool and builds the password
def pw_build ():
    counter = 0
    new_pw = ""
    while counter < pw_length:
        pw_pool = pool_gen(pw_length)
        position = random.randrange(len(pw_pool))
        value = pw_pool[position]
        new_pw = new_pw + value.__str__()
        counter +=1
    print (new_pw)
    return new_pw

pw_build()

raw_input('\n\nPress any key to exit')