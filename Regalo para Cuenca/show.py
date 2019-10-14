from tkinter import *

class Show:

	def __init__(self, data, wData):	
		def close():
			root.destroy()

		root = Tk()
		root.title("¡LEGOS!")
		root.geometry("+850+350")
	
		scrll1 = Scrollbar(root, orient = VERTICAL)
		scrll2 = Scrollbar(root, orient = VERTICAL)

		xscrll1 = Scrollbar(root, orient = HORIZONTAL)
		xscrll2 = Scrollbar(root, orient = HORIZONTAL)

		Label(root, text = "INVENTARIO\n").grid(row = 0, sticky = N)

		l1 = Listbox(root, yscrollcommand = scrll1.set, xscrollcommand = xscrll1.set)
		for i in data.db:
			l1.insert(END, "%s:    %s" % (i, data.db[i]))
		l1.grid(row = 1, column = 0)
		scrll1.grid(row = 1, column= 1, sticky = N+S)
		xscrll1.grid(row = 2, sticky = E+W)

		Label(root, text = "\nLISTA DE DESEOS\n").grid(row = 3)

		l2 = Listbox(root, yscrollcommand = scrll2.set, xscrollcommand = xscrll2.set)
		for i in wData.db:
			l2.insert(END, "%s:    %s" % (i, wData.db[i]))
		l2.grid(row = 4, column = 0)
		scrll2.grid(row = 4, column= 1, sticky = N+S)
		xscrll2.grid(row = 5, sticky = E+W)

		b1 = Button(root, text = 'Cerrar', command = close)
		b1.grid(sticky = S)

		scrll1.config(command=l1.yview)
		xscrll1.config(command=l1.xview)
		scrll2.config(command=l2.yview)
		xscrll2.config(command=l2.xview)	
	



