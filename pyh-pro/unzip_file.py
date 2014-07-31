import os
import sys
globe=5
os.system("clear");
while globe==5:
		print("\t1.To Uncompress a File ");
		print("\t2.To return Back");
		choice=int(input("Enter your choice:"));
		if choice==1:
			z=input("\tEnter filename:");
			k=os.system("gunzip "+z); 			
			if k==0:
				print("\tFile Successfully unzipped....\n\n");
			else:
				print("\tFile Unzipping failed...\n\n");
		elif choice==2:
			sys.exit();
		else:
			print("Invalid Choice");
