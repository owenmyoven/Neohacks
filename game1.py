### The person needs a starting point and a destination


import pygame
from pygame.locals import *
from random import randint,uniform
from math import sqrt, sin
from time import daylight, time 
import sys, os

pygame.init()

FPS = 60
clock = pygame.time.Clock()
### Colors  
WHITE = (255,255,255)
DARK_GRAY = (20,20,20)
WIDTH, HEIGHT = 1920, 1080
SPEED = 5
BACKGROUND_COLOR = WHITE

DISPLAY_SURF = pygame.display.set_mode((WIDTH,HEIGHT))
DISPLAY_SURF.fill(WHITE)

pygame.display.set_caption("Elevator")
background = pygame.Surface((WIDTH,HEIGHT))
background.fill(BACKGROUND_COLOR)






class Person(pygame.sprite.Sprite):
    def __init__(self,x,y):
        ##super().__init__() 
        self.image = pygame.image.load("person.png")
        
        self.x = x
        self.y = y
        self.SPEED = 5
        
        self.surf = pygame.Surface((24, 24))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect(center = (x, y))
       
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        
        
        if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
              
        if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Elevator():
    def __init__(self,x,y,final_y):
        ##super().__init__()
        
        self.x = x
        self.y = y

        self.surf = pygame.Surface((0,0))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect(center = (x, y))
    
    def update():
        pygame.draw.rect(DISPLAY_SURF,DARK_GRAY,(200,150,100,50))
        

people = []
elevators = []

for i in range(1):
  people.append(Person(300,900))
for i in range(1):
    elevators.append(Elevator(1100,900,100))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

    DISPLAY_SURF.blit(background, (0,0))
    
    try:
      for person in people:
        DISPLAY_SURF.blit(person.image, person.rect)
        person.update() 
      for elevator in elevators:
        DISPLAY_SURF.blit(elevator.surf, elevator.rect)
        elevator.update() 
    
    except:
      pass

    pygame.display.update()
    clock.tick(FPS)

### Bruh
### Second Bruh
