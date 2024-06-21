import pygame
import sys

#initialize the game 
pygame.init()

# setup a display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# main game loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    pygame.display.flip()
