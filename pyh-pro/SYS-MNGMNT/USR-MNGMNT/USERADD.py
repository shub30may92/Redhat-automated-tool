#!/usr/bin/python3

import os

x=input("Enter the username to be added : ")
x=os.system("useradd " + x + " > /root/Desktop/trash.txt")
os.system("rm /root/Desktop/trash.txt")


