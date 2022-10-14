import pygame, sys
from random import randint

class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('graphics/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        

    def update(self):
        self.input()
        if self.direction.magnitude() != 0:
            self.direction.normalize()
        self.rect.center += self.direction * self.speed

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0]//2
        self.half_h = self.display_surface.get_size()[1] // 2

        self.camera_border = {'left': 200, 'right':200,'top':100,'bottom':100}
        l = self.camera_border['left']
        t = self.camera_border['top']
        w = self.display_surface.get_size()[0] - (self.camera_border['left'] + self.camera_border['right'])
        h = self.display_surface.get_size()[1] - (self.camera_border['bottom'] + self.camera_border['top'])
        self.camera_rect = pygame.Rect(l,t,w,h)

        self.ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
        self.ground_rect = self.ground_surface.get_rect(topleft = (0,0))

        self.keyboard_speed = 5
        self.mouse_speed = 0.4

    def center_target_camera(self,target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def box_target_camera(self,target):

        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - self.camera_border['left']
        self.offset.y = self.camera_rect.top - self.camera_border['top']

    # def keyboard_control(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_a]:
    #         self.offset.x -= self.keyboard_speed
    #     if keys[pygame.K_d]:
    #         self.offset.x += self.keyboard_speed
    #     if keys[pygame.K_w]:
    #         self.offset.y -= self.keyboard_speed
    #     if keys[pygame.K_s]:
    #         self.offset.y += self.keyboard_speed

    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.camera_rect.x -= self.keyboard_speed
        if keys[pygame.K_d]:
            self.camera_rect.x += self.keyboard_speed
        if keys[pygame.K_w]:
            self.camera_rect.y -= self.keyboard_speed
        if keys[pygame.K_s]:
            self.camera_rect.y += self.keyboard_speed

        self.offset.x = self.camera_rect.left - self.camera_border['left']
        self.offset.y = self.camera_rect.top - self.camera_border['top']

    def mouse_control(self):
        mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_offset_vector = pygame.math.Vector2()

        left_border = self.camera_border['left']
        top_border= self.camera_border['top']
        right_border = self.display_surface.get_size()[0] - self.camera_border['right']
        bottom_border = self.display_surface.get_size()[1] - self.camera_border['bottom']

        if top_border < mouse.y < bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector.x = mouse.x - left_border
                pygame.mouse.set_pos((left_border,mouse.y))
            if mouse.x > right_border:
                mouse_offset_vector.x = mouse.x - right_border
                pygame.mouse.set_pos((right_border,mouse.y))

        elif mouse.y < top_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(left_border, top_border)
                pygame.mouse.set_pos((left_border, top_border))
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(right_border, top_border)
                pygame.mouse.set_pos((right_border, top_border))
        elif mouse.y > bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(left_border, bottom_border)
                pygame.mouse.set_pos((left_border, bottom_border))
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(right_border, bottom_border)
                pygame.mouse.set_pos((right_border, bottom_border))


        if left_border < mouse.x < right_border:
            if mouse.y < top_border:
                mouse_offset_vector.y = mouse.y - top_border
                pygame.mouse.set_pos((mouse.x,top_border))
            if mouse.y > bottom_border:
                mouse_offset_vector.y = mouse.y - bottom_border
                pygame.mouse.set_pos((mouse.x,bottom_border))
            
        self.offset += mouse_offset_vector* self.mouse_speed


    def custom_draw(self,player):

        self.center_target_camera(player)
        # self.box_target_camera(player)
        # self.keyboard_control()
        # self.mouse_control()

        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surface,ground_offset)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)



pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.event.set_grab(True)

camera_group = CameraGroup()
player = Player((640,360), camera_group)

for i in range(20):
    randomx = randint(1000,2000)
    randomy = randint(1000,2000)
    Tree((randomx,randomy),camera_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill('#71ddee')

    camera_group.update()
    camera_group.custom_draw(player)

    pygame.display.update()
    clock.tick(60)