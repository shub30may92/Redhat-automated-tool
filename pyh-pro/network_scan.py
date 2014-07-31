#!/usr/bin/python3
import os
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
print("NOTE : IF YOU WISH SCAN A RANGE OF IPS' SPECIFY THE RANGE EXAMPLE 192.168.0.1-255");		
x=input("enter start IP address :");
os.system('tput setaf 1');
print("   \t SCAN BEGINS    ");
os.system('tput setaf 0');
os.system("nmap -sP "+x);
input("Enter any key to exit");

