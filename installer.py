
import os
from sys import argv

ip = argv[1]
exein = "msfconsole -q -x 'db_nmap -sV " + ip + " ; hosts ; services ; vulns ; quit'"
os.system(exein)

