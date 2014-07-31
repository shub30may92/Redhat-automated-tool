import os
import sys
globe=5;
os.system("clear");
while globe==5:
	
	print("\t1.To remove a file  present at current location");
	print("\t2.To remove a file  present at some other location");
	print("\t3.To return back");
	choice=int(input("Enter your choice:"));
	if choice==1:
		x=input("Enter Filename:");
		k=os.system("rm  "+x);
		if k==0:
			print("\tFile Successfully removed...\n\n");
		else:
			print("\tFile removal failed...\n\n");
	elif choice==2:
		x=input("\tEnter Location ...example : /root/Desktop/ :");
		y=input("\tEnter Filename :");
		k=os.system("rm  "+x+y);
		if k==0:
			print("File Successfully removed...\n\n");
		else:
			print("File removal failed...\n\n");
	else:
		sys.exit();
