import os
import sys

while True:
	os.system('clear')
	
	print("Press 1 : FTP")
	print("Press 2 : TELNET")
	print("Press 3 : SSH")
	print("Press 4 : WEB SERVER")
	print("Press 5 : NIS SERVER")		
	print("Press 6 : MAIL SERVER")
	print("Press 7 : SAMBA SERVER")
	print("Press 8 : TCP WRAPPER")
	print("Press 9 : To go Back")
	print ("\n\n")

	ch=int(input("Enter ur choice: "));

	if ch == 1 :
		os.system("python3 MENU-FTP.py")
	elif ch == 2 :
		os.system("python3 MENU-TELNET.py")
	elif ch == 3 :
		os.system("python3 MENU-SSH.py")
	elif ch == 4 :
		os.system("./WEB/MENU.py")
	elif ch == 5 :
		os.system("./NIS/MENU.py")
	elif ch == 6 :
		os.system("./MAIL/MENU.py")
	elif ch == 7 :
		os.system("python3 MENU-SAMBA.py")
	elif ch == 8 :
		os.system("python3 MENU-TCP-WRAPPER.py")	
	
	elif ch == 9 :
		sys.exit()		
	else:
		print("option not supported")
