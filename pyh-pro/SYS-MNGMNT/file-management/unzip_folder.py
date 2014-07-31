import os
import sys
globe=5
os.system("clear");
while globe==5:
		print("\t1.To Uncompress a Folder ");
		print("\t2.To return Back");
		choice=int(input("Enter your choice:"));
		if choice==1:
			z=input("\tEnter DirectoryName ...exmaple hello:");
			k=os.system("tar -zxvf "+z+".tar.gz"); 			
			if k==0:
				print("\tDirectory Successfully unzipped....\n\n");
			else:
				print("\tDirectory Unzipping failed...\n\n");
		elif choice==2:
			sys.exit();
		else:
			print("Invalid Choice");
