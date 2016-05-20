'''
Created on Apr 10, 2015

@author: mayberryr
'''
import pygame

pygame.init()

RED = (255, 0, 0)
WHITE = (255, 255, 255)

size = [410, 110]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Drawing Ellipse")

done = False
clock = pygame.time.Clock()

while not done:
    
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(WHITE)
    
    pygame.draw.ellipse(screen, RED, [5, 5, 400, 100])
    
    pygame.display.flip()   

pygame.quit()