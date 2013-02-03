#!/usr/bin/python

from time import sleep

filename = "leader.html"
cpt = 0

def increment():
    global cpt
    myfile = open(filename, 'w')
    myfile.write("%d" % (cpt))

    cpt += 1
    myfile.close()


while True:
    increment()
    sleep(1)
