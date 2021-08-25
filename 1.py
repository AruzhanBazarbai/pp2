import pygame

screen=pygame.display.set_mode((400,400))
screen.fill((0,0,0))
pygame.draw.circle(screen,(255,255,255),(20,20),20)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        pygame.display.flip()