# Add your Python code here. E.g.
from microbit import *


while True:
    xAccel = accelerometer.get_x()
    yAccel = accelerometer.get_y()
    
    x = 1;
    y = 1;
    
    while 1 == 1:
        if xAccel > 20:
            x = x + 1
    
        elif xAccel < -20:
            x = x - 1
        
        
        display.set_pixel(x, y, 9)
    
    sleep(2000)
