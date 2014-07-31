import os
import sys
globe=5
os.system("clear");
while globe==5:
	
	print("\t1.To create at current location");
	print("\t2.To create at some other location");
	print("\t3.To return back");
	choice=int(input("Enter your choice:"));
	if choice==1:
		x=input("Enter DirectoryName:");
		k=os.system("mkdir "+x);
		if k==0:
			print("\tDirectory Successfully created...\n\n");
		else:
			print("\tDirectory Creation failed...\n\n");
	elif choice==2:
		x=input("\tEnter Location ...example : /root/Desktop/ :");
		k=os.system("cd "+x);
		if	k==0:
			y=input("\tEnter DirectoryName :");
			k=os.system("mkdir "+x+y);
			if k==0:
				print("Directory Successfully Created...\n\n");
			else:
          			print("Directoty Creation failed...\n\n");
		else:
			print("Directory creation failed...Invalid Location");		
		
	else:
		sys.exit();
