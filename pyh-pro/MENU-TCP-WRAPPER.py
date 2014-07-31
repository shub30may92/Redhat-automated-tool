#!/usr/bin/python3
import os
import sys
os.system("clear")
os.system('tput setaf 0');
x=5;
while x==5	:
		print("1.SSH Security");
		print("2.Telnet Security");
		print("3.FTP Security");
		print("4.Any Other Security");
		print("5.Go Back");
		choice=int(input("Enter your choice :"))
		if choice ==1:
			os.system("python3 ssh_security.py");
			os.system("clear");
		elif choice == 2 :
			os.system("python3 telnet_security.py")
			os.system("clear")
		elif choice == 3:
			os.system("python3 ftp_security.py")
			os.system("clear")
		elif choice == 4:
			os.system("tput setaf 1")			
			print("\t\tUNDER WORK\n\n")			
			#os.system("python3 other_security.py")
			#os.system("clear")
			os.system("tput setaf 0")
			input("Press enter to continue....")
			os.system("clear")	
		elif choice == 5:
			sys.exit();
		else:
			print("Invalid Choice");
			os.system("clear");


