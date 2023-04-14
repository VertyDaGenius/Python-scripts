# this is a test script 
# so dont take it srsly 

import time
import os

while True:
    os.system('cls')
    age = int(input('how old are you?'))
    if age >= 18:
        print('you are at the legal age in america to vote!')
    else:
        print('you cannot vote')
    time.sleep(3)
