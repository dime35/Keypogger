import tkinter as tk
import tkinter.ttk as ttk
import re
import execute
import logfilter

ipregex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

root = tk.Tk()
root.wm_minsize(350, 400)
root.wm_title("Anti-Keypogger")

v = tk.StringVar()

title = title = tk.Label(text="Enter YOUR IP")
title.pack()

entry = tk.Entry(text=v)
entry.pack()

def getEntry():
    return entry.get()
def buttonPressed():
    input = getEntry()
    search = re.match(ipregex, input)
    if search == None:
        v.set("")
    else:
        open('log.txt', 'w').close()

        execute.exestart(input)
        fillporttree()
        fillvulntree()



porttree = ttk.Treeview( columns=("Port", "Type"), height=10)

porttree.heading('#0', text='Port')
porttree.heading('#1', text='Type')
porttree.heading('#2', text='Status')

porttree.column('#0', stretch=tk.YES)
porttree.column('#1', stretch=tk.YES)
porttree.column('#2', stretch=tk.YES)

porttree.pack(pady = 15)

vulntree = ttk.Treeview( columns=("Vulnerability"), height=2)

vulntree.heading('#0', text='Vulnerability')
vulntree.heading('#1', text='Date')

vulntree.column('#0', stretch=tk.YES)
vulntree.column('#1', stretch=tk.YES)
vulntree.pack(pady = 15)

submit = tk.Button(text="Start scan",
                   command=buttonPressed,
                   width=25,
                   height=5,
                   bg="black",
                   fg="white")
def fillporttree():
    ports = logfilter.readhost();
    for port in ports:
        s = logfilter.splithost(port)
        porttree.insert(parent='',index = 0,text = s[0], values=(s[1], s[2]))
def fillvulntree():
    vulns = logfilter.readvuln()
    if vulns == []:
        return
    for vuln in vulns:
        s = logfilter.splithost(vuln)
        vulntree.insert(parent='', index=0, text=s[0], values=(s[1]))


submit.pack()
root.mainloop()
