# Add your Python code here. E.g.
from microbit import *


while True:
    xAccel = accelerometer.get_x()
    yAccel = accelerometer.get_y()
    
    display.scroll(xAccel)
    sleep(2000)
