import os
def exestart(ip):
    os.system('bash -c "python3 installer.py ' + ip + ' > log.txt"')
