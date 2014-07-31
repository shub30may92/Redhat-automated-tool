#!/usr/bin/python3

import os 

y=os.system("rpm -q vsftpd > /root/Desktop/trash.txt")
if y == 0 :
	print("Software is already installed")	
	#pass
else :
	os.system("yum install vsftpd > /root/Desktop/trash.txt")


os.system("service vsftpd restart > /root/Desktop/trash.txt")
os.system("setenforce 0")
os.system("iptables -F")

os.system("rm /root/Desktop/trash.txt")

print("YOUR SERVER HAS STARTED")
#input("Press enter to close.....")
