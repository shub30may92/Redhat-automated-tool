#!/usr/bin/python

import os

y=os.system("rpm -q xinetd > /root/Desktop/trash.txt")
if y == 0 :
	print("Software is already installed")	
	#pass
else :
	os.system("yum install xinetd > /root/Desktop/trash.txt")

os.system("service xinetd restart > /root/Desktop/trash.txt")

os.system("rm /root/Desktop/trash.txt")

print("YOUR SERVER HAS STARTED")
input("Press enter to close.....")
