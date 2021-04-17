import pygame
import random
import pickle

pygame.init()
FILE_NAME='snakes.data'

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
        if foodx<=x<=foodx+15 and foody<=y<=foody+15:
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
        pygame.draw.rect(screen,GREEN,(self.x,self.y,15,15))

def menu():
    player_1,player_2=False, False
    start=True
    menu_1,menu_2=True,False

    #TEXTS
    font_1=pygame.font.SysFont(None,WIDTH//23)
    text_start_1=font_1.render("Press space to load saved game, or other button to start a new one", True,BLACK)
    font_2=pygame.font.SysFont(None,50)
    font_3=pygame.font.SysFont(None,50)
    text_start_2=font_2.render("Press 1 to one player's game",True,BLACK)
    text_start_3=font_3.render("Press 2 to two player's game",True,BLACK)

    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return False, False,False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and menu_1:
                    return True,True,False
                elif event.key!=pygame.K_SPACE and menu_1:
                    menu_1=False
                    menu_2=True

                elif event.key==pygame.K_1:
                    player_1=True
                    menu_2=False
                elif event.key==pygame.K_2:
                    player_2=True
                    menu_2=False

        screen.fill(GREEN)
        if menu_1:
            screen.blit(text_start_1,(20,HEIGHT//2))
        elif menu_2:
            screen.blit(text_start_2,(WIDTH//5,HEIGHT//3))
            screen.blit(text_start_3,(WIDTH//5,HEIGHT//3+100))
        else:
            start=False
        pygame.display.flip()
    return True,False,player_1


S1=Snake(100,100)
F1=Food()
S2=Snake(150,100)

def game_loop():
    clock=pygame.time.Clock()
    d=5
    a,b,c=menu()
    if not a:
        return
    elif b:
        try:
            with open(FILE_NAME, 'br') as f:
                    snakes = pickle.load(f)
        except Exception as e:
            # print(e)
            if c:
                snakes=(S1)
            else:
                snakes=(S1,S2)
    elif c:
       snakes=(S1)
    else:
        snakes=(S1,S2)

    done=False

        
    #GAME LOOP
    while not done:
        clock.tick(S1.speed)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
                return
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    with open(FILE_NAME, 'bw') as f:
                        pickle.dump(snakes, f)
                    done=True
                    return
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
                if not c:
                    if event.key==pygame.K_d and S2.dx!=-d:
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
        for snake in snakes:
            if snake.eat(F1.x,F1.y):
                snake.is_add=True
                F1.get()
        for snake in snakes:
            snake.move()
        for snake in snakes:
            snake.draw()

        screen.fill(BLACK)
        F1.draw()
        pygame.display.flip()

game_loop()
pygame.quit()




