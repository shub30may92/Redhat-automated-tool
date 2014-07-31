#!/usr/bin/python

import os 

y=os.system("rpm -q vsftpd > /root/Desktop/trash.txt")
if y == 0 :
	print("Software is already installed")	
	#pass
else :
	os.system("yum install vsftpd > /root/Desktop/trash.txt")


os.system("service vsftpd restart > /root/Desktop/trash.txt")

os.system("rm /root/Desktop/trash.txt")

print("YOUR SERVER HAS STARTED")
#input("Press enter to close.....")
