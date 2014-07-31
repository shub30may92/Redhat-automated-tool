import os
import sys
globe=5
os.system("clear");
while globe==5:
		print("\t1.To Compress a Directory ");
		print("\t2.To return Back");
		choice=int(input("Enter your choice:"));
		if choice==1:
			z=input("\tEnter DirectoryName:");
			k=os.system("tar -zcvf "+z+".tar.gz "+z); 			
			if k==0:
				print("\tDirectory Successfully compressed..You can look for yout file_name.tar.gz file...\n\n");
			else:
				print("\tDirectory Compressing failed...\n\n");
		elif choice==2:
			sys.exit();
		else:
			print("Invalid Choice");
