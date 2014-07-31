#!/usr/bin/python3

import os
import sys

os.system('dialog --infobox  "welcome to my tool" 10  30')

os.system('sleep 2')

os.system('dialog --passwordbox "enter ur pass to access"  10 40  2> /tmp/pass ') 

apass="lw"

f=open('/tmp/pass')
passin=f.read(100)


if apass == passin :
	os.system('dialog --msgbox "Successful login. press ok to cont.."  10  50')
	os.system('dialog --menu  "Cloud Setup" 20 40 5  "1" "Create file"   "2" "Crate User" "3" "Conf NFS Server" "4" "logout user" "5" "cloud setup"  "6" "server security" "7" "misc" 2> /tmp/choice')

	fhch=open('/tmp/choice')
	choice=fhch.read(10)

	if choice == "1" :
		print(1)
	elif choice == "2" :
		print(2)
	elif choice == "3" :
		os.system('./nfs.py')
	else:
		print("not available")


else:
	ch=os.system('dialog --yesno "Do you want to logout"  10  40')
	if ch == 0 :
		sys.exit(1)
	else:
		pass
		



input()



