import pygame

pygame.init()

white = (255,255,255)
red = (255,0,0)
green = (0 , 255,0)
blue = (0 , 0 , 255)
black = (0 , 0 , 0)
screen_width = 700
screen_height = 500

gameWindow = pygame.display.set_mode((screen_width, screen_height))

screen_width = 900
screen_height = 600
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10


pygame.display.set_caption('Snakes')
pygame.display.update()


# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
            

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,black,(snake_x,snake_y,snake_size,snake_size))
    pygame.display.update()


pygame.quit()
quit()