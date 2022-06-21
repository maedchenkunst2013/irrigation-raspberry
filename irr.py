#!/usr/bin/python
import spidev
import os
import time
from gpiozero import LED
import numpy as np
import matplotlib.pyplot as plt
import csv


power = LED(16) #PIN for Transitor to turn on/off your pump (workaround via gpiozero)o)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
start_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())


fig, ax = plt.subplots()

# You can change these parameters:
delay = 1800  #in sek
minval = 610  # determine by calibration
maxrep = 50 
# ------------


dataSen = np.zeros((maxrep, 1))


# for the pump
def motor_on(waittime):
    power.on()
    time.sleep(waittime)
    power.off()
 
# reading data
def readChannel(channel):
    val = spi.xfer2([1,(8+channel)<<4,0])
    data = ((val[1]&3) << 8) + val[2]
    return data

i = 0

#"main" code
while i < maxrep:
    ts = i
    val = readChannel(0)
    print(val)
    dataSen[i, 0] = val
    
    i = i+1
    
    if (val > minval): ##pump on?
        motor_on(5) 
    time.sleep(delay)
    
print(dataSen) # for added control after running

# Diagram for analysis
ax.plot(dataSen)
ax.set_title(start_time)

fig.show()
fig.savefig(start_time + ".pdf", )
#-----------------------


# data in csv
with open(start_time+'.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(dataSen)     #maybe change to .writerows()

#------------
    
