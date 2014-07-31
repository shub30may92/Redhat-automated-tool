#!/usr/bin/python3

import os

y=input("Enter the Folder to be shared : ")
x=input("Enter cliet's IP address : ")
cmd='echo {} {} >> /etc/exports'.format( y, x )
os.system(cmd)
os.system("service nfs restart")
input("Enter to close.......")
