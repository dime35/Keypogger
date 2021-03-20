from urllib.request import urlretrieve
import os
import subprocess


#exein = "msfconsole -q -x 'db_status' >> log.txt"


#exe = os.system(exein)
#f = open("log.txt", "w")
#print("hi")

#os.system(bytes(exein))
#if __name__ == '__main__':
ip = "13.210.40.244" #input("enter your IP: ")
exein = "msfconsole -q -x 'db_nmap -sV " + ip + " ; hosts ; services ; vulns ; quit'"
#exein = "msfconsole -q -x 'db_status ; version ; quit'"
os.system(exein)

# msfconsole -x 'db_nmap -sV 13.210.40.244';'exit'