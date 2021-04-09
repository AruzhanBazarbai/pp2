#set_alpha- прозрачность
import pygame
pygame.init()
screen=pygame.display.set_mode((500,400))
surf=pygame.Surface((100,100))
screen.fill((255,255,255))
surf.fill((0,255,0))
pygame.draw.rect(screen,(0,0,0),(50,150,300,100))
surf.set_alpha(200)
screen.blit(surf,(100,100))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    pygame.display.flip()

pygame.quit()