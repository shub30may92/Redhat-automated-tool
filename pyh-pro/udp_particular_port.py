#!/usr/bin/python3
import os
import sys
k=os.system("rpm -q nmap");
if k != 0 :
	print ("Installing nmap for you");
	w=os.system("yum install nmap -y");
	if w==0:
		print("Installation successful");
	else:
		print("Installation failed");
		exit();

else :
	pass
os.system("clear");
s=True
while s:
	print("NOTE : IF YOU WISH SCAN A RANGE OF IPS' SPECIFY THE RANGE EXAMPLE 192.168.0.1-255");		
	x=input("enter start IP address :");
	print("1.For scanning particular port \n2.For scanning a range of ports");
	k=int(input("Enter choice"))
	if k==1:
		r=input("Enter port no : ")
		os.system('tput setaf 1');
		print("  \t\tUDP PORT SCAN BEGINS\t");
		os.system('tput setaf 0');
		os.system("nmap -sU "+x+" -p "+r);
		input("Enter any key to exit :");
		sys.exit();	
	elif k==2:
		r=input("Enter start port no :")
		o=input("Enter final port no :")
		os.system('tput setaf 1');
		print("  \t\tUDP PORT SCAN BEGINS\t");
		os.system('tput setaf 0');
		os.system("nmap -sU "+x+" -p "+r+"-"+o);
		input("Enter any key to exit :");
		sys.exit();
	else:
		print("Invalid Choice")
		p=input("Enter yes to retry no to exit: ");
		if p=="yes":
			pass
		else:
			s=False;

