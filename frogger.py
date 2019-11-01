# Add your Python code here. E.g.
from microbit import *
import math

status = "in game"

#gotta set variables outside of loop
x = 2;
y = 4;

clear = Image(  "00000:"
                "00000:"
                "00000:"
                "00000:"
                "00000")
                
class Car:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        
car = Car(1, 1, 0.5)
                
                
#run on a forever loop
while (status == "in game"):
    
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
        y -= 1
        if y < 0:
            y = 4
            
            

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
    display.set_pixel(math.ceil(car.x), car.y, 4)
    
    car.x += car.speed;

    if car.x < 0:
        car.x = 4
    elif car.x > 4:
        car.x = 0

if car.x == x & car.y == y:
     display.scroll("GAME OVER")
     display.scroll("Do you want to play again?")
     display.scroll("Enter a for yes and b for no")
     if button_b.is_pressed():
            status = "end game"
            
