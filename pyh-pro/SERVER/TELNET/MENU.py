#!/usr/bin/python3
import os
import sys

while True:
	os.system('clear')

	os.system('tput setaf 1')
	print("\n\t\tCLIENT SIDE\n")

	os.system('tput setaf 0')	
	print("Press 1 : WORK AS TELNET CLIENT")

	os.system('tput setaf 1')
	print("\n\t\tSERVER SIDE\n")
	
	os.system('tput setaf 0')
	print("Press 2 : CREATE YOUR OWN TELNET SERVER")
	print("Press 3 : CHECK SERVER STATUS")
	print("Press 4 : ADD TO ALLOW LIST")
	print("Press 5 : REMOVE FROM ALLOW LIST")		
	print("Press 6 : ADD TO DENY LIST")
	print("Press 7 : REMOVE FROM DENY LIST")
	print("Press 8 : To go Back")
	print ("\n\n")

	ch=int(input("Enter ur choice: "));

	if ch == 1 :
		os.system("./TELNET-CLIENT.py")
	elif ch == 2 :
		os.system("./TELNET-SERVER.py")
	elif ch == 3 :
		os.system("service xinetd status")
		input("Enter to continue......")
	elif ch == 4 :
		os.system("./ALLOW-ADD.py")
	elif ch == 5 :
		os.system("./ALLOW-REMOVE.py")
	elif ch == 6 :
		os.system("./RESTRICT-ADD.py")
	elif ch == 7 :
		os.system("./RESTRICT-REMOVE.py")
	elif ch == 8 :
		sys.exit()		
	else:
		print("option not supported")
