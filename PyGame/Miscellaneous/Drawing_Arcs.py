'''
Created on Apr 9, 2015

@author: mayberryr
'''
# Drawing Arcs
# Python 3.2

import math
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Drawing Arcs")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
            
    screen.fill((255, 255, 255))
    
    # draw the arc
    color = 0, 0, 255
    position = 25, 50, 175, 175
    start_angle = math.radians(0)
    end_angle = math.radians(361)
    width = 7
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    # draw the second arc
    color = 0, 0, 0
    position = 225, 50, 175, 175
    start_angle = math.radians(0)
    end_angle = math.radians(361)
    width = 7
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    # draw the third arc
    color = 255, 0, 0
    position = 425, 50, 175, 175
    start_angle = math.radians(0)
    end_angle = math.radians(361)
    width = 7
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    # draw the fourth arc
    color = 255, 255, 0
    position = 125, 150, 175, 175
    start_angle = math.radians(0)
    end_angle = math.radians(361)
    width = 7
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    # draw the fifth arc
    color = 35, 140, 35
    position = 325, 150, 175, 175
    start_angle = math.radians(0)
    end_angle = math.radians(361)
    width = 7
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
    
    pygame.display.update()
