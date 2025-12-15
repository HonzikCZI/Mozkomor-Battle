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


# === CLASS ===
class game:
    def __init__(self, our_player, group_of_mozkomors):
        self.score = 0
        self.round_number = 1

        self.round_time = 0
        self.slow_down_cycle = 0

        self.our_player = our_player
        self.group_of_mozkomors = group_of_mozkomors

        # yhudba v pozadi
        pygame.mixer.music.load("music/bg-music-hp.wav")
        pygame.mixer.music.play(-1, 0.0)

        # fonty
        self.potter_font = pygame.font.Font("font/Harry.ttf", 24)

        # obrazky
        blue_image = pygame.image.load("img/mozkomor-modry.png")
        blue_image = pygame.transform.scale("blue_image", (500, 500))
        green_image = pygame.image.load("img/mozkomor-zeleny.png")
        yellow_image = pygame.image.load("img/mozkomor-zluty.png")
        purple_image = pygame.image.load("img/mozkomor-ruzovy.png")
        self.mozkomors_image = [blue_image, green_image, purple_image, yellow_image]

        # generujeme mozkomora
        self.mozkomor_catch_type = random.randint(0, 3)
        self.mozkomor_catch_image = self.mozkomors_image[self.mozkomor_catch_type]
        self.mozkomor_catch_image_rect = self.mozkomor_catch_image.get_rect()
        self.mozkomor_catch_image_rect.centerx = width // 2
        self.mozkomor_catch_image_rect.top = 25

    # kód který je volán stale dokola
    def update(self):
        self.slow_down_cycle += 1
        if self.slow_down_cycle == fps:
            self.round_time += 1
            self.slow_down_cycle = 0
            print(self.round_time)

        # kontrola kolioze
        self.check_collision()

    # vykresluje vše ve hře
    def draw(self):
        dark_yellow = pygame.Color("#938f0c")
        blue = (21, 31, 217)
        green = (24, 194, 38)
        purple = (195, 23, 189)
        yellow = (195, 181, 23)

        colors = [blue, green, purple, yellow]

        # nastaveni textu
        catch_text = self.potter_font.render("Catch this demetor", True, dark_yellow)
        catch_text_rect = catch_text.get_rect()
        catch_text_rect.centerx = width // 2
        catch_text_rect.top = 5

        score_text = self.potter_font.render(f"Score: {self.score}", True, dark_yellow)
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (10, 4)

        lives_text = self.potter_font.render(f"Lives: {self.our_player.lives}", True, dark_yellow)
        lives_text_rect = lives_text.get_rect()
        lives_text_rect.topleft = (10, 30)

        round_text = self.potter_font.render(f"Round: {self.round_number}", True, dark_yellow)
        round_text_rect = round_text.get_rect()
        round_text_rect.topleft = (10, 60)

        time_text = self.potter_font.render(f"Time: {self.round_time}", True, dark_yellow)
        time_text_rect = time_text.get_rect()
        time_text_rect.topright = (width - 5, 4)

        save_zone_text = self.potter_font.render(f"Save zone: {self.our_player.enter_safe_zone}", True, dark_yellow)
        save_zone_text_rect = save_zone_text.get_rect()
        save_zone_text_rect.topright = (width - 5, 30)


        # bliting
        screen.blit(catch_text, catch_text_rect)
        screen.blit(score_text, score_text_rect)
        screen.blit(lives_text, lives_text_rect)
        screen.blit(round_text, round_text_rect)
        screen.blit(time_text, time_text_rect)
        screen.blit(save_zone_text, save_zone_text_rect)
        screen.blit(self.mozkomor_catch_image, self.mozkomor_catch_image_rect)

        # Tvary
        pygame.draw.rect(screen, colors[self.mozkomor_catch_type], (0, 100, width, height - 200), 4)

    # kontroluje kolizi
    def check_collision(self):
        collided_mozkomor = pygame.sprite.spritecollideany(self.our_player, self.group_of_mozkomors)

        if collided_mozkomor:
            if collided_mozkomor.type == self.mozkomor_catch_type:
                self.score += 10 *self.round_number
                print("joo")
                collided_mozkomor.remove(self.group_of_mozkomors)

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
        super().__init__()
        self.image = pygame.image.load("img/potter-icon.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height

        self.lives = 5
        self.enter_safe_zone = 3
        self.speed = 8

        self.catch_sound = pygame.mixer.Sound("music/expecto-patronum.mp3")
        self.catch_sound.set_volume(0.1)
        self.wrong_sound = pygame.mixer.Sound("music/wrong.wav")
        self.wrong_sound.set_volume(0.1)

    # kód který se volá stále dokola
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < height - 100:
            self.rect.y += self.speed

    # návrat do bezpečné zóny
    def back_to_safe_zone(self):
        if self.enter_safe_zone > 0:
            self.enter_safe_zone -= 1
            self.rect.bottom = height

    # vrací hráče do výhozí pozice
    def reset(self):
        self.rect.centerx = width // 2
        self.rect.bottom = height


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

# === INICIALIZACE ===

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

# skupina hracu
player_group = pygame.sprite.Group()
one_player = player()
player_group.add(one_player)

# objekt game
my_game = game(one_player, mozkomor_group)

# === HLAVNÍ CYKLUS ===

lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                one_player.back_to_safe_zone()

    # vyplnění plochy
    screen.fill((0, 0, 0))

    # updatujeme skupinu mozkomoru
    mozkomor_group.draw(screen)
    mozkomor_group.update()
    # updatujeme skupinu hracu
    player_group.draw(screen)
    player_group.update()
    # updatujeme ojekt podle classy game
    my_game.update()
    my_game.draw()

    # update obrazovky
    pygame.display.update()

    # spomalovaní cyklu
    clock.tick(fps)


# ukončení hry
pygame.quit