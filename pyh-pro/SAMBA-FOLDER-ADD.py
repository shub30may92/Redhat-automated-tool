#!/usr/bin/python3
import os

def again(x,y) :
	print(x)
	print(y)
	os.system("echo \[{}\]  >>  /etc/samba/smb.conf".format(y))
	os.system("echo path\ =\ {} >> /etc/samba/smb.conf".format(x))
	
def one(y) :
		
	print("Don't forget writing '/' at last of folder\'s path")
	x=input("Enter the Folder name with its path :")
#checking does user has given / after the folder name	
	if x[-1]=='/' :	
		folder="cat /etc/samba/smb.conf | grep path\ =\ "+x+" > trash"
		os.system(folder)
		h=open("trash",'r')
		k=1		
		for k in h :
			pass
#checking if folder is already there in configuration file		
		if k == 1 :	
			pub=input("Share this folder publically ?(y/n) : ")
			if pub == 'y' :
				again(x,y)
				os.system("echo public\ =\ yes >> /etc/samba/smb.conf")
			else :
				again(x,y)				
				user=input("Enter the username (valid users) : ")
				print(user)			
				os.system("useradd {}".format(user))				
				os.system("smbpasswd -a {}".format(user))
				#ip=input("Enter ip address : ")
				os.system("echo valid\ users\ =\ {}".format(user) +" >> /etc/samba/smb.conf")
				
		else :		
			m=k[7:-1]
			if m!=x : 
				pub=input("Share this folder publically ?(y/n) : ")
				if pub == 'y' :
					again(x,y)
					os.system("echo public\ =\ yes >> /etc/samba/smb.conf")
				else :
					again(x,y)
					user=input("Enter the username (valid users) : ")
					os.system("smbpasswd -a {}".format(user))
					#ip=input("Enter ip address : ")
					os.system("echo valid\ users\ =\ {} >> /etc/samba/smb.conf".format(user))			
			else :
				print("Folder already exists.")
	else :
		print("SORRY! INCORRECT PATH")
		a=input("You want to try give folder name again(y/n) : ")






y=input("Enter the share name : ")
shr_name = "cat /etc/samba/smb.conf | grep "+y+" > trash"
os.system(shr_name)
f=open("trash",'r')
i=1
for i in f :
	pass
#checking for unique share name
if i==1 :
	one(y)
else :
	z=i[1:-2]
	if y == z :
		print("SORRY! That share name already exist")
	else :
		print(y)		
		one(y)
os.system("service smb restart")
input("Enter to close.....")
#os.system("rm trash")



