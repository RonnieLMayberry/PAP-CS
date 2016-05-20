import sys, random, pygame
from pygame.locals import *

pygame.init()

w = 640
h = 480

screen = pygame.display.set_mode((w,h))
morphingShape = pygame.Surface((20,20))
morphingShape.fill((255, 137, 0)) #random colour for testing
morphingRect = morphingShape.get_rect()

# clock object that will be used to make the animation
# have the same speed on all machines regardless
# of the actual machine speed.
clock = pygame.time.Clock()

def ShapeSizeChange(shape, screen):
    x = random.randint(-21, 20)
    w = shape.get_width()
    h = shape.get_height()
    if w + x > 0 and h + x > 0:
        shape = pygame.transform.smoothscale(shape, (w + x, h + x))
    else:
        shape = pygame.transform.smoothscale(shape, (w - x, h - x))
    shape.fill((255, 137, 0))
    rect = shape.get_rect()
    screen.blit(shape, rect)
    return shape


while True:
    # limit the demo to 50 frames per second
    clock.tick( 50 );

    # clear screen with black color
    # THIS IS WHAT WAS REALLY MISSING...
    screen.fill( (0,0,0) )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    morphingShape = ShapeSizeChange(morphingShape, screen)
    pygame.display.update()
