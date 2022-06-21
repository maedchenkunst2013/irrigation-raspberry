# irrigation-raspberry
You can change the parameters in irr.py to fit with your plants. At the moment it will save data on your plants soil moisture as .csv and in a .pdf diagram. For "minval" use callibration in your irrigated soil.

You can use humidity.py and motor.py to test your components.
0 means hight moisture (water is around 100), 1024 is air/dry.


## Components

Raspberry Pi
Pump: 
RUNCCI-YUN Micro Motorpumpe DC 3V-5V (any other will propably do just fine, as long as you use the right power source!)
3m PVC hose

Sensor: 
SBT4447 Sensor Controller Board
YL69 ground sensor

Also used:
MCP3008 8-channel 10-bit analog to digital converter
BC337 Transistor

## Circuit
![circuit-2](https://user-images.githubusercontent.com/20001372/174871070-a0997e31-8145-41c6-a671-d4eb0c4a8c97.png)

## dependencies
spidev, os, time
from gpiozero: LED
numpy, matplotlib.pyplot, csv


## Outstanding problems
- Corrotion of ground sensor could probably be fixed by using it with another transitor to turn it of while not in use. Until then, callibration before every measurement works just fine.

- no live data and limited runtime -> could be solved by reworking the main code
