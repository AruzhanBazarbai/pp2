import pygame

size = width, height = (500, 500)
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))  # black
# 1-p)na chem budem risovat',2-p)color of object,3-p) x,y,width,height, 4-p)shirina kontura
pygame.draw.rect(screen, (100, 10, 100), [100, 100, 150, 150], 10)
done = False

while not done:
    # draw something
    for event1 in pygame.event.get():
        if event1.type==pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()
