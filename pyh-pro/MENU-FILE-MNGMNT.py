#!/usr/bin/python3
import os
import sys
os.system("clear")
os.system('tput setaf 0');
x=5;
while x==5	:
		print("1.Create File");
		print("2.Remove File");
		print("3.List Files & Folders");
		print("4.Edit File");
		print("5.Copy file");
		print("6.Change Directory");
		print("7.Create Directory");
		print("8.Remove Directory");
		print("9.Copy Directory");
		print("10.Compress File");
		print("11.Unzip a File");
		print("12.Compress Folder");
		print("13.Unzip a Folder");
		print("14.To return Back");
		choice=int(input("Enter your choice :"));
		if choice==1	:
			os.system("python3 create_file.py");
			os.system("clear");
		elif choice==2  :
			os.system("python3 remove_file.py");
			os.system("clear");
		elif choice==3  :
			os.system("python3 list_files_folders.py");
			os.system("clear");
		elif choice==4  :
			os.system("python3 edit_file.py");
			os.system("clear");
		elif choice==5  :
			os.system("python3 copy_file.py");
			os.system("clear");
		elif choice==6  :
			os.system("python3 change_directory.py");
			os.system("clear");
		elif choice==7  :
			os.system("python3 create_directory.py");
			os.system("clear");
		elif choice==8  :
			os.system("python3 remove_directory.py");
			os.system("clear");
		elif choice==9  :
			os.system("python3 copy_directory.py");
			os.system("clear");
		elif choice==10  :
			os.system("python3 compress_file.py");
			os.system("clear");
		elif choice==11  :
			os.system("python3 unzip_file.py");
			os.system("clear");
		elif choice==12  :
			os.system("python3 compress_folder.py");
			os.system("clear");
		elif choice==13  :
			os.system("python3 unzip_folder.py");
			os.system("clear");
		elif choice==14  :
			os.system("clear");
			sys.exit();
