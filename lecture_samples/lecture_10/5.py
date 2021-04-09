#WORKING WITH SURFACE
import pygame
from random import randint

pygame.init()

screen=pygame.display.set_mode((500,500))
screen.fill((255,255,255))

background=pygame.Surface((500,200))
background.fill((0,255,0))
xb=0
yb=100

surf=pygame.Surface((100,100))
x=0
y=50

background.blit(surf,(x,y))
screen.blit(background,(xb,yb))

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.MOUSEBUTTONUP:
            yb=randint(0,300)

    if x<500:
        x+=2
    else:
        x=0

    screen.fill((255,255,255))
    background.fill((0,255,0))
    background.blit(surf,(x,y))
    screen.blit(background,(xb,yb))

    
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()