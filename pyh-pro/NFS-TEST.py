#!/usr/bin/python3
import os
import sys
while True:

	os.system('clear')
	os.system('tput setaf 1')
	print("\n\t\tCLIENT SIDE\n")
	os.system('tput setaf 0')	
	print("Press 1 : CONNECT TO NFS SERVER")
	os.system('tput setaf 1')
	print("\n\t\tSERVER SIDE\n")
	os.system('tput setaf 0')
	
	print("Press 2 : CREATE YOUR OWN NFS SERVER")
	print("Press 3 : CHECK SERVER STATUS")
	print("Press 4 : ADD FOLDER TO BE SHARED")
	print("Press 5 : MODIFY PERMISSIONS")
	print("Press 6 : CONFIGURATION FILE")	
	print("Press 7 : To go Back")
	print ("\n\n")
	ch=int(input("Enter ur choice: "));

	if ch == 1 :
		x=input("Enter the Server IP address : ")
		y=input("Enter the shared folder : ")
		z=input("Enter the mount point : ")
		os.system("mount " + x + ":" + y + " " + z)
		input("Enter to continue......")		

	elif ch == 2 :
		os.system("rpm -e nfs-utils --nodeps > /root/Desktop/trash.txt")
		os.system("yum install nfs-utils > /root/Desktop/trash.txt")
		input("Enter to continue......")	

	elif ch == 3 :
		os.system("service nfs status")
		input("Enter to continue......")

	elif ch == 4 :
		y=input("Enter the Folder to be shared : ")
		z=len(y)
		os.system("cat /etc/exports | grep "+ y +" > trash")
		f=open("trash",'r')
		for i in f :
			pass 
		j=i[:z]
		if j == y :
			print("SORRY! That folder already exists")
		else :
			x=input("Enter cliet's IP address : ")
			cmd='echo {} {} >> /etc/exports'.format( y, x )
			os.system(cmd)
			os.system("service nfs restart")
		os.system("trash")
		input("Enter to close.......")
	
	elif ch == 5 :
		os.system("cat /etc/exports")
		y=input("Emter the folder name : ")
		x=input("Enter the  IP address : ")
		os.system("cat /etc/exports | grep " + y + "\  |grep " + x +" > /root/Desktop/trash")				
		f=open("/root/Desktop/trash", 'r')
		input("enter to proceed....")
		i=1		
		for i in f :
			pass
		if i is '1' :
			print("IP address not found")
		else :
			cmd="sed -i -e 's/" + x + "/" + x + "(rw)/g' /etc/exports"
			print(cmd)			
			os.system(cmd)
			print("done")
			input("Enter to close.....")
			
	elif ch == 6 :
		input("You are entering to NFS server\'s configuration file. Be sure of any changes you make in this file.\nPress enter to continue...")
		os.system("vim /etc/exports")	

	elif ch == 7 :
		sys.exit()		
	
	else:
		print("option not supported")
