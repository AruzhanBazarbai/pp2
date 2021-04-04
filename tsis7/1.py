import pygame
import math

pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
HEIGHT=500
WIDTH=1000
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tsis7")
size1=WIDTH//20
size2=HEIGHT//2.5

p=3.14*size1
a=3*p
x=b=-3*p
x_values=[]
while x<=a:
    x_values.append(x)
    x+=6
sin_points=[]
cos_points=[]
for i in x_values:
    sin_points.append([i+3*p+10,math.sin(i)*size2+HEIGHT//2])
    cos_points.append([i+3*p+10,math.cos(i)*size2+HEIGHT//2])


done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    screen.fill(WHITE)
    #pygame.draw.aaline(screen,BLACK,(0,0),(100,100))
    #pygame.draw.aalines(screen,RED,False,points)

    pygame.draw.aalines(screen, BLUE,False,sin_points)
    pygame.draw.aalines(screen, RED,False,cos_points)

    pygame.display.flip()

pygame.quit()
print(math.pi)