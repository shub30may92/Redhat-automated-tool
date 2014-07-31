#!/usr/bin/python3

import os

x=input("Enter the Server IP address : ")
y=input("Enter the shared folder : ")
z=input("Enter the mount point : ")
os.system("mount " + x + ":" + y + " " + z)

