#!/usr/bin/python
import spidev
import os
import time
from gpiozero import LED
import numpy as np
import matplotlib.pyplot as plt
import csv


power = LED(16) #PIN für Transitoransteuerung zum ein/ausschalten des Motors (workaround über gpiozero)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
start_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) # der bug mit der zeitüber die settings mit internet einstellen!!


fig, ax = plt.subplots()

# Die Daten hier kann man anpassen:
delay = 1800  #in sek
minval = 610  # vorher durch cal festlegen
maxrep = 50 
# ------------


daten = np.zeros((maxrep, 1))


# für den Motor:
def motor_on(waittime):
    power.on()
    time.sleep(waittime)
    power.off()
 
# auslesen der daten
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
    daten[i, 0] = val
    
    i = i+1
    
    if (val > minval): ##motor an?
        motor_on(5) 
    time.sleep(delay)
    
print(daten) # zur kontrolle während es läuft

# für ein Diagram zur Auswertung
ax.plot(daten)
ax.set_title(start_time)

fig.show()
fig.savefig(start_time + ".pdf", )
#-----------------------


# daten in csv
with open(start_time+'.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(daten)

#------------
    
