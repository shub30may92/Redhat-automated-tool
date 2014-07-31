#!/usr/bin/python

import os

x=raw_input("Enter the username : ")
os.system("passwd -d " + x)
raw_input("enter to close....")
