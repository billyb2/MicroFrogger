# Add your Python code here. E.g.
from microbit import *
import math
import radio
import random

#gotta set variables outside of loop
x = 2;
y = 4;

radio.on()

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
        
car = Car(0, random.randint(0,3), 0.3)
                
                
#run on a forever loop
while True:
    
    #how far the microbit is leaning left or right
    xAccel = accelerometer.get_x()
    yAccel = accelerometer.get_y()
    
    sleep(100)


    #300 seems like a decent sensitivity, button controlls are easier though
    
    if xAccel > 350:
        if x < 4:
            x += 1
    
    elif xAccel < -350:
        if x > 0:
            x -= 1
            
    #the only real way to move forward and backwards 
    if yAccel > 350:
        if y < 4:
            y += 1
    
    elif yAccel < -350:
        y -= 1
            
    radio.send(str(x))


    #Button controls
    if button_a.is_pressed():
        #if a is pressed, and the x isn't offscreen, move left
        y -= 1
        print(y)
        print("car:" + str(car.y))
    elif button_b.is_pressed():
        #vice versa
        if y < 4:
            y += 1
        print(y)
        print("car:" + str(car.y))
        
    otherPlayerX = radio.receive()
    otherPlayerX = str(otherPlayerX)
    # otherPlayerY = int(otherPlayerX)
    
    if y < 0:
        y = 4
    
    car.x += car.speed;
    
    display.show(clear)
    display.set_pixel(x, y, 9)
    display.set_pixel(math.floor(car.x), math.floor(car.y), 4)
    
    
    if math.floor(car.x) == x and car.y == y:
        print(x)
        print("car" + str(math.floor(car.x)))
        display.scroll("GAME OVER")
        display.scroll("A to play again")


    if car.x < 0:
        car.x = 4
    elif car.x > 4:
        car.x = 0
        
        

            
