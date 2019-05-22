#### script that creates multiple vlan on multiple switches using telnet
### open up a file and read the contents of that file.
## the ips will be in a file. note they can be the only thing in the file as it'll be reading the contents in rows
## this script will login to switches one at a time, it's possible to open multiple sessions at the same time using process pools

user = input("Enter your username: ")
password = getpass.getpass()


f = open("switchfile")

for IP in f:
	IP=IP.strip()    #remove any whitespaces
	print ("configuring switch " + (IP))
	HOST = IP
	tn = telnetlib.Telnet(HOST)
	tn.read_until(b"username: ")
	tn.write(user.encode('ascii') + b"\n")    #the encode converts it to ascii characters
	if password:
		tn.read_until(b"Password: ")
		tn.write(password.encode('ascii') + b"\n")
	tn.write(b"enable\n")  #enable is sent
	tn.write(b"cisco\n")   #the enabled password is sent
	tn.write(b"conf t\n")
	for n in range (2,11):
		tn.write(b"vlan " + str(n).encode('ascii') + b"\n"")      ##b means we have to send a byte string to python; hence we need to encode the string
		tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n"")
	tn.write(b"end\n")
	tn.write(b"exit\n")
	print(tn.read_all().decode('ascii'))