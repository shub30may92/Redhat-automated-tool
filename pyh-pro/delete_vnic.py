#!/usr/bin/python3
import os
k=os.system("service network restart");
if k==0:
	print("Successfully deleted");
else:
	print("Failed");	
input("Press any key to exit");

