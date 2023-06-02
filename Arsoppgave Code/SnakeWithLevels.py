import pygame
import time
import random

pygame.init()

fancyGreen = (102, 143, 128)
red = (255, 0, 0)
fancyBlue = (11, 201, 205)
bGreen = (227, 233, 194)
fYellow = (248, 198, 48)
black = (0, 0, 0)

window_width = 1200
window_height = 800


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake game by Kicke (WITH LEVELS!)")

clock = pygame.time.Clock()

snake_radius = 10
snake_speed = 15

font_style = pygame.font.SysFont("Times New Roman", 20)
score_font = pygame.font.SysFont("bahnschrift", 35)


def your_score(score):
    value = score_font.render("Your Score " + str(score), True, fYellow)
    window.blit(value, [0, 0])

def cool_snake(snake_radius, snake_List):
    for x in snake_List:
        pygame.draw.circle(window, fancyGreen, (x[0], x[1]), snake_radius)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, (window_width / 3, window_height / 2))

def gameLoop():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, window_width - snake_radius) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_radius) / 10.0) * 10.0

    while not game_over:
        
        while game_close == True:
            window.fill(bGreen)
            message("You Suck LOSER! Press 'q' to Quit or 'space' to Play Again", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and not x1_change == snake_radius:
                    x1_change = -snake_radius
                    y1_change = 0
                elif event.key == pygame.K_d and not x1_change == -snake_radius:
                    x1_change = snake_radius
                    y1_change = 0
                elif event.key == pygame.K_w and not y1_change == snake_radius: 
                    x1_change = 0
                    y1_change = - snake_radius
                elif event.key == pygame.K_s and not y1_change == -snake_radius:
                    x1_change = 0
                    y1_change = snake_radius

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True           
        x1 += x1_change
        y1 += y1_change
        window.fill(fancyBlue)
        pygame.draw.rect(window, fYellow, (foodx, foody, snake_radius, snake_radius))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        cool_snake(snake_radius, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()
    
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_radius + 10) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_radius + 10) / 10.0) * 10.0
            Length_of_snake += 1
            
        clock.tick(snake_speed)

    pygame.quit()
    quit()



gameLoop()