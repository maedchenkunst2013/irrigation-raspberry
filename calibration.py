#!/usr/bin/python
import spidev
import os
import time
import numpy as np

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

daten = np.zeros((15, 1))
i = 0

def readChannel(channel):
    val = spi.xfer2([1,(8+channel)<<4,0])
    data = ((val[1]&3) << 8) + val[2]
    return data

while i < 15:
    ts = i
    val = readChannel(0)
    daten[i, 0] = val
    
    i = i+1
    time.sleep(0.5)

calVal = round(np.mean(daten))

print(calVal)