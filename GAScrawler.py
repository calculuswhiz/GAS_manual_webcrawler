from os import system
from time import sleep
import random
# from re import search

carg = "'https://sourceware.org/binutils/docs/as/"
counter = 0
dirstruct = []

with open("Index.txt") as fp:
    for line in fp:
        if counter%2!=0:
            sysCall = "curl "+carg+line.strip()+"' > "+line.strip()[:line.strip().find("#")]
            print(sysCall)
            system(sysCall)
            sleep(random.uniform(1.1,2.5))
        counter+=1
