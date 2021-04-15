import pygame, random
import math

"""
INSTRUCTION:
1)eraser: right button of mouse
2)to draw rectangle: K_q
3)to draw circle: K_a
4)buttons to choose color: you can see on function FUNC_COLOR()
5)quit and save:
        1.pygame.QUIT
        2.K_w + CTRL
        3.K_F4 + ALT
NOTE:
if you clicked on K_a and then on K_q you can only draw a rectangle. 
Because the last click blocks all other clicks
"""
m='random'

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

#FUNCTION FOR CHOSING COLOR
def func_color(e_key):
    global m
    if e_key==pygame.K_r:
        m='red'
    if e_key==pygame.K_b:
        m='blue'
    if e_key==pygame.K_g:
        m='green'
    if e_key==pygame.K_p:
        m='pink'
    if e_key==pygame.K_y:
        m='yellow'
    if e_key==pygame.K_w:
        m='white'
    if e_key==pygame.K_o:
        m='orange'
    if e_key==pygame.K_u:
        m='purple'
    if e_key==pygame.K_e:
        m='grey'
    if e_key==pygame.K_n:
        m='brown'
    return m

#TO POSITIONS OF RECTANGLE
def rect_positions(x1,y1,x2,y2):
    if x1>x2 and y1<y2:
        x1,x2=x2,x1
    elif x1>x2 and y1>y2:
        x1,x2=x2,x1
        y1,y2=y2,y1
    elif x1<x2 and y1>y2:
        y1,y2=y2,y1

    return x1,y1,x2,y2

#TO POSITIONS OF CIRCLE
def circle_positions(x1,y1,x2,y2):
    a=abs(x1-x2)/2
    b=abs(y1-y2)/2
    if x1>x2 and y1<y2:
        x=x1-a
        y=y1+b
    elif x1>x2 and y1>y2:
        x=x1-a
        y=y1-b
    elif x1<x2 and y1>y2:
        x=x1+a
        y=y1-b
    elif x1<x2 and y1<y2:
        x=x1+a
        y=y1+b

    c=abs(y1-y2)
    d=abs(x1-x2)
    r=math.sqrt(c*c+d*d)/2

    return x,y,r



def main():
    pygame.init()
    WIDTH=800
    HEIGHT=600
    SCREEN_COLOR=(0,0,0)
    screen=pygame.display.set_mode((WIDTH,HEIGHT))  
    screen.fill(SCREEN_COLOR)
    draw_on, draw_rect, draw_circle=False, False, False
    mode='random'
    a,b=0,0
    radius=10
    
    colors={
        'red' : (255,0,0),
        'blue' : (0,0,255),
        'green' : (0,255,0),
        'pink' : (255,100,100),
        'yellow' : (226, 239, 73),
        'white' : (255,255,255),
        'orange' : (250, 103, 19),
        'purple' : (87, 32, 123),
        'grey' : (121, 136, 143),
        'brown' : (164, 109, 40)
    }

    while True:
        pressed=pygame.key.get_pressed()
        alt_held=pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held=pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            #TO EXIT THE GAME
            if event.type==pygame.QUIT:
                pygame.image.save(screen,'paint.jpg')
                return 
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w and ctrl_held:
                    pygame.image.save(screen,'paint.jpg')
                    return
                elif event.key==pygame.K_F4 and alt_held:
                    pygame.image.save(screen,'paint.jpg')
                    return
                #CHANGING THE SIZE OF PEN
                elif event.key==pygame.K_UP:
                    if radius<20:
                        radius+=1
                elif event.key==pygame.K_DOWN:
                    if radius>1:
                        radius-=1
                elif event.key==pygame.K_q:
                    draw_rect=True
                    draw_circle=False
                elif event.key==pygame.K_a:
                    draw_circle=True
                    draw_rect=False
                #CHANGING THE COLOR
                else:
                    mode=func_color(event.key)

            if event.type==pygame.MOUSEBUTTONDOWN:
                #CHANGE MODE TO ERASE OR DRAW
                if event.button==1:
                    if mode=='random':
                        color=(random.randrange(256),random.randrange(256),random.randrange(256))
                    else:
                        color=colors[mode]

                    if not draw_rect and not draw_circle:
                        draw_on=True
                        pygame.draw.circle(screen,color,event.pos,radius) #pos0-coordinate of x; pos1-coordinate of y
                    else:
                        pos=event.pos

                elif event.button==3:
                    color=SCREEN_COLOR
                    pygame.draw.circle(screen,color,event.pos,radius)
                    draw_on=True

            if event.type==pygame.MOUSEBUTTONUP:
                draw_on=False
                #DRAW THE RECTANGLE
                if draw_rect:
                    l1,l2,p1,p2=rect_positions(pos[0],pos[1],event.pos[0],event.pos[1])
                    a=abs(p1-l1)
                    b=abs(p2-l2)
                    pygame.draw.rect(screen,color,(l1,l2,a,b))
                elif draw_circle:
                    x,y,r=circle_positions(pos[0],pos[1],event.pos[0],event.pos[1])
                    pygame.draw.circle(screen,color,(x,y),r)
                draw_rect=False
                draw_circle=False

            #DRAW
            if event.type==pygame.MOUSEMOTION:
                if draw_on:
                    draw_line(screen,last_pos,event.pos,radius,color)
                last_pos=event.pos

                
        pygame.display.update()

    pygame.quit()
main()
pygame.quit()
