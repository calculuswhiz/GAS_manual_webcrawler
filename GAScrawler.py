from os import system
from time import sleep
import random
# from re import search

carg = "'https://sourceware.org/binutils/docs/as/"
counter = 0
dirstruct = []

with open("Index.2.25.txt") as fp:
    for line in fp:
        if counter%2!=0:
            sysCall = "curl "+carg+line.strip()+"' > "+line.strip()[:line.strip().find("#")]
            print(sysCall)
            system(sysCall)
            sleep(random.uniform(.5,1.0))
        counter+=1
