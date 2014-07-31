import os
import sys
globe=5
os.system("clear");
while globe==5:
	
	print("\t1.To view files and folders at current location");
	print("\t2.To view files and folders at some other location");
	print("\t3.To view hidden files and folders at current location");
	print("\t4.To view hidden files and folders at some other location");
	print("\t5.To return back");
	choice=int(input("Enter your choice:"));
	if choice==1:
		k=os.system("ls -F| cat -n");
		if k==0:
			print("\t Successfully Listed...\n\n");
		else:
			print("\tFile creation failed...\n\n");
	elif choice==2:
		x=input("\tEnter Location ...example : /root/Desktop/ :");
		y=input("\tEnter Filename :");
		k=os.system("ls -F "+x+" | cat -n");
		if k==0:
			print(" Successfully listed...\n\n");
		else:
			print(" Listing failed...\n\n");
	elif choice==3:
		k=os.system("ls -Fa| cat -n");
		if k==0:
			print("\t Successfully Listed...\n\n");
		else:
			print("\tFile creation failed...\n\n");
	elif choice==4:
		x=input("\tEnter Location ...example : /root/Desktop/ :");
		y=input("\tEnter Filename :");
		k=os.system("ls -F "+x+" | cat -n");
		if k==0:
			print(" Successfully listed...\n\n");
		else:
			print(" Listing failed...\n\n");
		
	else:
		sys.exit();
