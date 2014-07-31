#!usr/bin/python3
import os
k=True
while k:
	x=input("Enter your NIC name  ");
	y=input("Enter your IP  ");
	k=os.system("ifconfig "+x+" "+y);
	if k==0:
		print("Ip successfully changed");
		break;
	else:
		print("Ip change failed");
		r=input("You want to retry ...yes/no : ")
		if r is yes:
			pass
		else:	
			k=False;
input("Press any key to Exit")
