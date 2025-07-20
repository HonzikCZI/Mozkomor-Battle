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

# classy
class game:
    def __init__(self):
        pass

    # kód který je volán stale dokola
    def update(self):
        pass

    # vykresluje vše ve hře
    def draw(self):
        pass

    # kontroluje kolizi
    def check_collision(self):
        pass

    # zahají nové kolo
    def start_new_round(self):
        pass

    # vybírá nového mozkomora
    def choose_new_target(self):
        pass

    # pozastavení hry
    def pause_game(self):
        pass

    # resetuje hru
    def reset_game(self):
        pass


class player(pygame.sprite.Sprite):
    def __init__(self):
        pass

    # kód který se volá stále dokola
    def updates(self):
        pass

    # návrat do bezpečné zóny
    def back_to_safe_zone(self):
        pass

    # vrací hráče do výhozí pozice
    def reset(self):
        pass


class mozkomor(pygame.sprite.Sprite):
    def __init__(self):
        pass

    # kód který je volán stále dokola
    def update(self):
        pass


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