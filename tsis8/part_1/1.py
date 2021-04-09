import pygame
import random

pygame.init()
WIDTH=400
HEIGHT=600
BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("game_1")
clock=pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('Enemy.png')
        self.surf=pygame.Surface((50,80))
        self.rect=self.surf.get_rect(center=(random.randint(25,375),0))

    def move(self):
        self.rect.move_ip(0,10)
        if self.rect.bottom>600:
            self.rect.top=0
            self.rect.center=(random.randint(25,375),0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Player.png")
        self.surf=pygame.Surface((50,100))
        self.rect=self.surf.get_rect(bottom=HEIGHT)

    def update(self,WIDTH):
        pressed_keys=pygame.key.get_pressed()

        if self.rect.left>0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
                
        # if self.rect.right < WIDTH:
        #     if pressed_keys[K_RIGHT]:
        #         self.rect.move_ip(5,0)


    def draw(self,surface):
        surface.blit(self.image,self.rect)
    
P1=Player()
E1=Enemy()
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(WHITE)
    P1.update(WIDTH)
    E1.move()
    
    E1.draw(screen)
    P1.draw(screen)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()