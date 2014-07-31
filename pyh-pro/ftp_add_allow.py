#!/usr/bin/python3
import os
import sys
os.system("clear")
os.system("cat /etc/hosts.allow | grep vsftpd: >temp")
f=open("temp","r")
print("Below is the list of all ips that are allowed to connect to ftp service")
j=0
k="";
for i in f:
	j=j+1;
	k="";
	for z in i:
		if z in ('1','2','3','4','5','6','7','8','9','0','.'):
			k=k+z;
		else:
			pass
	print("{} {}".format(j,k));
f.close()
os.system("rm -f temp");
k=input("Enter the ip you wish to add to allow list");
q="vsftpd:";
f=open("temp","w")
f.write('\n'+q+k);
f.close();
r=os.system('cat temp >> /etc/hosts.allow')
os.system("rm -f temp")
if r==0:
	print("Successfully Added")
	print("Updated List of IP's is")
	j=0
	os.system("cat /etc/hosts.allow | grep vsftpd: >temp")
	f=open("temp","r")
	k="";
	for i in f:
		j=j+1;
		k="";
		for z in i:
			if z in ('1','2','3','4','5','6','7','8','9','0','.'):
				k=k+z;
			else:
				pass
		print("{} {}".format(j,k));
	f.close()
	os.system("rm -f temp");

else:
	print("Adding IP failed")
input("Press any key to exit")

