#!/usr/bin/python3
import os
import sys

while True:
	os.system('clear')

	os.system('tput setaf 1')
	print("\n\t\tCLIENT SIDE\n")

	os.system('tput setaf 0')	
	print("Press 1 : WORK AS SAMBA CLIENT")

	os.system('tput setaf 1')
	print("\n\t\tSERVER SIDE\n")
	
	os.system('tput setaf 0')
	print("Press 2 : CREATE YOUR OWN SAMBA SERVER")
	print("Press 3 : CHECK SERVER STATUS")
	#print("Press 5 : REMOVE IP")		
	#print("Press 5 : ENABLE/DISABLE PUBLIC LOGIN")
	print("Press 4 : ADD FOLDERS FOR SHARING")
	print("Press 5 : ADD USER")	
	print("Press 6 : Go back")
	print ("\n\n")

	ch=int(input("Enter ur choice: "));

	if ch == 1 :
		x=input("Enter the ip address : ")
		y=input("Enter the sharename : ")
		os.system("smbclient //"+x+"/"+y)
	elif ch == 2 :
		os.system("yum install samba > trash")
		os.system("yum install samba-common > trash")
		os.system("service smb restart")
		os.system("chkconfig smb on")
		os.system("setenforce 0")
		os.system("iptables -F")
		input("Enter to close....")
		
	elif ch == 3 :
		os.system("service smb status")
		input("Enter to continue......")
	
	elif ch == 4 :
		os.system("python3 SAMBA-FOLDER-ADD.py")
	elif ch == 5 :
		os.system("python3 SAMBA-USER-ADD.py")	
	
	elif ch == 6 :
		sys.exit()		
	else:
		print("option not supported")
input("enter to close")
