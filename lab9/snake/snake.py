import pygame, sys ,time 
from random import randrange
pygame.font.init()


RES = 700
SIZE = 25

x, y = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)

length = 1
snake = [(x,y)]

dx, dy = 0, 0

fps = 20

pygame.init()
screen = pygame.display.set_mode((RES,RES))
clock = pygame.time.Clock()

game_speed = 0.5

apple_value = 1

temp_apple = False

f = pygame.font.Font(None, 36)
apple_value_text = f.render(str(apple_value), True, "blue")


eaten_apples = 0
score = 0

apples_for_next_level = 0

dirs = {"UP":True,"DOWN":True,"LEFT":True,"RIGHT":True}

font = pygame.font.Font(None, 36)
game_over = font.render("Game Over", True, "black")

start_ticks=pygame.time.get_ticks()

while True:
    clock.tick(fps) 
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    screen.fill("black")

    
    [(pygame.draw.rect(screen,"green", (i,j,SIZE,SIZE) ) ) for i,j in snake]

        
    if not temp_apple:
        pygame.draw.rect(screen,"red", (*apple,SIZE,SIZE))
    else:
        if (pygame.time.get_ticks()//1000)%2==0:
            pygame.draw.rect(screen,"red", (*apple,SIZE,SIZE))

     
    
    x += dx * (SIZE//2)
    y += dy * (SIZE//2)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT] and dirs["LEFT"]:
        dx, dy = -game_speed,0
        dirs = {"UP":True,"DOWN":True,"LEFT":True,"RIGHT":False}
    if pressed[pygame.K_RIGHT] and dirs["RIGHT"]:
        dx, dy = game_speed,0
        dirs = {"UP":True,"DOWN":True,"LEFT":False,"RIGHT":True}
    if pressed[pygame.K_UP] and dirs["UP"]:
        dx, dy = 0,-game_speed
        dirs = {"UP":True,"DOWN":False,"LEFT":True,"RIGHT":True}    
    if pressed[pygame.K_DOWN] and dirs["DOWN"]:
        dx, dy = 0,game_speed
        dirs = {"UP":False,"DOWN":True,"LEFT":True,"RIGHT":True}

    if x<-SIZE:
        x = RES 
    elif x>RES:
        x=-SIZE
    if y<-SIZE:
        y = RES 
    elif y>RES:
        y=-SIZE           

    snake.append((x,y))
    snake = snake[-length:] 

    if (snake[-1][0] > apple[0]-SIZE and snake[-1][0] < apple[0]+SIZE) and (snake[-1][1] > apple[1]-SIZE and snake[-1][1] < apple[1]+SIZE):
        apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)   
        length +=apple_value
        score+=apple_value
        apple_value = randrange(1,6)

        eaten_apples += 1
        apples_for_next_level+=1

        temp_apple_random = randrange(1,4)
        
        if temp_apple_random==1 or temp_apple_random==2:
            temp_apple = False
        elif temp_apple_random==3:
            temp_apple = True    

        apple_value_text = f.render(str(apple_value), True, "blue")

        if temp_apple:
            start_ticks=pygame.time.get_ticks()

    if temp_apple:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
    

    if temp_apple and seconds>10: 
        temp_apple = False      
        apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
        seconds = 0
        temp_apple_random = randrange(1,4)

    if apples_for_next_level==2:
        game_speed+=0.1
        apples_for_next_level = 0


    eaten_text = font.render("eaten:"+ str(eaten_apples), True, "green")
    score_text = font.render("score:"+ str(score), True, "white")
    screen.blit(eaten_text,(RES-100,5))
    screen.blit(score_text,(RES-100,35))



    screen.blit(apple_value_text, apple)
    pygame.display.flip()
       
    if len(snake) != len(set(snake)):
        screen.fill("red")
        screen.blit(game_over, (RES//2 - 100 ,RES//2))
        
        pygame.display.update()    
        time.sleep(3)
        pygame.quit()
        sys.exit() 