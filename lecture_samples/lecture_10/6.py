#WORKING WITH IMAGE
import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))

done=False
clock=pygame.time.Clock()
image=pygame.image.load('bf.png')

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
     
    screen.fill((255,255,255))
    screen.blit(image,(100,100))

    pygame.display.flip()
pygame.quit()