import pygame
from sys import exit
pygame.init()

# Screen Setup
width, height = 551, 630
screen = pygame.display.set_mode((width, height))
fps = 240 #30 for extra easy mode 60 for easy 120 for medium 240 for hard and so on.....
pygame.display.set_caption('Try Not To Hit The Ground!')
flappy_bird = pygame.image.load('birdy.png')
sky = pygame.image.load('background.png')
ground = pygame.image.load('groundimg.jpg')
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = flappy_bird
        self.rect = self.image.get_rect()
        self.rect.center = 100, 315
        self.velocity = 0
    def update(self, key): 
        self.velocity += 0.5
        if self.velocity >= 6:
            self.vel = 7
        if self.rect.y < 500: self.rect.y += self.velocity
        if key[pygame.K_SPACE] and self.rect.y > 0:
            self.velocity = -7

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.rect.x -= 1
        if self.rect.x <= -width: self.kill


clock = pygame.time.Clock()
pygame.transform.scale(ground, (ground.get_width(), 720))

bird = pygame.sprite.GroupSingle()
bird.add(Bird())
x = 0
pipe = pygame.sprite.Group()
pygame.time.delay(1000)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(sky, (0,0))
    screen.blit(ground, (0, 520))
    key = pygame.key.get_pressed()
    pipe.draw(screen)
    pipe.update()
    bird.draw(screen)
    bird.update(key)
    clock.tick(fps)
    pygame.display.flip()
    
