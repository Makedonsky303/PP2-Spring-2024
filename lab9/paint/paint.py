from utils import *
import pygame,sys
from math import sqrt

pygame.init()

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()


def init_grid(rows,cols,color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color) 
    return grid


grid = init_grid(ROWS,COLS,BG_COLOR)

def draw_grid(win,grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win,pixel,(j*PIXEL_SIZE,i*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE))
    if DRAW_GRID_LINES:
        for i in range(ROWS+1):
            pygame.draw.line(win,BLACK,(0,i*PIXEL_SIZE),(WIDTH,i*PIXEL_SIZE))
        for j in range(COLS+1):
            pygame.draw.line(win,BLACK,(j*PIXEL_SIZE,0),(j*PIXEL_SIZE,HEIGHT-TOOLBAR_HEIGHT))

def draw(win,grid,buttons):
    win.fill(BG_COLOR)
    draw_grid(win,grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()

def get_row_col_from_pos(pos):
    x,y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row,col

drawing_color = BLACK
previous_color = drawing_color

button_y = HEIGHT - TOOLBAR_HEIGHT//2 - 25
buttons = [
    Button(10,button_y,25,25,BLACK),
    Button(40,button_y,25,25,RED),
    Button(10,button_y+30,25,25,BLUE),
    Button(40,button_y+30,25,25,GREEN),
    Button(75,button_y-22,52,40,WHITE,"Erase"),
    Button(75,button_y+22,52,40,WHITE, "Clear"),
    Button(135,button_y-22,60,40,WHITE, "Circle"),
    Button(135,button_y+22,90,40,WHITE, "Rectangle"),
    Button(235,button_y-22,125,40,WHITE, "Right triangle"),
    Button(235,button_y+22,170,40,WHITE, "Equilateral triangle"),
    Button(390,button_y-22,100,40,WHITE, "Rhombus")
]

rectangle_mode = False
circle_mode = False
right_triangle_mode = False
equilateral_triangle_mode = False
rhombus_mode = False

while True:
    clock.tick(FPS)
    pressed = pygame.key.get_pressed()


    
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        
        x,y = pos
        row = y // PIXEL_SIZE
        col = x // PIXEL_SIZE

        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and rectangle_mode and row<=ROWS:
            
            row1,col1 = get_row_col_from_pos(pos)
            
        elif event.type == pygame.MOUSEBUTTONUP and rectangle_mode and row<=ROWS:

            row2,col2 = get_row_col_from_pos(pos)

            for i in range(min(row1,row2), max(row1,row2)):
                for j in range(min(col1,col2),max(col1,col2)):
                    grid[i][j] = drawing_color

            # if (row1>=row2):
            #     if col1>=col2:
                    
            #         for i in range(row2, row1):
            #             for j in range(col2,col1):
            #                 grid[i][j] = drawing_color 
            #     elif col1<col2:
                    
                    
            #         for i in range(row2, row1):
            #             for j in range(col1,col2):
            #                 grid[i][j] = drawing_color
            # elif(row1<row2):
            #     if col1>=col2:
            #         for i in range(row1, row2):
            #             for j in range(col2,col1):
            #                 grid[i][j] = drawing_color 
            #     elif col1<col2:
                    
            #         for i in range(row1, row2):
            #             for j in range(col1,col2):
            #                 grid[i][j] = drawing_color
                    
                  

        elif event.type == pygame.MOUSEBUTTONDOWN and circle_mode and row<=ROWS:

            first_pos = pos
            
            # row1,col1 = get_row_col_from_pos(pos)
            
        elif event.type == pygame.MOUSEBUTTONUP and circle_mode and row<=ROWS:
            second_pos = pos

            # row2,col2 = get_row_col_from_pos(pos)

            radius =  sqrt((first_pos[0]-second_pos[0])**2 + (first_pos[1]-second_pos[1])**2 ) / 2 

     

            center_x = (first_pos[0]+second_pos[0])//2
            center_y = (first_pos[1]+second_pos[1])//2

            for i in range(min(first_pos[0],second_pos[0])-int(radius), 2 *max(first_pos[0],second_pos[0])):
                for j in range(min(first_pos[1],second_pos[1])-int(radius), 2 *max(first_pos[1],second_pos[1])):
                    if (i-center_x)**2 + (j-center_y)**2  <= radius**2 and j // PIXEL_SIZE<ROWS and i//PIXEL_SIZE<HEIGHT:
                        row1,col1 = get_row_col_from_pos((i,j))
                        grid[row1][col1] = drawing_color
            
        elif event.type == pygame.MOUSEBUTTONDOWN and right_triangle_mode and row<=ROWS:
            
            row1,col1 = get_row_col_from_pos(pos)
            
        elif event.type == pygame.MOUSEBUTTONUP and right_triangle_mode and row<=ROWS:

            row2,col2 = get_row_col_from_pos(pos)
            minRow = min(row1,row2)
            maxRow = max(row1,row2)
            minCol = min(col1,col2)
            maxCol = max(col1,col2)

            if (row1<row2 and col1<col2) or (row1>row2 and col1>col2):
                for i in range(minRow,  maxRow):
                    for j in range(minCol,maxCol):
                        if i-minRow>j-minCol:
                            grid[i][j] = drawing_color

            else:
                
                for i in range(minRow,  maxRow):
                    for j in range(minCol,maxCol):
                        
                        if (i-minRow)+(j-minCol) >= min(maxRow-minRow,maxCol-minCol):
                            grid[i][j] = drawing_color 

                                         
            # how?
            # a = max(row1,row2) - min(row1,row2)
            # b = max(col1,col2) - min(col1,col2)

            # for i in range(1,a+1):
            #     for j in range(1,b+1):
            #         if (a-(j-1)*b - (a+1) + i) >=0:
            #             grid[min(row1,row2)+i][min(row1,row2)+j] = drawing_color

        elif event.type == pygame.MOUSEBUTTONDOWN and equilateral_triangle_mode and row<=ROWS:
            
            row1,col1 = get_row_col_from_pos(pos)
            
        elif event.type == pygame.MOUSEBUTTONUP and equilateral_triangle_mode and row<=ROWS:

            row2,col2 = get_row_col_from_pos(pos) 

            minCol = min(col1,col2)
            maxCol = max(col1,col2) 


            if (maxCol-minCol)%2==1:
                triangle_height = (maxCol-minCol)//2 + 1
            else:
                triangle_height = (maxCol-minCol)//2  
            
            bottom = min(row1,row2)- triangle_height
            top = min(row1,row2)

            print(maxCol-minCol)
            print(triangle_height)

            for i in range(bottom, top+1):
                for j in range(minCol,maxCol+1):
                    
                    if triangle_height - (i-bottom)<= j-minCol and triangle_height + (i-bottom)>= j-minCol:
                        grid[i][j] = drawing_color

                    # if (top-bottom)/2 - (i-bottom)< j-minCol:
                    #     grid[i][j] = drawing_color
                        
        elif event.type == pygame.MOUSEBUTTONDOWN and rhombus_mode and row<=ROWS:
            
            row1,col1 = get_row_col_from_pos(pos)
            
        elif event.type == pygame.MOUSEBUTTONUP and rhombus_mode and row<=ROWS:

            row2,col2 = get_row_col_from_pos(pos) 

            minCol = min(col1,col2)
            maxCol = max(col1,col2) 


            if (maxCol-minCol)%2==1:
                triangle_height = (maxCol-minCol)//2 + 1
            else:
                triangle_height = (maxCol-minCol)//2  
            
            bottom = min(row1,row2)- triangle_height
            center = min(row1,row2)
            top = min(row1,row2) + triangle_height

            print(maxCol-minCol)
            print(triangle_height)

            for i in range(bottom, center+1):
                for j in range(minCol,maxCol+1):
                    
                    if triangle_height - (i-bottom)<= j-minCol and triangle_height + (i-bottom)>= j-minCol:
                        grid[i][j] = drawing_color


            for i in range(center, top+1):
                for j in range(minCol,maxCol+1):
                    
                    if triangle_height - (triangle_height-(i-center))<= j-minCol and triangle_height + (triangle_height-(i-center))>= j-minCol:
                        grid[i][j] = drawing_color            
                   
            # *****
            # 0***0
            # 00*00        
                                          
        
  
                     
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                if rectangle_mode or circle_mode or right_triangle_mode or equilateral_triangle_mode or rhombus_mode:
                    raise IndexError
                row,col = get_row_col_from_pos(pos)

                if pressed[pygame.K_1]:
                    for i in range(row-1,row+2):
                        for j in range(col-1,col+2):
                            grid[i][j] = drawing_color
                    
                if pressed[pygame.K_2]:
                    for i in range(row-3,row+4):
                        for j in range(col-3,col+4):
                            grid[i][j] = drawing_color
                    
                if pressed[pygame.K_3]:
                    for i in range(row-5,row+6):
                        for j in range(col-5,col+6):
                            grid[i][j] = drawing_color
                    

                grid[row][col] = drawing_color

            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    previous_color = drawing_color

                    
                    if button.text == "Circle" or button.text == "Rectangle" or button.text == "Right triangle" or button.text == "Equilateral triangle" or button.text=="Rhombus":
                        drawing_color = previous_color
                    else:
                        drawing_color = button.color

                    if button.text == "Rectangle":
                        rectangle_mode = True  
                    elif not button.text == "Clear":
                        rectangle_mode = False


                    if button.text == "Right triangle":
                        right_triangle_mode = True  
                    elif not button.text == "Clear":
                        right_triangle_mode = False

                    if button.text == "Circle":
                        circle_mode = True  
                    elif not button.text == "Clear":
                        circle_mode = False  

                    if button.text == "Equilateral triangle":
                        equilateral_triangle_mode = True  
                    elif not button.text == "Clear":
                        equilateral_triangle_mode = False 

                                       
                    if button.text == "Rhombus":
                        rhombus_mode = True  
                    elif not button.text == "Clear":
                        rhombus_mode = False 


                    if button.text == "Clear":
                        grid = init_grid(ROWS,COLS,BG_COLOR)
                        drawing_color = previous_color


    draw(WIN,grid,buttons)
    
