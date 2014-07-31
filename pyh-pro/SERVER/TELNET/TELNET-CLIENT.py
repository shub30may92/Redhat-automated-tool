#!/usr/bin/python

import os

y=os.system("rpm -q telnet > /root/Desktop/trash.txt")
if y == 0 :
	print("Software is already installed")	
	#pass
else :
	os.system("yum install telnet > /root/Desktop/trash.txt")


os.system("rm /root/Desktop/trash.txt")

print("Enter the IP address os server : ")
x=raw_input()
os.system("telnet " + x)

#input("press enter to exit.....")

