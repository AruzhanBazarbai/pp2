import pygame
import random
import time
# from pygame.locals import *

#initializing
pygame.init()

#colors
BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

#screen
WIDTH=400
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("game")

#FPS
clock=pygame.time.Clock()
FPS=60

#SPEED AND SCORE
speed_e=5
speed_p=5
SCORE=0

#SOUND-BACKGROUND
sound_back=pygame.mixer.Sound("background.wav")
sound_back.play(-1)

#BACKGROUND AND TEXTS
background=pygame.image.load("Background.png")
# SCORE=0
font=pygame.font.SysFont(None,WIDTH//6)
font_small=pygame.font.SysFont(None,30)
game_over=font.render("GAME OVER!",True,BLACK)

#CLASS FOR ENEMY
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('Enemy.png')
        self.surf=pygame.Surface((50,80))
        self.rect=self.surf.get_rect(center=(random.randint(25,WIDTH-25),0)) #or top=0

    def move(self):
        global SCORE
        self.rect.move_ip(0,speed_e)
        if self.rect.top>HEIGHT:
            SCORE+=1
            self.rect.top=0
            self.rect.center=(random.randint(25,WIDTH-25),0)

    # def draw(self,surface):
    #     surface.blit(self.image,self.rect)

#CLASS FOR PLAYER
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Player.png")
        self.surf=pygame.Surface((50,100))
        self.rect=self.surf.get_rect(center=(WIDTH//2,HEIGHT-100)) #or bottom=500

    def move(self):
        pressed_keys=pygame.key.get_pressed()

        if self.rect.left>0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-speed_p,0)
                
        if self.rect.right<WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(speed_p,0)


    # def draw(self,surface):
    #     surface.blit(self.image,self.rect)
    
P1=Player()
E1=Enemy()

#SPRITE GROUPS
enemies=pygame.sprite.Group()
enemies.add(E1)
all_sprites=pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#CHANGING SPEED PER TIME
time_change=1000
INC_SPEED=pygame.USEREVENT+1
pygame.time.set_timer(INC_SPEED,time_change)

done=False
k=True

#GAME LOOP
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==INC_SPEED: #change the speed
            speed_e+=0.5
        
    # screen.fill(WHITE)
    screen.blit(background,(0,0))
    scores=font_small.render(str(SCORE),True,BLACK)
    screen.blit(scores,(10,10))

    #moves and redraws all sprites
    for x in all_sprites:
        screen.blit(x.image,x.rect)
        x.move()

    #to be run if collision occur between Player and Enemy
    if pygame.sprite.spritecollideany(P1,enemies):
        k=False
        sound_back.stop()
        pygame.mixer.Sound("Crash.wav").play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over,(50,250))
        pygame.display.flip()

        for x in all_sprites:
            x.kill()

        time.sleep(2)
        done=True
        # pygame.quit()

    # P1.update()
    # E1.move()
    # E1.draw(screen)
    # P1.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
if k:
    sound_back.stop()
pygame.quit()