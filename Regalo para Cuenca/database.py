import os
import json

class DataBase:
	#Intern
	def __init__(self , location):
		self.location = os.path.expanduser(location)
		self.load(self.location)

	def load(self , location):
		if os.path.exists(location):
	    		self._load()
		else:
	    		self.db = {}
		return True

	def _load(self):
		self.db = json.load(open(self.location , "r"))

	def dumpdb(self):
		try:
		    json.dump(self.db , open(self.location, "w+"))
		    return True
		except:
		    return False
	#Extern
	def set(self , key , value):
		try:
		    self.db[str(key)] = value
		    self.dumpdb()
		    return True
		except Exception as e:
		    print("[X] Error Saving Values to Database : " + str(e))
		    return False

	def get(self , key):
		try:
		    return self.db[key]
		except KeyError:
		    print("No Value Can Be Found for " + str(key))
		    return False

	def delete(self , key):
		if not key in self.db:
		    return False
		del self.db[key]
		self.dumpdb()
		return True

	def deleteAll(self):
		self.db.clear()
		self.dumpdb()

	def showAll(self):
		for i in self.db:
			print(i + '\t' + self.db[str(i)])
		
			
