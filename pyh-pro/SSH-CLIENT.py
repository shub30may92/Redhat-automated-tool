import os

y=os.system("rpm -q openssh-clients > /root/Desktop/trash.txt")
if y == 0 :
	print("Software is already installed")	
	#pass
else :
	os.system("yum install openssh-clients > /root/Desktop/trash.txt")

os.system("rm /root/Desktop/trash.txt")


y=input("Enter the ipaddress of server : ")
x=input("Enter the username for remote login : ")
os.system("ssh " + x + "@" + y)
input("perss enter to close...") 
