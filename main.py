
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chase Game")


start_x = 400
start_y = 300
speed = 5
boost = 10


enemy_speed = 4

def reset_game():
    global x, y, ex, ey, game_over
    x = start_x
    y = start_y
    ex = 100
    ey = 100
    game_over = False

reset_game()

running = True

while running:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    
    if game_over:
        if keys[pygame.K_r]:
            reset_game()

    else:
        
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            current_speed = boost
        else:
            current_speed = speed

        
        if keys[pygame.K_LEFT]:
            x -= current_speed
        if keys[pygame.K_RIGHT]:
            x += current_speed
        if keys[pygame.K_UP]:
            y -= current_speed
        if keys[pygame.K_DOWN]:
            y += current_speed

        
        if ex < x:
            ex += enemy_speed
        if ex > x:
            ex -= enemy_speed
        if ey < y:
            ey += enemy_speed
        if ey > y:
            ey -= enemy_speed
        if x < 0:
            x = 0
        if x > 750:
            x = 750
        if y < 0:
            y = 0
        if y > 550:
            y = 550



        
        if x < ex + 50 and x + 50 > ex and y < ey + 50 and y + 50 > ey:
            game_over = True
    screen.fill((254, 143, 0))

    pygame.draw.rect(screen, (0, 255, 0), (x, y, 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), (ex, ey, 50, 50))

    if game_over:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 100)
        text = font.render("GAME OVER", True, (0, 255, 0))
        screen.blit(text, (180, 200))

        font2 = pygame.font.Font(None, 50)
        text2 = font2.render("Press R to Restart", True, (255, 255, 255))
        screen.blit(text2, (220, 320))

    pygame.display.update()


pygame.quit()
