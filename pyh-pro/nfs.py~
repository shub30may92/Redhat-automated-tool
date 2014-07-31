#!/usr/bin/python3

import os

os.system("rm /tmp/ip")
os.system("rm /tmp/share")
os.system('dialog --msgbox "welocme to nfs server" 10 30')
os.system('sleep 2')
os.system('yum install nfs-utils -y')

os.system('dialog --inputbox "enter folder to share" 10 30 2> /tmp/share' )
fsh=open('/tmp/share')
fname=fsh.read(50)

os.system('dialog --inputbox "Enter ip address" 10 40 2> /tmp/ip')

fip=open('/tmp/ip')
fipname=fip.read(50)

ch=os.system('dialog --yesno "Do you want give write access to this IP?" 10 40')
if ch == 0 :	
	cmd="echo {} {}\(rw\) >> /etc/exports".format(fname, fipname)
	os.system(cmd)
	os.system("chmod o+w " + fname)
else :
	cmd="echo {} {} >> /etc/exports".format(fname, fipname)
	os.system(cmd)
os.system("rm /tmp/ip")
os.system("rm /tmp/share")
os.system("service nfs restart")

os.system('dialog --msgbox "nfs ready" 10 20')
