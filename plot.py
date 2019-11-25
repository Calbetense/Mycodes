#!/usr/bin/python3

import pandas as pd
import sys
import matplotlib.pyplot as plt
from datetime import datetime

#Global
uid = []
df = 0

def calib(sen, mod):
    if sen == "804f34c6d2fb":
        if mod == "TEMP":
            return 4
        if mod == "HUMD":  
            return 2.8
        if mod == "MAGN":  
            return 0                #-1
    elif sen == "7525c4109aec" : 
        if mod == "TEMP":
            return 4
        if mod == "HUMD":  
            return 2.8
        if mod == "MAGN":  
            return 0                #-2
    elif sen == "f8e4fbf56bc5": 
        if mod == "TEMP":  
            return 4
        if mod == "HUMD":  
            return 2.8/1.17
        if mod == "MAGN":  
            return 0                #-1.7
    else: 
        if mod == "TEMP":  
            return 0
        if mod == "HUMD":  
            return 1
        if mod == "MAGN":  
            return 0

def avg_time(sen):
    avg_tm = []
    i = 0
    form = '%Y-%m-%d %H:%M:%S' #'%H:%M:%S'  #'%Y-%m-%d %H:%M:%S'

    time = df.loc[df['ADDR'] == sen, 'TIME']
    time = time.values.tolist()

    for elm in time:
        if (i%5 == 0):
            s = elm.split('.')
            store = datetime.strptime(s[0], form)
            avg_tm.append(store)
        i += 1
    """
    POR AHORA ESTA PARTE PARECE INNECESARIA
    if(len(time)%5 != 0):	#If the number of samples is multiple of 5 messes up the result
        s = time[len(time)-1].split('.')
        store = datetime.strptime(s[0], form)
        avg_tm.append(store)
    """
    return avg_tm

def avg_temp(sen):
    avg = []
    tmp = [] 
    
    clb = calib(sen, "TEMP")

    #Get a list of temperature
    temp = df.loc[df['ADDR'] == sen, 'TEMP']
    temp = temp.values.tolist()

    for i in range(1, len(temp)):
        if (i % 5 == 0): #Average of 5 samples

            avg.append(round((sum(tmp) / len(tmp)), 2)) #Make average
            tmp = []
            tmp.append(float(temp[i]) - clb)
        else:
            tmp.append(float(temp[i]) - clb)
    avg.append(round((sum(tmp) / len(tmp)), 2)) #Last sample

    return avg

def avg_humd(sen):
    avg = []
    tmp = []
    
    clb = calib(sen, "HUMD")

    humd = df.loc[df['ADDR'] == sen, 'HUM']
    humd = humd.values.tolist()

    for i in range(1, len(humd)):
        if (i % 5 == 0): #Average of 5 samples
            avg.append(round((sum(tmp) / len(tmp)), 2)) #Make average
            tmp = []
            tmp.append(float(humd[i]) * clb)
        else:
            tmp.append(float(humd[i]) * clb)
    avg.append(round((sum(tmp) / len(tmp)), 2)) #Last sample

    return avg

def avg_mag(sen):
    avg = []
    tmp = []

    clb = calib(sen, "MAGN")

    mag = df.loc[df['ADDR'] == sen, 'MAG']
    mag = mag.values.tolist()

    for i in range(1, len(mag)):
            if (i % 5 == 0): #Average of 5 samples
                    avg.append(round((sum(tmp) / len(tmp)), 2)) #Make average
                    tmp = []
                    tmp.append(float(mag[i]) + clb)
            else:
                tmp.append(float(mag[i]) + clb)
    avg.append(round((sum(tmp) / len(tmp)), 2)) #Last sample

    return avg

def get_samples():
    global uid
    global df

    #Get The CSV File
    try:
        df = pd.read_csv(sys.argv[1])
    except:
        sys.exit("\n\tMust Be a CSV File\n")
    #Extract The Sensors info.
    uid = df.ADDR.unique()

def graph():
    global uid
    global df

    fig = []
    axs = []

    #Get samples raw data and extract all sensors
    get_samples()

    for sen in uid:
        #A graphic for each sensor
        fig = plt.figure()

        #Time
        time = avg_time(sen)

        #Temp and Humd in a same plot
        plt.subplot(2, 1, 1)
        plt.xticks(rotation=20)
        plt.ylabel("Humidity (%) and Temperature (ºC)", weight='bold')
        plt.title("Concrete Corrosion Samples (" + sen + ")", weight='bold', fontsize=15)

        #Temp
        temp = avg_temp(sen)
        plt.plot(time, temp, '--o', color='darkorange')
        #Humd
        humd = avg_humd(sen)
        plt.plot(time, humd, '--o')

        #Magn in a different one
        plt.subplot(2, 1, 2)
        plt.xticks(rotation=20)
        plt.xlabel("Data and Time", weight='bold')
        plt.ylabel("Magnetism (Gauss)", weight='bold')
        #Magn
        mag = avg_mag(sen)
        plt.plot(time, mag, '--o', color='green')

    plt.show()

"""
Estaría guay pedir por consola descripción de los sensores para hacer mejor las gráficas, pero igual se carga la idea de hacerlo parametrizale
"""

#Main -> Let's rock!
if len(sys.argv) > 1:
    graph()
else:
    sys.exit("\n\tPlease, Select The Sample File Name\n")
