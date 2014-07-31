#!/usr/bin/python3

import os


y=os.system("rpm -q ftp > /root/Desktop/trash.txt")
if y == 0 :
	print("Software is already installed")	
	#pass
else :
	os.system("yum install ftp > /root/Desktop/trash.txt")

os.system("rm /root/Desktop/trash.txt")


print("Enter the ftp-server ip: ")
x=input()

os.system('ftp ' + x )

#input('Enter to close...')


