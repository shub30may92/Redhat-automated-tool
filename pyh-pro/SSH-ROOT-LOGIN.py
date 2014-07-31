#!/usr/bin/python

import os
import sys

os.system("cat /etc/ssh/sshd_config | grep \#PermitRootLogin\ yes > /root/Desktop/trash.txt")
i=1
f=open("/root/Desktop/trash.txt")
for i in f :
	pass
if i == 1 :
	x=raw_input("root login is diabled on ssh, Do you want to enable it ?(y/n)")
	if x == 'y' :
		os.system("sed -i -e 's/PermitRootLogin no/#PermitRootLogin yes/g' /etc/ssh/sshd_config")
	elif x == 'Y' :
		os.system("sed -i -e 's/PermitRootLogin no/#PermitRootLogin yes/g' /etc/ssh/sshd_config")
	else :
		os.system("rm /root/Desktop/trash.txt")
		sys.exit()
else :
	x=raw_input("root login is enabled on ssh, Do you want to enable it ?(y/n)")
	if x == 'y' :
		os.system("sed -i -e 's/#PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config")
	elif x == 'Y' :
		os.system("sed -i -e 's/#PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config")
	else :
		os.system("rm /root/Desktop/trash.txt")
		sys.exit()
	
os.system("rm /root/Desktop/trash.txt")
os.system("service sshd restart")
raw_input("Enter to close....")
