#!/usr/bin/python3

import os

x=input("Enter the Telnet service enable time : ")
print(x)
os.system("sed -i -e 's/\tenabled\t=/\tenabled\t=\ "+ x + "\ /g' /etc/xinetd.conf")
#os.system("sed -i -e 's/#\tenabled/\tenabled/g' /etc/xinetd.conf")
input("enter to cont.........")
