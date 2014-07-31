#!/usr/bin/python

import os


y=os.system("rpm -q openssh-clients > /root/Desktop/trash.txt")
if y == 0 :
	print("Software is already installed")	
	#pass
else :
	os.system("yum install openssh-clients > /root/Desktop/trash.txt")

os.system("rm /root/Desktop/trash.txt")


print("Enter the ssh-server ip: ")
x=raw_input()

os.system('ssh ' + x )

#input('Enter to close...')


