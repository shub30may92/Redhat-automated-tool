#!/usr/bin/python

import os 

y=os.system("rpm -q openssh-server > /root/Desktop/trash.txt")
if y == 0 :
	print("Software is already installed")	
	#pass
else :
	os.system("yum install openssh-server > /root/Desktop/trash.txt")


x=os.system("service sshd restart > /root/Desktop/trash.txt")

os.system("rm /root/Desktop/trash.txt")

if x == 0 :
	print("YOUR SERVER HAS STARTED")
#input("Press enter to close.....")
