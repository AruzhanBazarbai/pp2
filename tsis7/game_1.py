import pygame
import random
pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
HEIGHT=500
WIDTH=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pygame additional examples")
clock=pygame.time.Clock()

done=False
x,y=0,0
a,b=2,2
list_of_rect=[]
list_of_rect.append([x,y])

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            c=random.randint(0,700)
            d=random.randint(0,500)
            list_of_rect.append([c,d])

    screen.fill(BLACK)
    for i in range(len(list_of_rect)):
        x,y=list_of_rect[i]
        x+=a
        y+=b
        if x>650 or x<0:
            a*=-1
        if y>450 or y<0:
            b*=-1
        pygame.draw.rect(screen,WHITE,[x,y,50,50])
        pygame.draw.rect(screen,RED,[x+10,y+10,30,30])
        list_of_rect[i]=[x,y]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
