import pygame
import math

pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
HEIGHT=500
WIDTH=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tsis7")
size_x=WIDTH-60
size_y=HEIGHT-60
a=size_x//6
b=size_y//8
center_x=WIDTH/2
center_y=HEIGHT/2
PI=math.pi

n=math.ceil(6*PI/0.1)
x_values=[]
for i in range(n+1):
    x_values.append(i/10+(-3*PI))
#print(x_values)
kx=(WIDTH-60)//(6*PI)
ky=(HEIGHT-60)//2

cos_points=[]
sin_points=[]
points_y=["1.00","0.75","0.50","0.25","0.00","-0.25","-0.50","-0.75","-1.00"]
points_x=["-3п","-2п","-п","0","п","2п","3п"]

for x in x_values:
    y_s=(math.sin(x))*ky
    y_c=(math.cos(x))*ky
    x_p=x*kx
    sin_points.append([x_p+center_x,-y_s+center_y])
    cos_points.append([x_p+center_x,-y_c+center_y])
#print(sin_points)
#print(cos_points)
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    #surface and lines
    screen.fill(WHITE)
    line_x=pygame.draw.line(screen, BLACK, (30,HEIGHT//2),(WIDTH-30,HEIGHT//2),3)
    line_y=pygame.draw.line(screen, BLACK, (WIDTH//2,30),(WIDTH//2,HEIGHT-30),1)
    border=pygame.draw.rect(screen, BLACK, (30,30,WIDTH-60,HEIGHT-60),3)
    j=0
    for i in range(30,size_x+31,a):
        pygame.draw.line(screen,BLACK,(i,30),(i,HEIGHT-30),2)
        font=pygame.font.Font(None,20)
        text=font.render(points_x[j],True,BLACK)
        screen.blit(text,(i,HEIGHT-20))
        j+=1
    j=0
    for i in range(30,size_y+31,b):
        pygame.draw.line(screen,BLACK,(30,i),(WIDTH-30,i),2)
        font=pygame.font.Font(None,15)
        text=font.render(points_y[j],True,BLACK)
        screen.blit(text,(5,i-2))
        j+=1

    #points
    pygame.draw.aalines(screen, RED, False, sin_points)
    pygame.draw.aalines(screen, BLUE, False, cos_points)
    
    
    pygame.display.flip()

pygame.quit()
#n=int(6*PI/(WIDTH-60)*1000)
#print(n)