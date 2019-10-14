#!/usr/bin/python

#imports
from tkinter import *
import files

#variables
fsmNames = []

#frames raiser
def raise_frame(frame):
	global fsmNames
	global nFSM
	nFSM = fsm.get()
	files.getInformation(name.get(), ltl.get(), nFSM)
	for i in range(0, fsm.get()):
		fsmNames.append(StringVar())
		Label(f2, text = "Name of FSM %s"%(i)).pack()
		Entry(f2, textvariable = fsmNames[i]).pack()
	frame.tkraise()

#Screen
root = Tk()
root.geometry("200x200")

#Main program and close
def do_your_stuff():
	global fsmNames
	global nFSM
	for i in range(0, nFSM):
		fsmNames[i] = fsmNames[i].get()
	files.evenMoreInformation(fsmNames)
	files.code()
	root.destroy()

#frames
f1 = Frame(root)
f2 = Frame(root)

for frame in (f1, f2):
	frame.grid(row = 0, column = 0, sticky = 'news')

#Basic info
Label(f1, text = "Please, write the file name").pack()
name = StringVar()
Entry(f1, textvariable = name).pack()

Label(f1, text = "How many LTL do you want?").pack()
ltl = IntVar()
Entry(f1, textvariable = ltl).pack()

Label(f1, text = "How many FSM do you want?").pack()
fsm = IntVar()
Entry(f1, textvariable = fsm).pack()
Button(f1, text = "OK", command=lambda:raise_frame(f2)).pack()

#Other info
Button(f2, text = "Generate", command=do_your_stuff).pack()

#Let's play
raise_frame(f1)
root.mainloop()
