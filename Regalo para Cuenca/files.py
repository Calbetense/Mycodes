import os
from database import DataBase
from show import Show
from showName import ShowName

#Initialize files and directories
try:
	os.chdir("DataBase")
	_file = open("DataBase.json", "a")
	_file.close()
	_file2 = open("DataBase.json", "a")
	_file2.close()
except OSError:
	os.mkdir("DataBase")
	os.chdir("DataBase")
	_file = open("DataBase.json", "a")
	_file.write("{}")
	_file.close()
	_file2 = open("wDataBase.json", "a")
	_file2.write("{}")
	_file2.close()

#Create DataBase objects
data = DataBase(os.path.abspath("DataBase.json"))
wData = DataBase(os.path.abspath("wDataBase.json"))

#Translation
def add(name, desc):
	data.set(name, desc)

def wAdd(name, desc):
	wData.set(name, desc)

def delete(name):
	data.delete(name)

def wDelete(name):
	wData.delete(name)

def searchName(name):
	n = data.get(name)	
	a = ShowName(name, n)

def wSearchName(name):
	n = wData.get(name)	
	a = ShowName(name, n)

def showAll():
	#data.showAll()	
	a = Show(data, wData)

def deleteAll():
	data.deleteAll()

def wDeleteAll():
	wData.deleteAll()
