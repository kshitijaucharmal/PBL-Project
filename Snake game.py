print("Lets create a game in Python")
# Snake game
import pygame as py
import random
import time
# Snake's speed 
snake_speed = 10
# Defining width and height of the screen
width_x = 960
height_y = 720

# colors of the text as shown
black = py.Color(0,0,0)
white = py.Color(255,255,255)
red = py.Color(255,64,64)
green = py.Color(118,238,0)
blue = py.Color(0,205,205)

# Initialize the Pygame and control the fps to make the speed of the snake flexibe

# Initialize Pygame

py.init()
# Initialize the window of the game

py.display.set_caption("SNAKE GAME")
window_snakegame = py.display.set_mode((width_x,height_y))

# To control the frames per second
fps =   py.time.Clock()

# Initializing the snake position,food position and direction of the snake on the game screen

# Defining the snake position at default
snake_position = [120,60]
# Creating a snake by assigning 5 blocks to the snake's body

snake_body = [[120,60],
              [110,60],
              [100,60],
              [90,60],
              [80,60]
             ]
# Locating the food in random manner
food_position = [random.randrange(1,(width_x//10))*10,random.randrange(1,(height_y//10))*10]

spawn_of_food = True

# Assigning the direction to the snake

snake_direction = 'LEFT'
flexible_to_change = snake_direction

# Declaring the satrting score as 0

score = 0

# Scored earned and its size

def score_matrices(selection,color,font,size):
# Building the font obj where we defier the font color 
    font_score = py.font.SysFont(font,size)
    surface_score = font_score.render('The Score earned: ' + str(score),True,color)
    
# create a rectangular object referencing the text surface object
    rect_score = surface_score.get_rect()
    
# To display the score while playing
    window_snakegame.blit(surface_score, rect_score)
    
# When the snake hits the wall or itself

def end_gameover():
# font object which will display the scores earned so far
    font_displayscore = py.font.SysFont("The times new roman", 50)
    
    surface_gameover = font_displayscore.render('The current score is: ' + str(score),True,red)
    
    rect_gameover = surface_gameover.get_rect()
    
# GAME OVER will appear in the middle of the game window
    rect_gameover.midtop = (width_x/2,height_y/4)
    
    window_snakegame.blit(surface_gameover, rect_gameover)
    
# Updating the score 
    py.display.flip()
# give 5 sec game time
    time.sleep(5)
    
# Quit the game by using 
    py.quit()
    
# main func()

while True:
# Enable keys for the movement of the snake
    for event in py.event.get():
        if event.type == py.KEYDOWN:
            if event.key == py.K_UP:
                flexible_to_change = "UP"
            if event.key == py.K_DOWN:
                flexible_to_change = "DOWN"
            if event.key == py.K_LEFT:
                flexible_to_change = "LEFT"
            if event.key == py.K_RIGHT:
                flexible_to_change = "RIGHT"
                
# since we don't to move our snake in the opposite direction
    if flexible_to_change == "UP" and snake_direction != "DOWN":
        snake_direction = "UP"
    if flexible_to_change == "DOWN" and snake_direction != "UP":
        snake_direction = "DOWN"
    if flexible_to_change == "LEFT" and snake_direction != "RIGHT":
        snake_direction = "LEFT"
    if flexible_to_change == "RIGHT" and snake_direction != "LEFT":
        snake_direction = "RIGHT"
        
# making the snake move
    if snake_direction == "UP":
        snake_position[1] -= 10
    if snake_direction == "DOWN":
        snake_position[1] += 10
    if snake_direction == "LEFT":
        snake_position[0] -= 10
    if snake_direction == "RIGHT":
        snake_position[0] += 10
        
# snake growing and when it hits the food
    snake_body.insert(0,list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 5
        spawn_of_food = False
    else:
        snake_body.pop()
        
    if not spawn_of_food:
        food_position = [random.randrange(1,(width_x//10))*10,random.randrange(1,(height_y//10))*10]
        
    spawn_of_food = True
    window_snakegame.fill(white)
    
    
    for position in snake_body:
        py.draw.rect(window_snakegame, blue, py.Rect(position[0],position[1],10,10))
        py.draw.rect(window_snakegame, red, py.Rect(food_position[0],food_position[1],10,10))
        
        
    if snake_position[0] < 0 or snake_position[0] > width_x - 10:
        end_gameover()
    if snake_position[1] < 0 or snake_position[1] > height_y - 10:
        end_gameover()
    
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            end_gameover()
            
            
    score_matrices(1, white , 'times new roman', 20)
    
    # refresh game window
    
    py.display.update()
    
    # refresh rate 
    
    fps.tick(snake_speed)
        
    
    
    


