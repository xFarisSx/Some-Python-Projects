import pygame, sys
from pygame.math import Vector2
import random

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.coll = False

        self.head_up = pygame.image.load('Snake-main/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Snake-main/Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Snake-main/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Snake-main/Graphics/head_left.png').convert_alpha()
            
        self.tail_up = pygame.image.load('Snake-main/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Snake-main/Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Snake-main/Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Snake-main/Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Snake-main/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Snake-main/Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Snake-main/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Snake-main/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Snake-main/Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Snake-main/Graphics/body_bl.png').convert_alpha()
        
        self.crunch_sound = pygame.mixer.Sound('Snake-main/Sound/crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == (len(self.body)-1):
                screen.blit(self.head,block_rect)

            elif index == 0:
                screen.blit(self.tail,block_rect)

            else:
                previous_block =   block - self.body[index - 1]
                next_block =  block - self.body[index + 1] 
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == 1 and next_block.y == 1 or next_block.x == 1 and previous_block.y == 1:
                        screen.blit(self.body_tl, block_rect)

                    elif previous_block.x == -1 and next_block.y == 1 or next_block.x == -1 and previous_block.y == 1:
                        screen.blit(self.body_tr, block_rect)

                    elif previous_block.x == 1 and next_block.y == -1 or next_block.x == 1 and previous_block.y == -1:
                        screen.blit(self.body_bl, block_rect)

                    elif previous_block.x == -1 and next_block.y == -1 or next_block.x == -1 and previous_block.y == -1:
                        screen.blit(self.body_br, block_rect)



    def update_head_graphics(self):
        head_relation = self.body[-2] - self.body[-1]
        if head_relation == Vector2(-1,0):
            self.head = self.head_right
        elif head_relation == Vector2(1,0):
            self.head = self.head_left
        elif head_relation == Vector2(0,-1):
            self.head = self.head_down
        elif head_relation == Vector2(0,1):
            self.head = self.head_up

    def update_tail_graphics(self):
        tail_relation = self.body[0] - self.body[1]
        if tail_relation == Vector2(-1,0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(1,0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0,1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0,-1):
            self.tail = self.tail_up


        
    def move_snake(self):
        if not self.coll:
            body_copy = self.body[1:]
        else:
            body_copy = self.body
        body_copy.append(body_copy[-1] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.coll = True
    def notadd(self):
        self.coll = False


    
    def play_sound(self):
        self.crunch_sound.play()
class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x,self.y)


    def draw_fruit(self):
        global fruit_rect
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x,self.y)
        for block in main_game.snake.body:
            if self.pos == block:
                main_game.fruit.randomize()


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[-1]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_sound()
        else:
            self.snake.notadd()

    

    def check_fail(self):
        global fail
        if self.snake.body:
            head = self.snake.body[-1]
            if not 0 <= head.x < 20 or not 0<= head.y < cell_number:
                fail = True
                self.game_over()
            nohead = self.snake.body[:-1]
            for body in nohead:
                if body == head:
                    fail = True
                    self.game_over()

    def game_over(self):
        global game_active
        game_active = False

    def draw_grass(self):
        grass_color = (167,209,61)

        for row in range(cell_number):
            if row%2 == 0:
                for col in range(cell_number):
                    if col %2==0:
                        grass_rect = pygame.Rect(40*col, 40*row, 40,40)
                        pygame.draw.rect(screen ,grass_color, grass_rect)

            else:
                for col in range(cell_number):
                    if col%2 != 0:
                        grass_rect = pygame.Rect(40*col, 40*row, 40,40)
                        pygame.draw.rect(screen ,grass_color, grass_rect)

    def draw_score(self):
        global score_text
        score_text = str(len(self.snake.body) - 3)
        score_surface = font.render(score_text,True , (56,74,12)) 
        score_x = cell_size * cell_number - 60
        score_y = cell_number * cell_size -40
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))

        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width+ score_rect.width+ 8, apple_rect.height)
        pygame.draw.rect(screen, (164, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56,74,12), bg_rect,2)


pygame.mixer.pre_init(44100, -16,2,512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
title = pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
apple = pygame.image.load('Snake-main/Graphics/apple.png').convert_alpha()
font = pygame.font.Font('Snake-main/Font/PoetsenOne-Regular.ttf', 25)
game_active = False
restart_s = font.render('Start', False, (255,255,255))
restart_r = restart_s.get_rect(center = (400,400))
current_time = 0
best_score = 0
font2 = pygame.font.Font('Snake-main/Font/PoetsenOne-Regular.ttf', 50)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,135)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            sys.exit()

        if game_active:
            if event.type == SCREEN_UPDATE and game_active:

                main_game.update()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)

        if not game_active:
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_r.collidepoint(event.pos):
                    game_active = True
                    main_game.snake.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
                    main_game.snake.direction = Vector2(1,0)
                    main_game.coll = False
                    main_game.fruit.randomize()
                elif quit_r.collidepoint(event.pos):
                    quit()
                    exit()

    if game_active:
        screen.fill((175, 215, 70))
        
        current_time = pygame.time.get_ticks()
        main_game.draw_elements()

        if int(score_text) > best_score:
            best_score = int(score_text)
    if not game_active:


        screen.fill((0,160,180))
        menu_rect = pygame.Rect(100,200,600,400)
        pygame.draw.rect(screen, (0, 200,200),menu_rect,0,5)
        button_r = pygame.Rect(350, 380, 100, 50)
        pygame.draw.rect(screen, (0,160,180),button_r, 0, 10)
        screen.blit(restart_s, restart_r)
        if current_time > 0:
            restart_s = font.render('Restart', False, (255,255,255))
            restart_r = restart_s.get_rect(center = (400,400))
            screen.blit(restart_s, restart_r)
            score_text2 = font.render(f'Score: {score_text}', True,(255,255,255))
            screen.blit(score_text2, (110, 235))
            best_score_s = font.render(f'Best Score: {best_score}', True,(255,255,255))
            screen.blit(best_score_s, (110, 203))
            

        quit_r = pygame.Rect(350, 440, 100,50)
        pygame.draw.rect(screen,(0,160,180),quit_r,0,10)
        quit_text = font.render('Exit', True,(255,255,255))
        screen.blit(quit_text, (375, 445))

        game_name = font2.render('Snake Game',True,(255,255,255))
        game_name_r = game_name.get_rect(center = (400, 330))
        pygame.draw.rect(screen,(0,160,180),game_name_r,0,10)
        screen.blit(game_name, (260,300))
    pygame.display.update()
    clock.tick(60)
    