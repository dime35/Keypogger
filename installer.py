from urllib.request import urlretrieve
import os
import subprocess
from sys import argv

#"13.210.40.244"
ip = argv[1]
print(ip)
exein = "msfconsole -q -x 'db_nmap -sV " + ip + " ; hosts ; services ; vulns ; quit'"
#exein = "msfconsole -q -x 'db_status ; version ; exit'"
os.system(exein)
# msfconsole -x 'db_nmap -sV 13.210.40.244';'exit'

