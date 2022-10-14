import pygame, sys, time
from debug import debug

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

class Test(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frames = [pygame.image.load(f'frames/{i}.png').convert_alpha() for i in range(1,3)]
        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midleft = (0,360))

        self.rotation = 0
        self.direction = 1
        self.move_speed = 100
        self.animation_speed = 5
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index > len(self.frames)-1:
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def move(self, dt):
        self.pos.x += self.direction * self.move_speed * dt
        self.rect.x = round(self.pos.x)
        if self.rect.right > 1280 or self.rect.left < 0:
            self.direction *= -1

    def rotate(self, dt):
        self.rotation += 50 * dt
        self.image = pygame.transform.rotozoom(self.image,self.rotation,1)

    def update(self, dt):
        self.animate(dt)
        self.move(dt)
        self.rotate(dt), dt

testGroup = pygame.sprite.Group()
testGroup.add(Test())

prevTime = time.time()
while True:
    dt = time.time() - prevTime
    prevTime = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('white')

    testGroup.update(dt)
    testGroup.draw(screen)

    pygame.display.update()
    clock.tick(60)