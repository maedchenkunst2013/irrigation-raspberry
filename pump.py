from gpiozero import LED
from time import sleep

power = LED(16)

power.on()
sleep(5)
power.off()
    
    