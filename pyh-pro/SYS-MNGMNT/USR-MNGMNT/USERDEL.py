#!/usr/bin/python3

import os

x=input("Enter the username to be deleted : ")
x=os.system("userdel -r " + x )

