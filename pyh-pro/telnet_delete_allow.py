#!/usr/bin/python3
import os
import sys
os.system("clear")
os.system("cat /etc/hosts.allow | grep xinetd: >temp")
f=open("temp","r")
print("Below is the list of all ips that are allowed to connect to telnet service")
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
k=input("Enter the ip you wish to delete from allow list");


w="sed -i -e 's"; 
q="/xinetd:"+k+"/";
e="/g' /etc/hosts.allow"
y=w+q+e
r=os.system(y);
if r==0:
	print("Successfully Deleted")
	print("Updated List of IP's is")
	j=0
	os.system("cat /etc/hosts.allow | grep xinetd: >temp")
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
	print("Deleting IP failed")
input("Press Any Key to Exit");

