import pygame
import random

pygame.init()

#SCREEN
WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#COLORS
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
BLACK=(0,0,0)

#CLASS FOR SNAKE
class Snake:
    def __init__(self,x,y):
        self.size=1
        self.elements=[[x,y]]
        self.radius=10
        self.dx=5 #right
        self.dy=0
        self.is_add=False
        self.speed=10

    #[x0,y0],[x1,y1],[x2,y2],[x3,y3]  i -> i - 1

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen,RED,element,self.radius)

    def add_to_snake(self):
        self.size+=1
        self.elements.append([0,0])
        self.is_add= False
        if self.size%3==0:
            self.speed+=10

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size-1,0,-1):
            self.elements[i][0]=self.elements[i-1][0]
            self.elements[i][1]=self.elements[i-1][1]

        self.elements[0][0]+=self.dx #изменяем координату головы по х
        self.elements[0][1]+=self.dy #изменяем координату головы по у

    def eat(self,foodx,foody):
        x=self.elements[0][0]
        y=self.elements[0][1]
        if foodx<=x<=foodx+10 and foody<=y<=foody+10:
            return True
        return False
    


#CLASS FOR FOOD
class Food:
    def __init__(self):
        self.x=random.randint(0,WIDTH)
        self.y=random.randint(0,HEIGHT)

    def get(self):
        self.x=random.randint(0,WIDTH)
        self.y=random.randint(0,HEIGHT)

    def draw(self):
        pygame.draw.rect(screen,GREEN,(self.x,self.y,10,10))



done=False
S1=Snake(100,100)
F1=Food()
S2=Snake(150,100)

#SPEED AND FPS
d=5
clock=pygame.time.Clock()
FPS=30

#GAME LOOP
while not done:
    clock.tick(S1.speed)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                done=True
            elif event.key==pygame.K_RIGHT and S1.dx!=-d:
                S1.dx=d
                S1.dy=0
            elif event.key==pygame.K_LEFT and S1.dx!=d:
                S1.dx = -d
                S1.dy = 0
            elif event.key==pygame.K_DOWN and S1.dy!=-d:
                S1.dx=0
                S1.dy=d
            elif event.key==pygame.K_UP and S1.dy!=d:
                S1.dx=0
                S1.dy= -d

            elif event.key==pygame.K_d and S2.dx!=-d:
                S2.dx=d
                S2.dy=0
            elif event.key==pygame.K_a and S2.dx!=d:
                S2.dx = -d
                S2.dy = 0
            elif event.key==pygame.K_s and S2.dy!=-d:
                S2.dx=0
                S2.dy=d
            elif event.key==pygame.K_w and S2.dy!=d:
                S2.dx=0
                S2.dy= -d
            # elif event.key==pygame.K_1:
            #     S1.is_add=True
    if S1.eat(F1.x,F1.y):
        S1.is_add=True
        F1.get()
    if S2.eat(F1.x,F1.y):
        S2.is_add=True
        F1.get()

    S1.move()
    S2.move()
    screen.fill(BLACK)
    S1.draw()
    S2.draw()
    F1.draw()
    pygame.display.flip()

pygame.quit()




