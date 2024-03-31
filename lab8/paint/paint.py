from utils import *
import pygame,sys

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
    Button(10,button_y,50,50,BLACK),
    Button(70,button_y,50,50,RED),
    Button(130,button_y,50,50,BLUE),
    Button(190,button_y,50,50,GREEN),
    Button(250,button_y,60,50,WHITE,"Erase"),
    Button(320,button_y,60,50,WHITE, "Clear"),
    Button(390,button_y,60,50,WHITE, "Circle"),
    Button(460,button_y,90,50,WHITE, "Rectangle")
]

rectangle_mode = False
circle_mode = False

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
            
            if (row1>row2):
                if col1>row2:
                  
                    for i in range(row2, row1 +1):
                        for j in range(col2,col1 + 1):
                            grid[i][j] = drawing_color 
                elif col2>col1:
                    
                    print(drawing_color)
                    for i in range(row2, row1 +1):
                        for j in range(col1,col2 + 1):
                            grid[i][j] = drawing_color
            elif(row2>row1):
                if col1>row2:
                   
                    for i in range(row1, row2 +1):
                        for j in range(col2,col1 + 1):
                            grid[i][j] = drawing_color 
                elif col2>col1:
                    
                    for i in range(row1, row2 +1):
                        for j in range(col1,col2 + 1):
                            grid[i][j] = drawing_color

        elif event.type == pygame.MOUSEBUTTONDOWN and circle_mode and row<=ROWS:
            
            row1,col1 = get_row_col_from_pos(pos)
            
        elif event.type == pygame.MOUSEBUTTONUP and circle_mode and row<=ROWS:

            row2,col2 = get_row_col_from_pos(pos)

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                if rectangle_mode or circle_mode:
                    raise IndexError
                row,col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color

            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    previous_color = drawing_color

                    

                    if button.text == "Circle" or button.text == "Rectangle":
                        drawing_color = previous_color
                    else:
                        drawing_color = button.color

                    if button.text == "Rectangle":
                        rectangle_mode = True  
                    else:
                        rectangle_mode = False


                    if button.text == "Circle":
                        circle_mode = True  
                    else:
                        circle_mode = False        
                    
                    if button.text == "Clear":
                        grid = init_grid(ROWS,COLS,BG_COLOR)
                        drawing_color = previous_color


    draw(WIN,grid,buttons)
    
