from tkinter import *

class ShowName:

	def __init__(self, name, data):
		
		def close():
			root.destroy()

		root = Tk()
		root.title("¡LEGOS!")
		root.geometry("+950+450")

		Label(root, text = "Buscador\n").grid(row = 0, sticky = N, rowspan = 2)
		
		Label(root, text = 'Nombre:        ').grid(row= 2, column = 0)
		Label(root, text = 'Descripción:   ').grid(row= 3, column = 0)

		if data != False:
			Label(root, text = str(name)).grid(row= 2, column = 1)
			Label(root, text = str(data)).grid(row= 3, column = 1)
		else:
			Label(root, text = 'Nothing').grid(row= 2, column = 1)
			Label(root, text = 'Nothing').grid(row= 3, column = 1)

		Label(root, text = '').grid(row= 4)
		
		b1 = Button(root, text = 'Cerrar', command = close)
		b1.grid(sticky = S, rowspan = 2)
