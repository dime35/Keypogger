from urllib.request import urlretrieve
import os
import subprocess


ip = "13.210.40.244" #input("enter your IP: ")
exein = "msfconsole -q -x 'db_nmap -sV " + ip + " ; hosts ; services ; vulns ; quit'"
#exein = "msfconsole -q -x 'db_status ; version ; exit'"
os.system(exein)

# msfconsole -x 'db_nmap -sV 13.210.40.244';'exit'