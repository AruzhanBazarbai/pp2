import pygame
import random
import pickle
import time
import sys

pygame.init()
FILE_NAME='snakes.data'
FILE_LEVEL='snakes.level'
SCORE_G=0
SCORE=5

#SCREEN
WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")

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
        self.speed=25
        self.d=5

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen,RED,element,self.radius)

    def add_to_snake(self):
        self.size+=1
        self.elements.append([0,0])
        self.is_add= False

    #CONDITIONS FOR BUTTONS
    def  change(self,pressed_keys):
        if (pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]) and self.dy!=self.d:
            self.dx=0
            self.dy=-self.d
        elif (pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]) and self.dy!=-self.d:
            self.dx=0
            self.dy=self.d
        elif (pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]) and self.dx!=self.d:
            self.dx =-self.d
            self.dy = 0
        elif (pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]) and self.dx!=-self.d:
            self.dx=self.d
            self.dy=0

    def move(self,score):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size-1,0,-1):
            self.elements[i][0]=self.elements[i-1][0]
            self.elements[i][1]=self.elements[i-1][1]

        self.elements[0][0]+=self.dx #изменяем координату головы по х
        self.elements[0][1]+=self.dy #изменяем координату головы по у

        #CONDITIONS FOR COLLISION SNAKE WITH WALLS
        if score==0:
            if self.elements[0][0]>=(WIDTH-25) or self.elements[0][0]<=25:
                message()
            elif self.elements[0][1]>=(HEIGHT-25) or self.elements[0][1]<=25:
                message()
        elif score==SCORE:
            self.speed=35
            if self.elements[0][0]>=(WIDTH-25) or self.elements[0][0]<=25:
                message()
            elif self.elements[0][1]>=(HEIGHT-25) or self.elements[0][1]<=25:
                message()
            elif self.elements[0][0]>=(WIDTH//2-50) and self.elements[0][0]<=WIDTH and self.elements[0][1]>=(HEIGHT//2-50) and self.elements[0][1]<=(HEIGHT//2-30):
                message()
        elif score==SCORE*2:
            self.speed=45
            if self.elements[0][0]>=0 and self.elements[0][0]<=(WIDTH//2+5) and self.elements[0][1]>=0 and self.elements[0][1]<=25:
                message()
            elif self.elements[0][0]>=(WIDTH//2-25) and self.elements[0][0]<=(WIDTH//2+5) and self.elements[0][1]>=0 and self.elements[0][1]<=(HEIGHT//3+55):
                message()
            elif self.elements[0][0]>=(WIDTH//2-5) and self.elements[0][0]<=WIDTH and self.elements[0][1]>=((HEIGHT//3)*2-5) and self.elements[0][1]<=((HEIGHT//3)*2+25):
                message()
            elif self.elements[0][0]>=(WIDTH-25) and self.elements[0][0]<=WIDTH and self.elements[0][1]>=((HEIGHT//3)*2+15) and self.elements[0][1]<=HEIGHT:
                message()
            elif self.elements[0][0]>=0 and self.elements[0][0]<=25 and self.elements[0][1]>=((HEIGHT//3)*2-5) and self.elements[0][1]<=HEIGHT:
                message()
            elif self.elements[0][0]>=20 and self.elements[0][0]<=(WIDTH//2+5) and self.elements[0][1]>=(HEIGHT-25) and self.elements[0][1]<=HEIGHT:
                message()
            
            if self.elements[0][0]>WIDTH:
                self.elements[0][0]=0
            elif self.elements[0][0]<0:
                self.elements[0][0]=WIDTH
            if self.elements[0][1]>HEIGHT:
                self.elements[0][1]=0
            elif self.elements[0][1]<0:
                self.elements[0][1]=HEIGHT


    def eat(self,foodx,foody):
        x=self.elements[0][0]
        y=self.elements[0][1]
        if foodx<=x<=foodx+20 and foody<=y<=foody+20:
            return True
        return False

#FINISH GAME IF SNAKE HITT THE WALLS
def message():
    font=pygame.font.SysFont(None,WIDTH//8)
    text=font.render("GAME OVER!!!",True,BLACK) 
    screen.fill(GREEN)
    screen.blit(text,(WIDTH//4,HEIGHT//4))  
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

#CLASS FOR FOOD
class Food:
    def __init__(self):
        self.x=random.randint(25,WIDTH-40)
        self.y=random.randint(25,HEIGHT-40)
        self.choose=0

    def get(self,score):
        if score==0:
            self.x=random.randint(25,WIDTH-40)
            self.y=random.randint(25,HEIGHT-40)
        elif score==SCORE:
            self.choose=random.randint(1,2)
            if self.choose==1:
                self.x=random.randint(25,WIDTH-40)
                self.y=random.randint(25,HEIGHT//2-70)
            else:
                self.x=random.randint(25,WIDTH-40)
                self.y=random.randint(HEIGHT//2-25,HEIGHT-40)
        elif score==SCORE*2:
            self.choose=random.randint(1,3)
            if self.choose==1:
                self.x=random.randint(WIDTH//2+5,WIDTH-15)
                self.y=random.randint(5,(HEIGHT//3)*2-5)
            elif self.choose==2:
                self.x=random.randint(WIDTH//2+5,WIDTH-40)
                self.y=random.randint((HEIGHT//3)*2+25,HEIGHT-5)
            else:
                self.x=random.randint(25,WIDTH//2-40)
                self.y=random.randint(25,HEIGHT-40)
        # print(self.x,self.y)

    def draw(self):
        pygame.draw.rect(screen,GREEN,(self.x,self.y,15,15))

#FUNCTION OF MENU
def menu():
    player_1,player_2=False, False
    start=True
    menu_1,menu_2=True,False

    #TEXTS
    font_1=pygame.font.SysFont(None,WIDTH//23)
    text_start_1=font_1.render("Press space to load saved game, or other button to start a new one", True,BLACK)
    font_1_2=pygame.font.SysFont(None,WIDTH//23)
    text_start_1_2=font_1_2.render("Also press space to save and quit the game",True,BLACK)
    font_2=pygame.font.SysFont(None,WIDTH//16)
    font_3=pygame.font.SysFont(None,WIDTH//16)
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
            screen.blit(text_start_1,(20,HEIGHT//2-100))
            screen.blit(text_start_1_2,(80,HEIGHT//2))
        elif menu_2:
            screen.blit(text_start_2,(WIDTH//5,HEIGHT//3))
            screen.blit(text_start_3,(WIDTH//5,HEIGHT//3+100))
        else:
            start=False
        pygame.display.flip()
    return True,False,player_1

#FUNCTIONS FOR LEVELS AND WALLS
def level_1():
    rect_1=(0,0,20,HEIGHT)
    rect_2=(20,0,WIDTH-20,20)
    rect_3=(WIDTH-20,20,20,HEIGHT-20)
    rect_4=(20,HEIGHT-20,WIDTH-40,20)
    pygame.draw.rect(screen,BLUE,rect_1)
    pygame.draw.rect(screen,BLUE,rect_2)
    pygame.draw.rect(screen,BLUE,rect_3)
    pygame.draw.rect(screen,BLUE,rect_4)

def level_2():
    rect_1=(0,0,20,HEIGHT)
    rect_2=(20,0,WIDTH-20,20)
    rect_3=(WIDTH-20,20,20,HEIGHT-20)
    rect_4=(20,HEIGHT-20,WIDTH-40,20)
    rect_5=(WIDTH//2-50,HEIGHT//2-60,WIDTH-20,20)
    pygame.draw.rect(screen,BLUE,rect_1)
    pygame.draw.rect(screen,BLUE,rect_2)
    pygame.draw.rect(screen,BLUE,rect_3)
    pygame.draw.rect(screen,BLUE,rect_4)
    pygame.draw.rect(screen,BLUE,rect_5)

def level_3():
    rect_1=(0,0,WIDTH//2-20,20)
    rect_2=(WIDTH//2-20,0,20,HEIGHT//3+50)
    rect_3=(WIDTH//2,(HEIGHT//3)*2,WIDTH//2,20)
    rect_4=(WIDTH-20,(HEIGHT//3)*2+20,20,HEIGHT-((HEIGHT//3)*2+20))
    rect_5=(0,(HEIGHT//3)*2,20,HEIGHT-((HEIGHT//3)*2))
    rect_6=(20,HEIGHT-20,WIDTH//2-20,20)
    pygame.draw.rect(screen,BLUE,rect_1)
    pygame.draw.rect(screen,BLUE,rect_2)
    pygame.draw.rect(screen,BLUE,rect_3)
    pygame.draw.rect(screen,BLUE,rect_4)
    pygame.draw.rect(screen,BLUE,rect_5)
    pygame.draw.rect(screen,BLUE,rect_6)
    


#MAIN FUNCTION
def game_loop(done):
    if done:
        return
    clock=pygame.time.Clock()
    S1=Snake(100,100)
    F1=Food()
    S2=Snake(150,100)
    d=5
    a,b,c=menu()
    l_1,l_2,l_3=True,False,False

    #SCORES
    global SCORE
    global SCORE_G
    level=0
    score_1=0
    score_2=0
    
    font_1=pygame.font.SysFont(None,WIDTH//26)
    font_2=pygame.font.SysFont(None,WIDTH//26)
    font_3=pygame.font.SysFont(None,100)

    if not a:
        return
    elif b:
        try:
            with open(FILE_NAME, 'br') as f:
                snakes = pickle.load(f)
            with open(FILE_LEVEL,'r') as f:
                text=f.read()
                res=''
                t=[]
                for x in text:
                    if x==' ':
                        t.append(int(res))
                        res=''
                    else:
                        res+=x
                # print(t)
                level,score_1,score_2,S1.speed=t          

        except Exception as e:
            print(e)
            if c:
                snakes=(S1,)
            else:
                snakes=(S1,S2)
    elif c:
       snakes=(S1,)
    else:
        snakes=(S1,S2)

    if level==1:
        l_1,l_2,l_3=True,False,False
        SCORE_G=0
    elif level==2:
        SCORE_G=SCORE
        l_1,l_2,l_3=False,True,False
    elif level==3:
        SCORE_G=SCORE*2
        l_1,l_2,l_3=False,False,True
        
    #GAME LOOP
    while not done:
        screen.fill(BLACK)
        clock.tick(S1.speed)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    with open(FILE_NAME, 'bw') as f:
                        pickle.dump(snakes, f)
                    with open(FILE_LEVEL,'w') as f:
                        f.write(str(level))
                        f.write(' ')
                        f.write(str(score_1))
                        f.write(' ')
                        f.write(str(score_2))
                        f.write(' ')
                        f.write(str(snakes[0].speed))
                        f.write(' ')
                    done=True
            
        pressed_keys=pygame.key.get_pressed()

        for snake in snakes:
            snake.draw()
            snake.move(SCORE_G)

        if snakes.__sizeof__()==32:
            if snakes[0].eat(F1.x,F1.y):
                snakes[0].is_add=True
                F1.get(SCORE_G)
                score_1+=1
            snakes[0].change(pressed_keys)
            text_1=font_1.render("SCORE_1: {0}/{1}".format(score_1,SCORE),True,WHITE)
            screen.blit(text_1,(20,20))
            # print(score_1)
            if score_1==SCORE:
                SCORE_G+=SCORE
                score_1=0

            if SCORE_G==SCORE and l_1:
                l_1=False
                l_2=True
            elif SCORE_G==(SCORE*2) and l_2:
                l_2=False
                l_3=True
            elif SCORE_G==(SCORE*3) and l_3:
                l_3=False


        elif snakes.__sizeof__()==40:
            if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_RIGHT]:
                snakes[0].change(pressed_keys)
            elif pressed_keys[pygame.K_w] or pressed_keys[pygame.K_s] or pressed_keys[pygame.K_a] or pressed_keys[pygame.K_d]:
                snakes[1].change(pressed_keys)

            if snakes[0].eat(F1.x,F1.y):
                snakes[0].is_add=True
                F1.get(SCORE_G)
                score_1+=1
            elif snakes[1].eat(F1.x,F1.y):
                snakes[1].is_add=True
                F1.get(SCORE_G)
                score_2+=1
            
            text_1=font_1.render("SCORE_1: {0}/{1}".format(score_1,SCORE),True,WHITE)
            screen.blit(text_1,(20,20))
            text_2=font_2.render("SCORE_2: {0}/{1}".format(score_2,SCORE),True,WHITE)
            screen.blit(text_2,(WIDTH-170,20))

            if score_1>=SCORE and score_2>=SCORE:
                SCORE_G+=SCORE
                score_1=0
                score_2=0

            if SCORE_G==SCORE:
                l_1=False
                l_2=True
            elif SCORE_G==SCORE*2:
                l_2=False
                l_3=True
            elif SCORE_G==SCORE*3:
                l_3=False
        
        if l_1:
            level=1
            level_1()
        elif l_2:
            level=2
            level_2()
        elif l_3:
            level=3
            level_3()
        else:
            screen.fill(GREEN)
            text_3=font_3.render("VICTORY!!!",True,BLACK)
            screen.blit(text_3,(WIDTH//4,HEIGHT//4))
            pygame.display.flip()
            time.sleep(2)
            done=True


        F1.draw()
        pygame.display.flip()

game_loop(False)
pygame.quit()