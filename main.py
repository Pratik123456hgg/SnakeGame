import pygame
import random

pygame.init()

from pygame import mixer
mixer.init()

#basic screen setup
HEIGHT,WIDTH = 600,1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("snake and food game")
clock = pygame.time.Clock()

#extras
player_size = 20

#food setup
def get_random():
    return random.randint(0,WIDTH-player_size),random.randint(0,HEIGHT-player_size)
food_size = 20
food_x,food_y = get_random()
food_rect = pygame.Rect(food_x,food_y,food_size,food_size)

#check boundry
def check_boundry(player):
    return (player[0].x < 0 or player[0].x > WIDTH) or (player[0].y < 0 or player[0].y > HEIGHT) 

#show food
food_img_o = pygame.image.load('fruit.png')
food_img = pygame.transform.scale(food_img_o,(25,25))
img_offset_x = (food_size - food_img.get_width()) // 2
img_offset_y = (food_size - food_img.get_height()) // 2
def food_show():
    screen.blit(food_img, (food_rect.x + img_offset_x, food_rect.y + img_offset_y))

#font and background
font_1 = pygame.font.SysFont("Times New Roman",30)
font_2 = pygame.font.SysFont('Arial Black',70)
bg_img = pygame.image.load('bg.png')
mixer.music.load('game_bg.mp3')
mixer.music.play(-1)
# draw_text and 
def draw_text(text,text_col,font,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

max_list = []

White = (255,255,255)
Black = (0,0,0)
Blue = (67, 97, 238)
Pink= (247, 37, 133)
Yellow = (255, 214, 10)
Green = (0,255,0)

def game_loop (max_list):

    #player setup
    food_count = 0
    player_x,player_y = WIDTH//2,HEIGHT//2
    player_speed = 20
    player_rect = [pygame.Rect(player_x,player_y,player_size,player_size)]
    direction = (1,0)

    #main game logic
    game_over = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            elif event.type == pygame.KEYDOWN:
                # Change direction (no diagonal movement)
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        while game_over:
            pygame.display.flip()
            screen.blit(bg_img,(0,0))
            draw_text(f'{food_count}',Pink,font_1,375,380)
            draw_text(f'{max(max_list)}',Pink,font_1,385,435)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running,game_over = (0,0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running,game_over = (0,0)
                    elif event.key == pygame.K_r:
                        mixer.music.unpause()
                        game_loop(max_list)

        screen.fill(Black)

        #player head moving logic
        head = player_rect[0].copy()
        head.x += direction[0]*player_speed
        head.y += direction[1]*player_speed
        player_rect.insert(0,head)

        #check collision
        if player_rect[0].colliderect(food_rect):
            print("Collision detected!")
            eat_sound = mixer.Sound('game_eat.mp3')
            eat_sound.play()
            food_count += 1
            food_rect.x, food_rect.y = get_random()
        else :
            player_rect.pop() 
        
        #draw food and player
        pygame.draw.rect(screen,Black,food_rect)
        food_show()
        for i in player_rect:
            
            pygame.draw.rect(screen,Green,i)

        #game scoreboard
        draw_text(f'Score : {food_count}',Blue,font_1,50,50)

        #game over logic
        for i in range(1,food_count+1):
            if (player_rect[0].x == player_rect[i].x and player_rect[0].y == player_rect[i].y):
                game_over = True
                max_list.append(food_count)
                game_over_sound = mixer.Sound('game_over.mp3')
                game_over_sound.play()
                mixer.music.pause()
        if check_boundry(player_rect):
            game_over = True
            max_list.append(food_count)
            game_over_sound = mixer.Sound('game_over.mp3')
            game_over_sound.play()
            mixer.music.pause()
        pygame.display.flip()
        clock.tick(10)

game_loop(max_list)

pygame.quit()
