#!/usr/bin/python3
import os
import sys
x=5;
os.system("clear")
print("TELNET SECURITY")
while x==5	:
		print("1.Display IP's allowed");
		print("2.Display IP's blocked");
		print("3.Add an IP to allow list");
		print("4.Delete an IP from allow list");
		print("5.Add an IP to deny list");		
		print("6.Delete an IP from deny list");
		print("7.To return back")
		choice=int(input("Enter your choice :"))
		if choice ==1:
			os.system("python3 telnet_display_allow.py");
			os.system("clear");
		elif choice == 2 :
			os.system("python3 telnet_display_deny.py")
			os.system("clear")
		elif choice == 3:
			os.system("python3 telnet_add_allow.py")
			os.system("clear")
		elif choice == 4:
			os.system("python3 telnet_delete_allow.py")
			os.system("clear")
		elif choice == 5:
			os.system("python3 telnet_add_deny.py")
			os.system("clear")
		elif choice == 6:
			os.system("python3 telnet_delete_deny.py")
			os.system("clear")
		elif choice == 7:
			sys.exit();
		else:
			print("Invalid Choice");
			os.system("clear");
