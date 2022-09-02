import pygame
from sys import exit
pygame.init()

# Screen Setup
width, height = 550, 630
screen = pygame.display.set_mode((width, height))
fps = 240 #30 for easy mode 60 for medium 120 for hard 240 for extra hard and so on.....
pygame.display.set_caption('Try Not To Hit The Ground!')
birdy = [pygame.image.load('birdy.png'), pygame.image.load('birdy2.png'), pygame.image.load('birdy3.png')]
sky = pygame.image.load('background.png')
ground = pygame.image.load('groundimg.jpg')
class Player(pygame.sprite.Sprite):
    def __init__(self, img1, img2, img3):
        pygame.sprite.Sprite.__init__(self)

        # For the animate() function
        self.imgs = [img1, img2, img3]
        self.image = self.imgs[0]
        self.image_index = 0

    def update(self, key): 
        self.image_index += 1
        self.animate()
        # Jump
        self.velocity += 0.5
        if key[pygame.K_SPACE] and self.rect.y > 0:
            self.velocity = -7

    def animate(self):
        if self.image_index >= 30:
            self.image_index = 0
        self.image = self.imgs[self.image_index // 10]



class Bird(Player):
    def __init__(self):
        Player.__init__(self, birdy[0], birdy[1], birdy[2])
        self.image = birdy[0]
        self.rect = self.image.get_rect()
        self.rect.center = 100, 315
        self.velocity = 0

    def update(self, key):
        self.image_index += 1
        self.animate()

        self.velocity += 0.5
        # Restricts Player to go higher than the screen
        if self.velocity >= 6: self.vel = 7
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
    

    
