#!/usr/bin/python3

import os

user=input("Enter the username : ")

pid="ps aux | grep {}".format(user) + "\ | grep bash | awk '{print $2}'  >   /root/Desktop/trash.txt"
os.system(pid)

f=open("/root/Desktop/trash.txt" , 'r')
for i in f :
	os.system("kill -9 " + i)
f.close()
os.system("rm /root/Desktop/trash.txt")


