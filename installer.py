from urllib.request import urlretrieve
import os
import subprocess
import cmd


# nmapname = 'nmap-7.91-win32.zip'
# metasploitname = 'metasploitframework-latest.msi'
#
# nmapurl = 'https://nmap.org/dist/' + nmapname
# metasploiturl = 'https://windows.metasploit.com/' + metasploitname
#
# urlretrieve(nmapurl, nmapname)
# urlretrieve(metasploiturl, metasploitname)



#os.system("msfconsole -x 'db_nmap -sV 13.210.40.244';'quit'")

subprocess.('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Metasploit\Metasploit Console')

# msfconsole -x 'db_nmap -sV 13.210.40.244';'quit'