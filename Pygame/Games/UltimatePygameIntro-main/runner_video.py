import pygame
from sys import exit
from random import randint, choice
import random
import string

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        self.player_tt = pygame.image.load('graphics/Player/spritesheet.png').convert_alpha()
        self.player_tt = pygame.transform.scale(self.player_tt, (72,64))

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0


    def player_input(self):
        keys = pygame.key.get_pressed()

        if rk == 'a':
            if keys[pygame.K_a ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'b':
            if keys[pygame.K_b ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'c':
            if keys[pygame.K_c ] and self.rect.bottom >= 300:
                self.gravity = -20
                


        if rk == 'd':
            if keys[pygame.K_d ] and self.rect.bottom >= 300:
                self.gravity = -20
                


        if rk == 'e':
            if keys[pygame.K_e ] and self.rect.bottom >= 300:
                self.gravity = -20
                


        if rk == 'f':
            if keys[pygame.K_f ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'g':
            if keys[pygame.K_g ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'h':
            if keys[pygame.K_h ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'i':
            if keys[pygame.K_i ] and self.rect.bottom >= 300:
                self.gravity = -20
                


        if rk == 'j':
            if keys[pygame.K_j ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'k':
            if keys[pygame.K_k ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'l':
            if keys[pygame.K_l ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'm':
            if keys[pygame.K_m ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'n':
            if keys[pygame.K_n ] and self.rect.bottom >= 300:
                self.gravity = -20
                


        if rk == 'o':
            if keys[pygame.K_o ] and self.rect.bottom >= 300:
                self.gravity = -20
                


        if rk == 'p':
            if keys[pygame.K_p ] and self.rect.bottom >= 300:
                self.gravity = -20
                


        if rk == 'q':
            if keys[pygame.K_q ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'r':
            if keys[pygame.K_r ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 's':
            if keys[pygame.K_s ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 't':
            if keys[pygame.K_t ] and self.rect.bottom >= 300:
                self.gravity = -20
                


        if rk == 'u':
            if keys[pygame.K_u ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'v':
            if keys[pygame.K_v ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'w':
            if keys[pygame.K_w ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'x':
            if keys[pygame.K_x ] and self.rect.bottom >= 300:
                self.gravity = -20
                


        if rk == 'y':
            if keys[pygame.K_y ] and self.rect.bottom >= 300:
                self.gravity = -20
                

        if rk == 'z':
            if keys[pygame.K_z ] and self.rect.bottom >= 300:
                self.gravity = -20
                

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation(self):
        keys = pygame.key.get_pressed()
        if self.rect.bottom < 300:
            self.image = self.player_jump

        elif keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.image = self.player_tt
            self.rect = self.image.get_rect(midbottom = (80, 300))

        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
            self.rect = self.image.get_rect(midbottom = (80, 300))

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "fly":
            fly_1 = pygame.image.load('graphics/Fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/Fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 230
 
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames= [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900,1100), y_pos))

    def animation_state(self):
        if type == "fly":
            self.animation_index += 0.5
            if self.animation_index > len(self.frames):
                self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]

        else:
            self.animation_index += 0.1
            if self.animation_index > len(self.frames):
                self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    current_time = int(pygame.time.get_ticks() /1000) - start_time
    score_surf = font.render(f'Score: {current_time}', False ,(64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def collision_sp():
    if pygame.sprite.spritecollide(player.sprite, obstacle_groub, False):
        obstacle_groub.empty()
        return False
    else: return True

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.1)
bg_music.play(loops = -1)


obstacle_groub = pygame.sprite.Group()

player = pygame.sprite.GroupSingle()
player.add(Player())

player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

sky_surf = pygame.image.load('graphics/Sky.png').convert()
sky_rect = sky_surf.get_rect(topleft = (0,0))

sky_surf2 = pygame.image.load('graphics/Sky.png').convert()
sky_rect2 = sky_surf.get_rect(topleft = (800,0))

ground_surf = pygame.image.load('graphics/ground.png').convert()
ground_rect = ground_surf.get_rect(topleft = (0,300))

ground_surf2 = pygame.image.load('graphics/ground.png').convert()
ground_rect2 = ground_surf.get_rect(topleft = (800,300))

title_surf = font.render("Pixel Runner", False, (64,64,64))
title_rect = title_surf.get_rect(center = (400, 50))

inst_surf = font.render("Press Space To Start", False, (64,64,64))
inst_rect = title_surf.get_rect(midbottom = (340, 350))


alphabet_string = string.ascii_lowercase
alphabets = list(string.ascii_lowercase)
rk = str(alphabets[randint(0,25)])
random_surf = font.render(rk, False, (64,64,64))
random_rect = random_surf.get_rect(center = (40, 50))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:

            if event.type == obstacle_timer:
                obstacle_groub.add(Obstacle(choice(['fly', 'snail', 'snail','snail'])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() /1000)
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True

    if game_active:
        
        screen.blit(sky_surf , sky_rect)
        screen.blit(sky_surf2 , sky_rect2)

        screen.blit(ground_surf , ground_rect)
        screen.blit(ground_surf2 , ground_rect2)
        score = display_score()


        ground_rect.x -= 3
        ground_rect2.x -= 3
        if ground_rect2.x < 1:
            ground_rect2.x = 800
            ground_rect.x = 0

        sky_rect.x -= 1
        sky_rect2.x -= 1
        if sky_rect2.x < 1:
            sky_rect2.x = 800
            sky_rect.x = 0

        player.draw(screen)
        player.update()

        obstacle_groub.draw(screen)
        obstacle_groub.update()

        if player.sprite.gravity < 0:
            rk = str(alphabets[randint(0,25)])

        random_surf = font.render(rk, False, (64,64,64))
        random_rect = random_surf.get_rect(center = (40, 50))
        screen.blit(random_surf, random_rect)

        game_active = collision_sp()
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        score_message = font.render(f"Your Score: {score}", False, (64,64,64))
        score_message_rect = score_message.get_rect(center = (400,330))

        if score > 0: screen.blit(score_message, score_message_rect)
        else: screen.blit(inst_surf, inst_rect)
        screen.blit(title_surf, title_rect)

        rk = str(alphabets[randint(0,25)])

    pygame.display.update()
    clock.tick(60)