import sys, pygame, time, serial

pygame.init()

size = width, height = 800, 500
speed = [1, 1]
black = 0, 0, 0
map = [
        [7, 0, 0, 10, 0],
        [5, 0, 0, 0, 0],
        [6, 0, 0, 0, 0],
        [3, 0, 0, 0, 0],
        [4, 0, 0 ,0, 0]

]

#s = serial.Serial(
 #    port='COM11',
  #  baudrate=115200
 #)

screen = pygame.display.set_mode(size)

car = pygame.image.load("car1.png")
car = pygame.transform.scale(car, (50, 50))
carrect = car.get_rect()

car2 = pygame.image.load("car2.png")
car2 = pygame.transform.scale(car2, (50, 50))
carrect2 = car2.get_rect()

car3 = pygame.image.load("car3.png")
car3 = pygame.transform.scale(car3, (50, 50))
carrect3 = car3.get_rect()

car4 = pygame.image.load("car4.png")
car4 = pygame.transform.scale(car4, (50, 50))
carrect4 = car4.get_rect()

frog = pygame.image.load("frog.png")
frog = pygame.transform.scale(frog, (50, 50))
frogrect = frog.get_rect()

while True:

  #data = open('data.txt', 'r')
  theData = str(11111111111111111)

        
  map[int(theData[2])][int(theData[3])] = 7
  map[int(theData[4])][int(theData[5])] = 3
  map[int(theData[6])][int(theData[7])] = 4
  map[int(theData[8])][int(theData[9])] = 5
  map[int(theData[10])][int(theData[11])] = 6




  for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()






  for x in range(5):
      for y in range(5):
          if map[x][y] == 7:
              frogrect.x = y * 100
              frogrect.y = x * 100

          elif map[x][y] == 3:
              carrect.x = y * 100
              carrect.y = x * 100

          elif map[x][y] == 4:
              carrect2.x = y * 100
              carrect2.y = x * 100

          elif map[x][y] == 5:
              carrect3.x = y * 100
              carrect3.y = x * 100

          elif map[x][y] == 6:
              carrect4.x = y * 100
              carrect4.y = x * 100

  screen.fill(black)
  screen.blit(frog, frogrect)
  screen.blit(car, carrect)
  screen.blit(car2, carrect2)
  screen.blit(car3, carrect3)
  screen.blit(car4, carrect4)
  pygame.display.flip()
