# import the time module 
import os
import time 


os.system('say ready') 
time.sleep(2) 
os.system('say set') 
time.sleep(2) 

os.system('say start') 
now = time.time()

difference = 0
while difference <= 149 : 

    later = time.time()
    difference = int(later - now)
    print(difference, end="\r") 

    if(difference % 10 == 0 and difference != 0 and difference < 140):
        os.system('say ' + str(difference)) 

    if(difference >= 140):
        os.system('say ' + str(10 - (difference - 140))) 

    time.sleep(1) 

os.system('say stop') 


while difference < 200 : 
    later = time.time()
    difference = int(later - now)
    print(difference, end="\r") 

    if(difference % 3 == 0):
        os.system('say ' + str(difference)) 

    time.sleep(1) 

