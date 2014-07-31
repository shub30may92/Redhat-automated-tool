import os
import sys
globe=5
os.system("clear");
while globe==5:
		print("\t1.To Copy Directory");
		print("\t2.To return Back");
		x=" ";
		y=" ";
		z=" ";
		w=" ";
		choice=int(input("Enter your choice:"));
		if choice==1:
			x=input("\tEnter Source_Location ...example : /root/Desktop/ :");
			k=os.system("cd "+x);
			if	k==0:
				y=input("\tEnter DirectoryName :");
			else:
				pass;			
			z=input("\tEnter Destination_Location ...example : /root/Desktop/ :");
			d=os.system("cd "+y);
			if	k==0:
				w=input("\tEnter DirectoryName :");
			else:
				pass;
			if k==0:
				if d==0:	
					q=os.system("cp "+x+y+" "+z+w); 			
					if q==0:
						print("\tDirectory Successfully copied...\n\n");
					else:
						print("\tDirectory Copying failed...\n\n");
			else:
				print("Invalid Address");
		elif choice==2:
			sys.exit();
		else:
			print("Invalid Choice");
