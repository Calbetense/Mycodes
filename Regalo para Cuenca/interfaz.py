#imports
from tkinter import *
import files

#Variables

#Screen
root = Tk()
root.title("¡¡LEGOS!!")
root.geometry("+900+300")

#files.initialize()

#frames
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
	frame.grid(row = 0, column = 0, sticky = 'news')

#Main program and close
def close():
	root.destroy()
def mainFrame():
	raise_frame(f1)

#frames raiser
def raise_frame(frame):
	frame.tkraise()

#Add
def add():
	files.add(legoName.get(), legoDscription.get())
	raise_frame(f1)
	
def wAdd():
	files.wAdd(wLegoName.get(), wLegoDscription.get())
	raise_frame(f1)

#Delete
def delete():
	files.delete(legoName.get())
	raise_frame(f1)
def wDel():
	files.wDelete(wLegoName.get())
	raise_frame(f1)

def deleteAll():
	files.deleteAll()
	raise_frame(f1)
def wDeleteAll():
	files.wDeleteAll()
	raise_frame(f1)

#Search
def searchInvent():
	files.searchName(sName.get())	
def searchWish():
	files.wSearchName(sWish.get())

def wSearchByName():
	files.wSearchName(legoName.get())

def showEverythig():
	#print("Inventario\n")
	files.showAll()
	#print("----------------\nLista de Deseos\n")
	#files.wShowAll()
	pass

#Main frame
Label(f1).pack()

Button(f1, text = "Inventario", command=lambda:raise_frame(f2), height = 2, width = 15).pack()
Label(f1).pack()
Label(f1).pack()
Label(f1).pack()

Button(f1, text = "Lista de deseos", command=lambda:raise_frame(f3), height = 2, width = 15).pack()
Label(f1).pack()
Label(f1).pack()
Label(f1).pack()

Button(f1, text = "Buscar lego", command=lambda:raise_frame(f4), height = 2, width = 15).pack()
Label(f1).pack()
Label(f1).pack()
Label(f1).pack()

Button(f1, text = "Cerrar", command=close, height = 2, width = 15).pack()

#Inventario
Label(f2, text = "INVENTARIO").pack()
Label(f2).pack()
Label(f2, text = "Nombre").pack()
legoName = StringVar()
Entry(f2, textvariable = legoName).pack()
Label(f2).pack()

Label(f2, text = "Descripción").pack()
legoDscription = StringVar()
Entry(f2, textvariable = legoDscription).pack()
Label(f2).pack()

Button(f2, text = "Añadir", command=add, height = 2, width = 15).pack()
Button(f2, text = "Borrar", command=delete, height = 2, width = 15).pack()
Label(f2, text='').pack()
Button(f2, text = "Borrar Todo", command=deleteAll, height = 2, width = 15).pack()
Label(f2, text='').pack()
Button(f2, text = "Volver", command=mainFrame, height = 2, width = 15).pack()
Button(f2, text = "Cerrar", command=close, height = 2, width = 15).pack()

#Lista de deseos
Label(f3, text = "LISTA DE DESEOS").pack()
Label(f3).pack()

Label(f3, text = "Nombre").pack()
wLegoName = StringVar()
Entry(f3, textvariable = wLegoName).pack()
Label(f3).pack()

Label(f3, text = "Descripción").pack()
wLegoDscription = StringVar()
Entry(f3, textvariable = wLegoDscription).pack()
Label(f3).pack()

Button(f3, text = "Añadir", command=wAdd, height = 2, width = 15).pack()
Button(f3, text = "Borrar", command=wDel, height = 2, width = 15).pack()
Label(f3, text='').pack()
Button(f3, text = "Borrar Todo", command=wDeleteAll, height = 2, width = 15).pack()
Label(f3, text='').pack()
Button(f3, text = "Volver", command=mainFrame, height = 2, width = 15).pack()
Button(f3, text = "Cerrar", command=close, height = 2, width = 15).pack()

#Buscar
Label(f4, text = "BUSCAR").pack()
Label(f4).pack()
sName = StringVar()
Entry(f4, textvariable = sName).pack()
Button(f4, text = "Buscar en el Inventario", command=searchInvent).pack()
Label(f4).pack()

sWish = StringVar()
Entry(f4, textvariable = sWish).pack()
Button(f4, text = "Buscar en la Lista de Deseos", command=searchWish).pack()

Label(f4).pack()
Button(f4, text = "Show ALL", command=showEverythig, height = 2, width = 15).pack()

Label(f4).pack()
Label(f4).pack()
Button(f4, text = "Volver", command=mainFrame, height = 2, width = 15).pack()
Button(f4, text = "Cerrar", command=close, height = 2, width = 15).pack()

#Let's play
raise_frame(f1)
root.mainloop()

