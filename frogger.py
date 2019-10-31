# Add your Python code here. E.g.
from microbit import *

#gotta set variables outside of loop
x = 0;
y = 0;

clear = Image(  "00000:"
                "00000:"
                "00000:"
                "00000:"
                "00000")
                
                
#run on a forever loop
while True:
    
    #how far the microbit is leaning left or right
    xAccel = accelerometer.get_x()
    yAccel = accelerometer.get_y()
    
    sleep(100)


    #250 seems like a decent sensitivity, button controlls are easier though
    
    if xAccel > 300:
        if x < 4:
            x += 1
    
    elif xAccel < -300:
        if x > 0:
            x -= 1
            
            

    #Button controls
    if button_a.is_pressed():
        #if a is pressed, and the x isn't offscreen, move left
        if x > 0:
            x -= 1

    elif button_b.is_pressed():
        #vice versa
        if x < 4:
            x += 1
    
    display.show(clear)
    display.set_pixel(x, y, 9)
    
    
