#!/usr/bin/python3
import os
import sys

while True:
	os.system('clear')

	os.system('tput setaf 1')
	print("\n\t\tCLIENT SIDE\n")

	os.system('tput setaf 0')	
	print("Press 1 : WORK AS SSH CLIENT")

	os.system('tput setaf 1')
	print("\n\t\tSERVER SIDE\n")
	
	os.system('tput setaf 0')
	print("Press 2 : CREATE YOUR OWN SSH SERVER")
	print("Press 3 : CHECK SERVER STATUS")
	print("Press 4 : ROOT LOGIN ENABLE/DISABLE")
	print("Press 5 : NO PAAWORD LOGIN ENABLE/DISABLE")		
	print("Press 6 : To go Back")
	print ("\n\n")

	ch=int(input("Enter ur choice: "));

	if ch == 1 :
		os.system("python3 SSH-CLIENT.py")
	elif ch == 2 :
		os.system("python3 SSH-SERVER.py")
	elif ch == 3 :
		os.system("service sshd status")
		input("Enter to continue......")
	elif ch == 4 :
		os.system("python3 SSH-ROOT-LOGIN.py")
	elif ch == 5 :
		os.system("python3 SSH-N0-PASSWD-LOGIN.py")
	elif ch == 6 :
		sys.exit()		
	else:
		print("option not supported")
