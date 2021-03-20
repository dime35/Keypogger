import tkinter as tk
import re
import execute

ipregex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

root = tk.Tk()
root.wm_title("really really funny")

v=tk.StringVar()

title = title = tk.Label(text="IP")
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
        execute.exestart(input)


submit = tk.Button(text="Start scan",
                   command=buttonPressed,
                   width=25,
                   height=5,
                   bg="black",
                   fg="white")
submit.pack()
root.mainloop()
