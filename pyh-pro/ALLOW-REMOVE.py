#!/usr/bin/python3

import os

y=input("Enter the ip address you want to remove from allow list: ")
os.system("cat /etc/xinetd.conf | grep only_from | grep "+ y + " > /root/Desktop/trash.txt")
f=open("/root/Desktop/trash.txt", 'r')
i=1
k=1
for i in f :
	pass
if i == 1 : 
	print("IP Address not found")
else :
	os.system("sed -i -e 's/"+ y + "//g' /etc/xinetd.conf")
	print("Done")
os.system("service xinetd restart")
os.system("rm /root/Desktop/trash.txt")
input("Enter to cont....")
		
