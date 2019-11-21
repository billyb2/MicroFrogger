# Add your Python code here. E.g.
from microbit import *
import math
import radio
import random

radio.on()

#gotta set variables outside of loop
x = 2
y = 4

x2 = 4
y2 = 4
level = 0

runOnce = 0

clear = Image(  "00000:"
                "00000:"
                "00000:"
                "00000:"
                "00000")
                
class Car:
    def __init__(self):
        self.x = random.randint(0,4)
        self.y = random.randint(1,3)
        self.speed = 0.3
        
car = Car()
car2 = Car()
car3 = Car()
car4 = Car()
mode = False

startedRadio = False


display.show("1 or 2P")


while mode == False:
    if button_a.is_pressed():
        display.scroll("3 2 1 go!")
        mode = "1p"
    elif button_b.is_pressed():
        mode = "2p"

        
        
        
        
        
        

                

            
            
            
            
            
            

                
#run on a forever loop
while True:
    sleep(100)
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
        
        
    if level >= 3:
        #ima just have all the cars move at the speed of the og car for now
        car2.x += car.speed
        display.set_pixel(round(car2.x), round(car2.y), 4)
                
        if round(car2.x) == x and car2.y == y:
            display.scroll("GAME OVER")
            display.scroll("A to play again")  
        #I'll nest the if statements to save ram (like this graphical intense needs)
        if level >= 6:
            car3.x += car.speed
            display.set_pixel(round(car3.x), round(car3.y), 4)
                    
            if round(car3.x) == x and car3.y == y:
                display.scroll("GAME OVER")
                display.scroll("A to play again")  
                
            if level >= 9:
                car4.x += car.speed
                display.set_pixel(round(car4.x), round(car4.y), 4)
                        
                if round(car4.x) == x and car4.y == y:
                    display.scroll("GAME OVER")
                    display.scroll("A to play again")
                    
                    
                
        #how far the microbit is leaning left or right
        xAccel = accelerometer.get_x()
        yAccel = accelerometer.get_y()
                            
        if xAccel > 350:
            if x < 4:
                x += 1
                        
        elif xAccel < -350:
            if x > 0:
                x -= 1
        #Button controls
        if button_a.is_pressed():
            #if a is pressed, and the x isn't offscreen, move left
            y -= 1
        elif button_b.is_pressed():
            #vice versa
            if y < 4:
                y += 1
    
    
    if mode == "1p":
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
        display.set_pixel(round(car.x), round(car.y), 4)
        if round(car.x) == x and car.y == y:
            display.scroll("GAME OVER")
            display.scroll("A to play again")

    
    elif mode == "2p":
        
        
        radio.on()
        while True:
            #Button controls
            if button_a.is_pressed():
                #if a is pressed, and the x isn't offscreen, move left
                if y > 0:
                    y -= 1
            elif button_b.is_pressed():
                #vice versa
                if y < 4:
                    y += 1
                    
                        
                    
                    
                        

            if y == 0 or y2 == 0:
                if y == 0 or y2 == 0:
                    time = running_time()

                    if runOnce == 0:
                        runOnce = 1
                        targetTime = time + 5000
                    
                    if time >= targetTime:
                            if y == 0 and y2 != 0:
                                print("Player 1 wins!")
                                
                            elif y != 0 and y2 == 0:
                                print("Player 2 wins!")
                                
                            elif y == 0 and y2 == 0:
                                level += 1
                                car.speed += 0.05
                                car.y = random.randint(0,3)
                                car2.y = random.randint(0,3)
                                car3.y = random.randint(0,3)
                                car4.y = random.randint(0,3)
                                level += 1
                                
                                
            
                                
                    
                    
                    
                    
            car.x += car.speed;
            
            display.show(clear)
            display.set_pixel(x, y, 9)
            display.set_pixel(round(car.x), round(car.y), 4)
    

            
            
            radio.send(str(x) + str(y))
            radioData = radio.receive()
            
            if radioData != None:
                x2 = str(radioData)[0]
                y2 = str(radioData)[1]
                print(radioData)
                
            display.show(clear)
            display.set_pixel(x, y, 9)
            display.set_pixel(int(x2), int(y2), 9)
            display.set_pixel(round(car.x), round(car.y), 4)
