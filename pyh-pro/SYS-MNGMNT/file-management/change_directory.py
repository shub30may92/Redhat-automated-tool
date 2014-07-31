import os
import sys
globe=5
os.system("clear");
while globe==5:
		print("\t1.To Change Directory");
		print("\t2.To return Back");
		choice=int(input("Enter your choice:"));
		if choice==1:
			y=input("\tEnter Destination_Location ...example : /root/Desktop/ :");
			k=os.system("cd "+y); 			
			if k==0:
				print("\tDirectory Successfully changed...\n\n");
			else:
				print("\tDirectory Changing Failed...\n\n");
		elif choice==2:
			sys.exit();
		else:
			print("Invalid Choice");
