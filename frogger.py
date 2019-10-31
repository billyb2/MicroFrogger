# Add your Python code here. E.g.
from microbit import *

#gotta set variables outside of loop
x = 2;
y = 2;

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


    #300 seems like a decent sensitivity, button controlls are easier though
    
    if xAccel > 300:
        if x < 4:
            x += 1
    
    elif xAccel < -300:
        if x > 0:
            x -= 1
            
    #the only real way to move forward and backwards 
    if yAccel > 300:
        if y < 4:
            y += 1
    
    elif yAccel < -300:
        if y > 0:
            y -= 1
            
            

    #Button controls
    if button_a.is_pressed():
        #if a is pressed, and the x isn't offscreen, move left
        if x > 0:
            x -= 1

    elif button_b.is_pressed():
        #vice versa
        if x < 4:
            x += 1
    
    #clears the screen before showing showing the pixels
    display.show(clear)
    display.set_pixel(x, y, 9)
    
    
