import os
import sys
globe=5
os.system("clear");
while globe==5:
		print("\t1.To Copy File");
		print("\t2.To return Back");
		choice=int(input("Enter your choice:"));
		if choice==1:
			x=input("\tEnter Source_Location ...example : /root/Desktop/ :");
			y=input("\tEnter Destination_Location ...example : /root/Desktop/ :");
			z=input("\tEnter filename:");
			k=os.system("cp "+x+z+" "+y); 			
			if k==0:
				print("\tFile Successfully copied...\n\n");
			else:
				print("\tFile Copying failed...\n\n");
		elif choice==2:
			sys.exit();
		else:
			print("Invalid Choice");
