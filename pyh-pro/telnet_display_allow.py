#!/usr/bin/python3
import os
import sys
os.system("clear")
os.system("cat /etc/hosts.allow | grep xinetd: >temp")
f=open("temp","r")
print("Below is the list of all ips that are allowed to telnet ")
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
input("Press any key to Exit");
	
