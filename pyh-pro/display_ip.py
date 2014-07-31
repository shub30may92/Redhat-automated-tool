#!/usr/bin/python3
import os
os.system("ifconfig|grep inet\ addr>temp");
f=open("temp","r");
k=0;
os.system("ifconfig > temp1");
os.system("cat temp1");
print("NOTE THAT HERE IP'S OF ALL YOUR NIC ARE DISPLAYED AND ALSO THE LAST IP IS YOUR LOOP BACK IP...Following are your ip's");
for i in f:
	print("{}. {}".format(k+1,i),end="")
	k=k+1;
f.close();
os.system("rm temp");
os.system("rm temp1");
input("Press any key to Exit");
