#import OS library
import os

#Get information
names = []
nameOfFile = ""
nFSM = 0
nLTL = 0
def getInformation(name, ltl, fsm):
	global nameOfFile
	global nLTL
	global nFSM
	nameOfFile = name
	nLTL = ltl
	nFSM = fsm

#get even more information
def evenMoreInformation(fsmNames):
	global nFSM
	for i in range(0, nFSM):
		names.append(fsmNames[i])

#LTL generation code
def code():
	global nLTL
	global nFSM
	str_LTL = "/*****  Especificaciones   ******/"

	for i in range(0,nLTL):
		str_LTL = str_LTL + """
	ltl spec%d {
		[]( )
	}
	"""%(i)

	#FSM states
	str_states = "\n/*****  FSM  *****/\n"

	for i in range(0, nFSM):
		str_states = str_states + """/* %s */
	mtype = {};\n
	mtype state_%s;\n
	""" % (names[i], names[i])

	#FSM generation code
	str_FSM = ""
	for i in range(0, nFSM):
		str_FSM = str_FSM + """
	/**** %s ****/
	active proctype %s(){

		state_%s = /* Initial state */;

		do
			:: (state_%s == /* First state */ )-> atomic {
			        if
			                :: 
			        fi;
			}
			:: (state_%s == /* Second state */ )-> atomic {
			        if
			                :: 
			        fi;
			}
		od;

	} """ % (names[i], names[i], names[i], names[i], names[i])

	#Enviroment generation code
	str_evrm = """\n/***** ENVIROMENT *******/
	active proctype enviroment() {
		do
		:: if
			:: /* do stuff */
			:: skip
		   fi ;
		   printf ( /* DEBUG */ );
		od;
	}"""

	#All code together
	str = str_LTL + "\n" + str_states + "\n\n" + str_FSM + "\n" + str_evrm

	#Create folder if not exist and come into
	try:
		os.chdir("spin")
	except OSError:
		os.mkdir("spin")
		os.chdir("spin")

	#creates a promela file
	file = open(nameOfFile+".pml", "w")

	#writes all code
	file.write(str)

	#closes file
	file.close()
