import pygame
import random

# inicializace hry
pygame.init()

# nastavení obrazovky
width = 1200
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MOZKOMOR BATTLE")

# nastavení hry
fps = 60
clock = pygame.time.Clock()


###################HLAVNÍ CYKLUS#########################
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False


    # update obrazovky
    pygame.display.update()

    # spomalovaní cyklu 
    clock.tick(fps)



# ukončení hry 
pygame.quit