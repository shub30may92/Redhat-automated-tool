import os
import sys
globe=5;
os.system("clear");
while globe==5:
	
	print("\t1.To remove a directory  present at current location");
	print("\t2.To remove a directory  present at some other location");
	print("\t3.To return back");
	choice=int(input("Enter your choice:"));
	if choice==1:
		x=input("Enter DirectoryName:");
		k=os.system("rmdir  "+x);
		if k==256:
			print("\tDirectory is non-empty you wish to continue deleting it..yes or no...\n\n");
			p=input("Enter yes or no");
			if p=="yes":
				q=os.system("rm -rfv "+x);
				if	q==0:
					print("Directory deletion successful");
				else:
					print("Directory deletion failure");
			else:
				pass;						
		else:
			print("\tDirectory removal failed...\n\n");
	elif choice==2:
		x=input("\tEnter Location ...example : /root/Desktop/ :");
		w=os.system("cd "+x);
		if w==0:
			y=input("\tEnter DirectoryName :");
			k=os.system("rmdir  "+x+y);
			if k==256:
				print("\tDirectory may be non-empty you wish to continue deleting it..yes or no...\n\n");
				p=input("Enter yes or no");
				if p=="yes":
					q=os.system("rm -rfv "+x+y);
					if	q==0:
						print("Directory deletion successful ");
					else:
						print("Directory deletion failure");
				else:
					pass;						
			else:
				print("\tDirectory removal failed...\n\n");		
		else:
			print("\tDirectory removal failed ..Invalid Address");	
	else:
		sys.exit();
