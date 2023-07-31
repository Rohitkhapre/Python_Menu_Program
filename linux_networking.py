import os
print("________________________________________________")

print(".........WELCOME TO LINUX AND NETWORKING........")
print("________________________________________________")

def Account():
	while True:

		print("""
----Operations Related to User Account-----
    1. Create New user
    2. Check the current logged in user
    3. Switch User Account
    4. Go back to menu
    TO Exit(Press 'e' or 'E')
    Press the No. to perform Operations!!
        """)

		Ch = input("enter operation: ")
		if(Ch == "1"):
			N = input("\nEnter User Name:")
			os.system("useradd "+N)
		elif(Ch == "2"):
			os.system('whoami')
		elif(Ch == "3"):
			A = input("\nEnter User Name you want to switch to:")
			os.system("su "+A)
		elif(Ch == "4"):
			menu()
		elif(Ch == 'e' or 'E'):
			exit()
def DateTime():
	while True:

		print("""
----Operations Related to User Account-----
    1. View calender
    2. clock
    3. change systems date and time
    4. Go back to menu
    TO Exit(Press 'e' or 'E')
    Press the No. to perform Operations!!
        """)

		Ch = input("enter operation: ")
		if(Ch == "1"):
			os.system('cal')
		elif(Ch == "2"):
			os.system('watch -n 1 date')
		elif(Ch == "3"):
			value=input("enter the valsues in format<MM><DD><hh><mm><YY>: ")
			os.system("date "+value)
		elif(Ch == "4"):
			menu()
		elif(Ch == 'e' or 'E'):
			exit()
def IpAddress():
	while True:

		print("""
----Operations Related to IP Address-----
    1. See IpAddress of system
    2. Change IpAddress of system
    3. Find IP of domain
    4. Go back to menu
    TO Exit(Press 'e' or 'E')
    Press the No. to perform Operations!!
        """)

		Ch = input("enter operation: ")
		if(Ch == "1"):
			os.system('ifconfig')
		elif(Ch == "2"):
			newip = input("Enter new IP:")
			os.system("ifconfig enp0s3 "+newip)
			os.system('ifconfig')
		elif(Ch == "3"):
			value=input("enter the domain name: ")
			os.system("nslookup "+value)
		elif(Ch == "4"):
			menu()
		elif(Ch == 'e' or 'E'):
			exit()

def menu():
	print("...........Menu.........")
	print("""\n 1.User Account 
             \n 2.Date & Time 
             \n 3.Ip Address
             \n 4.Convert one NumberSystem into another
             \n TO Exit(Press 'e' or 'E')""")
	print("\n Press the No. to perform Operations!!")
	choise = input("Enter your Choice: ")
	if(choise == "1"):
		Account()
	elif(choise == "2"):
		DateTime()
	elif(choise == "3"):
		IpAddress()
	elif(choise == "4"):
		print("---Enter 'ibase = <value>' for input value 'obase = <value>' for outpt value:---")
		os.system("bc")
	elif(choise == 'e' or 'E'):
		exit()
menu() 

