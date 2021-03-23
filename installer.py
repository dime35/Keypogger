#import os for interacting with the operating system
import os
from sys import argv

#Starts metasploit with msfconsole and then runs a nmap scan. Then takes results to run with hosts, services, vulns, and then exits the terminal
ip = argv[1]
exein = "msfconsole -q -x 'db_nmap -sV " + ip + " ; hosts ; services ; vulns ; quit'"
os.system(exein)

