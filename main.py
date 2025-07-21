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
    def __init__(self, x, y, image, mozkomor_type):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # typy mozkomorů
        self.type = mozkomor_type

        # nastavení náhodného směru mozkomora
        self.x = random.choice([-1, 1])
        self.y = random.choice([-1, 1])
        self.speed = random.randint(1, 5)

    # kód který je volán stále dokola
    def update(self):
        # pohyb mozkomora
        self.rect.x += self.x * self.speed
        self.rect.y += self.y * self.speed

        # odraz mozkomora
        if self.rect.left < 0 or self.rect.right > width:
            self.x = -1 * self.x
        if self.rect.top < 100 or self.rect.bottom > height - 100:
            self.y = -1 * self.y


# skupina mozkomorů
mozkomor_group = pygame.sprite.Group()
one_mozkomor = mozkomor(500, 500, pygame.image.load("img/mozkomor-modry.png"), 0)
mozkomor_group.add(one_mozkomor)
one_mozkomor = mozkomor(500, 500, pygame.image.load("img/mozkomor-zeleny.png"), 1)
mozkomor_group.add(one_mozkomor)
one_mozkomor = mozkomor(500, 500, pygame.image.load("img/mozkomor-ruzovy.png"), 2)
mozkomor_group.add(one_mozkomor)
one_mozkomor = mozkomor(500, 500, pygame.image.load("img/mozkomor-zluty.png"), 3)
mozkomor_group.add(one_mozkomor)

###################HLAVNÍ CYKLUS#########################
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # vyplnění plochy
    screen.fill((0, 0, 0))

    # updatujeme skupinu¨
    mozkomor_group.draw(screen)
    mozkomor_group.update()


    # update obrazovky
    pygame.display.update()

    # spomalovaní cyklu 
    clock.tick(fps)



# ukončení hry 
pygame.quit