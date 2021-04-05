import pygame
import math

pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
HEIGHT=700
WIDTH=1200
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tsis7")
size1=WIDTH//18
size2=HEIGHT//2.2

size_x=WIDTH-60
size_y=HEIGHT-60
a_x=size_x//6
b_y=size_y//8

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
    sin_points.append([i+3*p+10,math.sin(i+3*p)*size2+HEIGHT//2])
    cos_points.append([i+3*p+10,math.cos(i+3*p)*size2+HEIGHT//2])
    


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

    line_x=pygame.draw.line(screen, BLACK, (30,HEIGHT//2),(WIDTH-30,HEIGHT//2),3)
    line_y=pygame.draw.line(screen, BLACK, (WIDTH//2,30),(WIDTH//2,HEIGHT-30),1)
    border=pygame.draw.rect(screen, BLACK, (30,30,WIDTH-60,HEIGHT-60),3)
    
    for i in range(30,size_x+1,a_x):
        pygame.draw.line(screen,BLACK,(i,30),(i,HEIGHT-30),2)

    for i in range(30,size_y+1,b_y):
        pygame.draw.line(screen,BLACK,(30,i),(WIDTH-30,i),2)

    pygame.display.flip()

pygame.quit()
print(math.pi)