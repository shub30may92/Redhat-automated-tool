import os
import sys
globe=5
os.system("clear");
while globe==5:
		print("\t1.To Compress a File ");
		print("\t2.To return Back");
		choice=int(input("Enter your choice:"));
		if choice==1:
			z=input("\tEnter filename:");
			k=os.system("gzip "+z); 			
			if k==0:
				print("\tFile Successfully compressed..You can look for yout file_name.gz file...\n\n");
			else:
				print("\tFile Compressing failed...\n\n");
		elif choice==2:
			sys.exit();
		else:
			print("Invalid Choice");
