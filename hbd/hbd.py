import pygame
from pygame import mixer
from time import sleep 
import os 

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)



#image = pygame.image.load('Capture2.PNG')
"""icon = pygame.image.load('anniversaire.png')

pygame.display.set_icon(icon)"""
file ='mikrokosmos.mp3'
pygame.display.set_caption('HBD NCS')
"""mixer.music.load(file)
mixer.music.play()
while pygame.mixer.music.get_busy(): 
  pygame.time.Clock().tick(10)"""
image = pygame.image.load('smile.jpg')
screen.blit(image, (0,0))
pygame.display.update()
sleep(5)