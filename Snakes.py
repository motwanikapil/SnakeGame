import pygame
import random

pygame.init()

white = (255,255,255)
red = (255,0,0)
green = (0 , 255,0)
blue = (0 , 0 , 255)
black = (0 , 0 , 0)
screen_width = 700
screen_height = 500
velocity_x = 0
velocity_y = 0
score = 0

food_x = random.randint(20 , screen_width//1.5)%60
food_y = random.randint(20 , screen_height//1.5)%60

gameWindow = pygame.display.set_mode((screen_width, screen_height))

screen_width = 900
screen_height = 600
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10
clock = pygame.time.Clock()
fps = 60
init_velocity = 5


pygame.display.set_caption('Snakes')
pygame.display.update()


# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0
                

    snake_x += velocity_x
    snake_y += velocity_y
    if abs(snake_x - food_x < 1) and abs(snake_y - food_y < 1):
        score += 1
        print('Score : '+str(score))
        food_x = random.randint(20 , screen_width/2)
        food_y = random.randint(20 , screen_height/2)
        
    
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,red,(food_x,food_y,snake_size,snake_size))
    pygame.draw.rect(gameWindow,black,(snake_x,snake_y,snake_size,snake_size))
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()