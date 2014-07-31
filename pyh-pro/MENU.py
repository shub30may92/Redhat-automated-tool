#!/usr/bin/python3

import os
import sys
import getpass

passwd="lw"

#passin=input("Enter ur password to access :")

passin=getpass.getpass("Enter ur password to access :  ")

if passin == passwd :
	while True:
		os.system('clear')
		os.system('tput setaf 1')
		print("\t\t\tWelcome to My Menu Driven System")
		os.system('tput setaf 0')
		print("\t\t\t--------------------------------\n\n")

	
		print("Press 1 : SERVER CONFIGURATION")
		print("Press 2 : SYSTEM MANAGEMENT")
		print("Press 3 : NETWORKING")
		print("Press 4 : PERMISSIONS & SECURITY")
		print("Press 5 : BOOT OPTIONS")
		print("Press 6 : CLOUD SERVICES")		
		print("Press 7 : GET A SHELL")

		print ("\n\n")

		ch=int(input("Enter ur choice: "));
		#print(ch)

		if ch == 1 :
			os.system("python3 MENU-SERVER.py")

		elif ch == 2 :
			os.system("python3 MENU-SYS-MNGMNT.py")
		elif ch == 3 :
			os.system("python3 MENU-NETWORK.py")
		elif ch == 4 :
			print (4)
		elif ch == 5 :
			print(5)
		elif ch == 6 :
			print(6)
		elif ch == 7 :
			os.system("gnome-terminal")			
			sys.exit()		
		else:
			print("option not supported")


		#input("enter to cont.......")


else:
	print("Access Denied")
	input("press enter to close....")


