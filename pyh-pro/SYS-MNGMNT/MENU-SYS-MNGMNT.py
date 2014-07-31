import os
import sys

while True:
	os.system('clear')
	
	print("Press 1 : USER MANAGEMENT")
	print("Press 2 : FILE & DIRECTORY MANAGEMENT")
	print("Press 3 : To go Back")
	print ("\n\n")

	ch=int(input("Enter ur choice: "));

	if ch == 1 :
		os.system("./MENU-USR-MNGMNT.py")
	elif ch == 2 :
		sys.exit()
	elif ch == 3 :
		sys.exit()
	
	else:
		print("option not supported")


	

