# pygame.key.get_pressed()
# pressed=pygame.key.get_pressed()
# pressed[pygame.K_UP]

import pygame
pygame.init()

screen=pygame.display.set_mode((700,500))
pygame.display.set_caption("Rectacle moving")
done=False
is_blue=True
x,y=50,50
a=3
clock=pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            is_blue=not is_blue
    
    
    pressed=pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        y-=a
    if pressed[pygame.K_DOWN]:
        y+=a
    if pressed[pygame.K_LEFT]:
        x-=a
    if pressed[pygame.K_RIGHT]:
        x+=a

    if is_blue:
        color=(0,100,255)
    else:
        color=(255,50,0)

    screen.fill((0,0,0))
    pygame.draw.rect(screen,color,pygame.Rect(x,y,50,50))
    pygame.display.flip()
    clock.tick(60)   

pygame.quit() 