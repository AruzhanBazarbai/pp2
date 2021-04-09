import pygame
import random

BLACK=(0, 0, 0)
WHITE=(255,255,255)
SCREEN_WIDTH=700
SCREEN_HEIGHT=500

class Ball:
    BALL_SIZE=25

    def get_random_change(self):
        change=random.randint(-2,3)
        while change==0:
            change=random.randint(-2,3)

        return change

    def __init__(self):
        self.x=random.randint(self.BALL_SIZE,SCREEN_WIDTH-self.BALL_SIZE)
        self.y=random.randint(self.BALL_SIZE,SCREEN_HEIGHT-self.BALL_SIZE)
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.x_change=self.get_random_change()
        self.y_change=self.get_random_change()

    def move(self):
        self.x+=self.x_change
        self.y+=self.y_change

        if self.x>SCREEN_WIDTH-self.BALL_SIZE or self.x<self.BALL_SIZE:
            self.x_change*=-1
        if self.y>SCREEN_HEIGHT-self.BALL_SIZE or self.y<self.BALL_SIZE:
            self.y_change*=-1


def main():
    pygame.init()
    size=(SCREEN_WIDTH,SCREEN_HEIGHT)
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("Ball example")
    
    done=False
    ball_list=[]
    ball=Ball()
    ball_list.append(ball)
    clock=pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                ball_list.append(Ball())

        screen.fill(BLACK)
        
        for ball in ball_list:
            ball.move()
        for ball in ball_list:
            pygame.draw.circle(screen,ball.color,[ball.x,ball.y],ball.BALL_SIZE)

        clock.tick(60)
        pygame.display.flip()
    pygame.quit()

main()

    

    
