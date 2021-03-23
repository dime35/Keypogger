import os

#Bash script embeded with python3 to send command terminal output to a .txt file
def exestart(ip):
    os.system('bash -c "python3 installer.py ' + ip + ' > log.txt"')
