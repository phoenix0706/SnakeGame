author='Jyoti Nigam'


#Importing the modules
import pygame                                                                                                                                                 
import random
import os

#Initialisation
pygame.mixer.init()
pygame.init()


#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,139)


#creating window
screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width,screen_height))


#game title
pygame.display.set_caption("Snake Game")
pygame.display.update()


#Music
pygame.mixer.music.load('C:/Users/admin/Desktop/coding/proj/intro.mp3')
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.6)




#variables for game
clock=pygame.time.Clock()
font=pygame.font.SysFont("Comicsansms",35)



def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y]) #updates window

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])


 
def welcome():
    exit_game=False
    while not exit_game:
        startimg=pygame.image.load("C:/Users/admin/Desktop/coding/proj/start.jpg")
        startimg = pygame.transform.scale(startimg, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(startimg,(0,0))
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.fadeout(200)
                    pygame.mixer.music.load("C:/Users/admin/Desktop/coding/proj/background.mp3")
                    pygame.mixer.music.play(100)
                    pygame.mixer.music.set_volume(.6)
                    gameloop()

        pygame.display.update()
        clock.tick(60)



#Game loop

def gameloop():
    #Game specific variable
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    snk_list=[]
    snk_length=1
    
    
    #High SCore 
   

    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("C:/Users/admin/Desktop/coding/proj/highscore.txt","r") as f:
            hiscore=f.read()
    



   #FOOD
    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_height/2)
    
    

    #Game variables
    score=0
    init_velocity=5
    snake_size=10
    fps=60
    
    #game loop
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(hiscore))
            
            gameoverimg=pygame.image.load("C:/Users/admin/Desktop/coding/proj/gameover.jpg")
            gameoverimg=pygame.transform.scale(gameoverimg,(screen_width,screen_height)).convert_alpha()
            gameWindow.blit(gameoverimg,(0,0))

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    welcome()
            
            
        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
            
            

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x= - init_velocity
                        velocity_y=0

                    if event.key==pygame.K_UP:
                        velocity_y= - init_velocity
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    
                    if event.key==pygame.K_q:
                        score=score+10

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
               
                score+=10
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                snk_length+=5
                if score>int(hiscore):
                    hiscore=score

            bgimg=pygame.image.load("C:/Users/admin/Desktop/coding/proj/snakegame.jpg")
            bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg,(0,0))
            
            text_screen("Score "+str(score)+" Highscore: "+str(hiscore),blue,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size]) #leftx,topy,width,height 

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('C:/Users/admin/Desktop/coding/proj/intro.mp3')
                pygame.mixer.music.play(100)
                pygame.mixer.music.set_volume(.6)
                
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('C:/Users/admin/Desktop/coding/proj/food.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(.6)
            
        
        
        #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size]) #leftx,topy,width,height 
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update() #to update changes in window
        clock.tick(fps)
  

    pygame.quit()
    quit()
welcome()
