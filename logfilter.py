import re

filename = 'log.txt'

def readhost():
    with open(filename) as f:
        content = f.readlines()
        host = []
        i = 0;
        for n in content:
            j = re.sub(r'\s+', ' ', n)
            if j == ('host port proto name state info '):
                i += 1
            elif i == 1:
                i += 1
            elif i == 2 and j != ' ':
                host.append(j)
            elif i == 2:
                i+=1
    return host

#returns vuln section of .txt file to the application
def readvuln():
    with open(filename) as f:
        content = f.readlines()
        vuln = []
        i = 0;
        for n in content:
            j = re.sub(r'\s+', ' ', n)
            if n == 'Vulnerabilities ':
                i += 1
            elif i == 1:
                i += 1
            elif i == 2 and n != ' ':
                vuln.append()
            elif i == 2:
                i += 1
    return vuln


def splithost(line):
    strs = line.split()
    return [strs[1], strs[3], strs[4]]


def splitvuln(line):
    strs = line.split()
    return [strs[0], strs[1]]




