# Add your Python code here. E.g.
from microbit import *
import math
import radio
import random


#gotta set variables outside of loop
x = 2
y = 4

level = 0

radio.on()

clear = Image(  "00000:"
                "00000:"
                "00000:"
                "00000:"
                "00000")
                
class Car:
    def __init__(self):
        self.x = random.randint(0,4)
        self.y = random.randint(0,3)
        self.speed = 0.3
        
car = Car()
car2 = Car()
car3 = Car()
car4 = Car()
mode = False

display.show("1 or 2P")


while mode == False:
    print(mode)
    if button_a.is_pressed():
        display.scroll("3 2 1 go!")
        mode = "1p"
    elif button_b.is_pressed():
        display.scroll("3 2 1 go!")
        mode = "2p"
                
#run on a forever loop
while True:

    #how far the microbit is leaning left or right
    xAccel = accelerometer.get_x()
    yAccel = accelerometer.get_y()
    
    sleep(100)

    if mode == "1p":
        #300 seems like a decent sensitivity, button controlls are easier though
        
        if xAccel > 350:
            if x < 4:
                x += 1
        
        elif xAccel < -350:
            if x > 0:
                x -= 1
                
        #the only real way to move forward and backwards 
        '''   if yAccel > 350:
            if y < 4:
                y += 1
        
        elif yAccel < -350:
            y -= 1
        '''         
        #Button controls
        if button_a.is_pressed():
            #if a is pressed, and the x isn't offscreen, move left
            y -= 1
        elif button_b.is_pressed():
            #vice versa
            if y < 4:
                y += 1
    
        
        if y < 0:
            y = 4
            car.speed += 0.05
            car.y = random.randint(0,3)
            car2.y = random.randint(0,3)
            car3.y = random.randint(0,3)
            car4.y = random.randint(0,3)
            level += 1
            
        
        car.x += car.speed;
        
        display.show(clear)
        display.set_pixel(x, y, 9)
        display.set_pixel(math.floor(car.x), math.floor(car.y), 4)
        
        
        if math.floor(car.x) == x and car.y == y:
            print(x)
            print("car" + str(math.floor(car.x)))
            display.scroll("GAME OVER")
            display.scroll("A to play again")
                    
        if level >= 1:
            #ima just have all the cars move at the speed of the og car for now
            car2.x += car.speed
            display.set_pixel(math.floor(car2.x), math.floor(car2.y), 4)
                
            if math.floor(car2.x) == x and car2.y == y:
                display.scroll("GAME OVER")
                display.scroll("A to play again")    

    
    
        if car.x < 0:
            car.x = 4
        elif car.x > 4:
            car.x = 0
    
        if car2.x < 0:
            car2.x = 4
        elif car2.x > 4:
            car2.x = 0
            
        if car3.x < 0:
            car3.x = 4
        elif car3.x > 4:
            car3.x = 0
            
        if car4.x < 0:
            car4.x = 4
        elif car4.x > 4:
            car4.x = 0
    

