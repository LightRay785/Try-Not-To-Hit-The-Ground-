import pygame
from sys import exit
pygame.init()

# Screen Setup
width, height = 550, 630
screen = pygame.display.set_mode((width, height))
fps = 240 #30 for extra easy mode 60 for easy 120 for medium 240 for hard and so on.....
pygame.display.set_caption('Try Not To Hit The Ground!')
birdy = pygame.image.load('birdy.png')
sky = pygame.image.load('background.png')
ground = pygame.image.load('groundimg.jpg')
class Player(pygame.sprite.Sprite):
    def update(self, key): 
        # Jump
        self.velocity += 0.5
        if key[pygame.K_SPACE] and self.rect.y > 0:
            self.velocity = -7
class Bird(Player):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = birdy
        self.rect = self.image.get_rect()
        self.rect.center = 100, 315
        self.velocity = 0

    def update(self, key):
        self.velocity += 0.5
        # Restricts Player to go higher than the screen
        if self.velocity >= 6:
            self.vel = 7
        if self.rect.y < 500: self.rect.y += self.velocity

        # Jump
        if key[pygame.K_SPACE] and self.rect.y > 0:
            self.velocity = -7

clock = pygame.time.Clock()
pygame.transform.scale(ground, (ground.get_width(), 720))

bird = pygame.sprite.GroupSingle()
bird.add(Bird())
x = 0
pygame.time.delay(1000)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(sky, (0,0))
    screen.blit(ground, (0, 520))
    key = pygame.key.get_pressed()
    bird.draw(screen)
    bird.update(key)
    clock.tick(fps)
    pygame.display.flip()
    
