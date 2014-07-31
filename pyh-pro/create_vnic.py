#!/usr/bin/python3
import os
w=True
while w:
	x=input("Enter your virtual NIC name  ");
	y=input("Enter your virtual IP  ");
	k=os.system("ifconfig "+x+" "+y);
	if k==0:
		print("Virtual Card successfully created");
		break;
	else:
		print("Virtual Card creation failed");
		r=input("You want to retry ...yes to retry : ")
		if r =="yes":
			pass
		else:	
			w=False; 
input("Enter any key to exit");
