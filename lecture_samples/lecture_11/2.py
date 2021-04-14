#Paint
import pygame, random

# чтобы плавно рисовать и не было зазоров между кругами
# (x1,y1),(x2,y2)
# Ax+By+C=0
# (x-x1)/(x2-x1)=(y-y1)/(y2-y1)
# A=y2-y1
# B=x1-x2
# C=x2*y1-x1*y2

def draw_line(screen,start,end,width,color):
    x1=start[0]
    y1=start[1]
    x2=end[0]
    y2=end[1]

    dx=abs(x1-x2)
    dy=abs(y1-y2)

    A=y2-y1
    B=x1-x2
    C=x2*y1-x1*y2

    if dx>dy:
        if x1>x2:
            x1,x2=x2,x1
            y1,y2=y2,y1

        for x in range(x1,x2):
            y=(-C-A*x)/B
            pygame.draw.circle(screen,color,(x,y),width)
    else:
        if y1>y2:
            x1,x2=x2,x1
            y1,y2=y2,y1

        for y in range(y1,y2):
            x=(-C-B*y)/A
            pygame.draw.circle(screen,color,(x,y),width)



def main():
    pygame.init()
    WIDTH=800
    HEIGHT=600
    screen=pygame.display.set_mode((WIDTH,HEIGHT))  
    mode='random'
    draw_on=False
    color=(255,128,0)
    radius=10

    colors={
        'red' : (255,0,0),
        'blue' : (0,0,255),
        'green' : (0,255,0),
        # 'black': (0,0,0),
        'pink' : (100,0,0)
    }

    while True:
        pressed=pygame.key.get_pressed()
        alt_held=pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held=pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return 
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w and ctrl_held:
                    return
                if event.key==pygame.K_F4 and alt_held:
                    return
                if event.key==pygame.K_r:
                    mode='red'
                if event.key==pygame.K_b:
                    mode='blue'
                if event.key==pygame.K_g:
                    mode='green'
                if event.key==pygame.K_p:
                    mode='pink'
                if event.key==pygame.K_UP:
                    if radius<20:
                        radius+=1
                if event.key==pygame.K_DOWN:
                    if radius>1:
                        radius-=1
            if event.type==pygame.MOUSEBUTTONDOWN:
                # чтобы задать условие если нажали определенную кнопку мышки
                # if event.button==1:  -если нажимаем левую кнопку мышки.
                # if event.button==2:  -если нажали на скроллер мышки, то есть на среднюю кнопку мышки
                # if event.button==3:  -если нажали на правую кнопку мышки
                if mode=='random':
                    color=(random.randrange(256),random.randrange(256),random.randrange(256))
                else:
                    color=colors[mode]

                pygame.draw.circle(screen,color,event.pos,radius) #pos0-coordinate of x; pos1-coordinate of y
                draw_on=True
            if event.type==pygame.MOUSEBUTTONUP:
                draw_on=False

            if event.type==pygame.MOUSEMOTION:
                if draw_on:
                    draw_line(screen,last_pos,event.pos,radius,color)
                    # pygame.draw.circle(screen,color,event.pos,radius)
                last_pos=event.pos
        pygame.display.flip()

    pygame.quit()
main()
pygame.quit()
