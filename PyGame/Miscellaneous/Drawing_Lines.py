# Drawing Lines
# Python 3.2
import time
import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0,0,0))
    
    #draw the lines
    color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    
    lines = 0
    while lines < 1:
        pygame.draw.line(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(0, 500), random.randint(0, 500)), (random.randint(0, 500), random.randint(0, 500)), random.randint(1, 4))
        pygame.display.update()
        lines + 1
