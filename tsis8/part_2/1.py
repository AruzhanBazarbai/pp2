import pygame
import random
import time

#INITIALIZING
pygame.init()

#COLORS
BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

#SCREEN
WIDTH=400
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("game")

#FPS
clock=pygame.time.Clock()
FPS=60

#SPEED AND SCORE
speed_e=random.randint(1,5)
speed_p=5
speed_m=5
SCORE_E=0
SCORE_M=0

#SOUND-BACKGROUND
sound_back=pygame.mixer.Sound("background.wav")
sound_back.play(-1)

#BACKGROUND AND TEXTS
background=pygame.image.load("Background.png")
font=pygame.font.SysFont(None,WIDTH//6)
font_small=pygame.font.SysFont(None,30)
game_over=font.render("GAME OVER!",True,BLACK)
font_money=pygame.font.SysFont(None,30)
font_score=pygame.font.SysFont(None,WIDTH//6)

#CLASS FOR ENEMY
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('Enemy.png')
        self.surf=pygame.Surface((50,80))
        self.rect=self.surf.get_rect(center=(random.randint(25,WIDTH-25),0)) #or top=0

    def move(self):
        global SCORE_E
        global speed_e
        self.rect.move_ip(0,speed_e)
        if self.rect.top>HEIGHT:
            SCORE_E+=1
            speed_e=random.randint(1,5)
            self.rect.top=0
            self.rect.center=(random.randint(25,WIDTH-25),0)

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

        global p_left,p_right,p_top,p_bottom
        p_left=self.rect.left
        p_right=self.rect.right
        p_top=self.rect.top
        p_bottom=self.rect.bottom


#CLASS FOR COINS
class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Money.png")
        self.surf=pygame.Surface((20,20))
        self.rect=self.surf.get_rect(center=(random.randint(20,WIDTH-20),0))
        self.change=0

    def move(self):
        global SCORE_M
        self.change=SCORE_M

        self.rect.move_ip(0,speed_m)
        if self.rect.right>=p_left and self.rect.right<=p_right:
            if self.rect.bottom>=p_top and self.rect.bottom<=p_bottom:
                pygame.mixer.Sound("Adding_money.wav").play()
                SCORE_M+=1
            elif self.rect.top>=p_top and self.rect.top<=p_bottom:
                pygame.mixer.Sound("Adding_money.wav").play()
                SCORE_M+=1
                

        elif self.rect.left>=p_left and self.rect.left<=p_right:
            if self.rect.bottom>=p_top and self.rect.bottom<=p_bottom:
                pygame.mixer.Sound("Adding_money.wav").play()
                SCORE_M+=1
            elif self.rect.top>=p_top and self.rect.top<=p_bottom:
                pygame.mixer.Sound("Adding_money.wav").play()
                SCORE_M+=1

        if SCORE_M!=self.change or self.rect.top>HEIGHT:
            self.rect.top=0
            self.rect.center=(random.randint(20,WIDTH-20),10)

    
P1=Player()
E1=Enemy()
M1=coin()

#SPRITE GROUPS
enemies=pygame.sprite.Group()
enemies.add(E1)
all_sprites=pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)

#CHANGING SPEED PER TIME
# time_change=1000
# INC_SPEED=pygame.USEREVENT+1
# pygame.time.set_timer(INC_SPEED,time_change)

done=False
k=True

#GAME LOOP
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        # if event.type==INC_SPEED: #change the speed
        #     speed_e+=0.5
        
    # screen.fill(WHITE)
    screen.blit(background,(0,0))
    scores=font_small.render(str(SCORE_E),True,BLACK)
    scores_m=font_money.render(str(SCORE_M),True,BLACK)
    screen.blit(scores,(10,10))
    screen.blit(scores_m,(WIDTH-37,10))


    #MOVES AND REDRAWS ALL SPRITES
    for x in all_sprites:
        screen.blit(x.image,x.rect)
        x.move()

    #TO BE RUN IF COLLISION OCCUR BETWEEN PLAYER AND ENEMY
    if pygame.sprite.spritecollideany(P1,enemies):
        k=False
        sound_back.stop()
        pygame.mixer.Sound("Crash.wav").play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over,(50,250))
        score_of_money=font_money.render(f"Scores: {SCORE_M}", True, BLACK)
        screen.blit(score_of_money,(150,350))
        pygame.display.flip()

        for x in all_sprites:
            x.kill()

        time.sleep(2)
        done=True
        # pygame.quit()

    pygame.display.flip()
    clock.tick(FPS)

if k:
    sound_back.stop()
pygame.quit()