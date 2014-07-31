import os
import sys
globe=5
os.system("clear");
while globe==5:
	
	print("\t1.To edit file present at current location");
	print("\t2.To edit file at some other location at some other location");
	print("\t3.To return back");
	choice=int(input("Enter your choice:"));
	if choice==1:
		x=input("Enter Filename:");
		k=os.system("vim "+x);
		if k==0:
			print("\tFile Successfully edited...\n\n");
		else:
			print("\tFile Editing failed...\n\n");
	elif choice==2:
		x=input("\tEnter Location ...example : /root/Desktop/ :");
		k=os.system("cd "+x);
		if	k==0:
			y=input("\tEnter Filename :");
			k=os.system("vim "+x+y);
			if k==0:
				print("File Successfully edited...\n\n");
			else:
          			print("File Editing failed...\n\n");
		else:
			print("File Editing Failed...Invalid Location");
	else:
		sys.exit();
