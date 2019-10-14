#!/usr/bin/python3

import matplotlib.pyplot as plt
import csv
import sys
from datetime import datetime

#Data
time = []
temp = []
humd = []
mag = []

#Make average of a list
def average(list, calib):
	avg = []
	tmp = []

	avg.append(list[0])

	for i in range(1, len(list)):
		if (i % 5 == 0): #Average of 5 samples
			avg.append(round((sum(tmp) / len(tmp)), 2)) #Make average
			tmp = []
			tmp.append(float(list[i]) * calib)
		else:
			tmp.append(float(list[i]) * calib)
	avg.append(round((sum(tmp) / len(tmp)), 2)) #Last sample

	return avg

#Time of average samples
def avg_time(list):
	avg_tm = []
	i = 1
	form = '%Y-%m-%d %H:%M:%S' #'%H:%M:%S'  #'%Y-%m-%d %H:%M:%S'

	for elm in list:
		if (i%5 == 0):
			s = elm.split('.')
			store = datetime.strptime(s[0], form)
			avg_tm.append(store)
		i += 1

	if(len(list)%5 != 0):	#If the number of samples is multiple of 5 messes up the result
		s = list[len(list)-1].split('.')
		store = datetime.strptime(s[0], form)
		avg_tm.append(store)

	return avg_tm

#Read data from CSV file
def samples():
	with open(sys.argv[1]) as samplesFile:
		samples = csv.reader(samplesFile, delimiter = ',')
		for row in samples:
			time.append(row[0])
			temp.append(row[1])
			humd.append(row[2])
			mag.append(row[3])

def graph():
	#Get every sample
	samples()
	#Transform time
	x = avg_time(time)

	#Makes one plot for each kind of data
	fig1, a1 = plt.subplots()

	fig2, a2 = plt.subplots()
	"""
	fig3, a3 = plt.subplots()
	"""

	#Humidity
	hmd_avg = average(humd, 3.4)
	Label = hmd_avg.pop(0)
	a1.plot(x, hmd_avg, '--o', label=Label)

	a1.set_xlabel("Number of sample")
	a1.set_ylabel("Humidity (%)")
	a1.set_title("Concrete Corrosion Samples")

#	plt.legend()		#Not nedded if just one plot
	plt.sca(a1)
	plt.xticks(rotation=90)

	#Temperature
	tmp_avg = average(temp, 1)
	Label = tmp_avg.pop(0)
	a2.plot(x, tmp_avg, '--o', color='darkorange', label=Label)

	a2.set_xlabel("Number of sample")
	a2.set_ylabel("Temperature (ºC)")
	a2.set_title("Concrete Corrosion Samples")

#	plt.legend()		#Not needded if just one plot
	plt.sca(a2)
	plt.xticks(rotation=90)
	"""
	#Magnetism
	mag_avg = average(mag, 1)
	Label = mag_avg.pop(0)
	a3.plot(x, mag_avg, '--o',color= 'green', label=Label)

	a3.set_xlabel("Number of sample")
	a3.set_ylabel("Magnetism (Gauss)")
	a3.set_title("Concrete Corrosion Samples")

#	plt.legend()		#Not nedded if just one plot
	plt.sca(a3)
	plt.xticks(rotation=90)
	"""

	plt.show()

#Main -> Let's rock!
if len(sys.argv) > 1:
	graph()
else:
	sys.exit("\n\tPlease, Select the Sample File Name\n")

