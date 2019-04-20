import getpass
import sys
import telnetlib

# library already written that allows one to telnet and module written that prompts user for password
#
HOST = "localhost" #change the localhost to your ip address
user = raw_input("Enter your username: ") # prompts you to enter your username
password = getpass.getpass() #uses getpass module and promts user for password which is then stored in the variable password

tn = telnetlib.Telnet(HOST) #uses the telnetlib module to telnet to the host variable which is your ip address, stored as tn

tn.read_until("username: ") # once telnet is done, read console output and wait until it sees username
tn.write(user + "\n")   # when it sees username, write the value of stored user vaariable with carriage return
if password:    # if there's a value stored in the password variable as per line 9
    tn.read_until("Password: ")  # read console output and wait until it sees password prompt
    tn.write(password + "\n")  # then write the value of the password variable with carriage return

tn.write("enable\n")  #enable is sent
tn.write("cisco\n")   #the enabled password is sent
tn.write("conf t\n")
tn.write("int loop 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all() # this prints out everything the script saw during the telnet session