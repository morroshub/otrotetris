import pygame
from typing import NoReturn
from constants import *
from assets import *

def end_game() -> NoReturn:
    pygame.quit()
    quit()

# Init
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()

Grid = World()

# Timer event
time_delay = 500 # velocidad de caida
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)

def game_loop_scene() -> None:
    # Gameloop
    move_repeat_delay = 200  # Sensibilidad, cuanto mayor mas lento se mueve
    last_move_time = 0
    game_pause = False

    while not Grid.end:
        clock.tick(FPS)
        screen.fill(LIGHT_BLACK)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    end_game()
                if event.key == pygame.K_p:
                    game_pause = not game_pause
                if event.key == pygame.K_RIGHT:
                    if (not game_pause):
                        Grid.move(1,0)
                        last_move_time = pygame.time.get_ticks()
                if event.key == pygame.K_LEFT:
                    if (not game_pause):
                        Grid.move(-1,0)
                        last_move_time = pygame.time.get_ticks()
                if event.key == pygame.K_DOWN:
                    if (not game_pause):
                        pygame.time.set_timer(timer_event, 50)
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    if (not game_pause):
                        Grid.rotate()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pygame.time.set_timer(timer_event, time_delay)
            elif event.type == timer_event:
                if (not game_pause):
                    Grid.move(0,1)

        # Manejo de movimiento continuo
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if (not game_pause):
                current_time = pygame.time.get_ticks()
                if current_time - last_move_time >= move_repeat_delay:
                    Grid.move(-1, 0)
                    last_move_time = current_time
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if (not game_pause):
                current_time = pygame.time.get_ticks()
                if current_time - last_move_time >= move_repeat_delay:
                    Grid.move(1, 0)
                    last_move_time = current_time
                


        #Creacion de figuras
        Grid.draw(screen)
        pygame.display.update()
    end_scene()

def end_scene() -> None:
    #Game loop
    restart = False
    while not restart:
        clock.tick(FPS)


        #Events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    end_game()
                if event.key == pygame.K_SPACE:
                    restart = True
        
        key = pygame.key.get_pressed()

        #Draw
        #Draw a text using pygame
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('GAME OVER', True, RED, WHITE)
        textRect = text.get_rect()
        textRect.center = (SCREEN_RESOLUTION[0] // 2, SCREEN_RESOLUTION[1]//2)
        screen.blit(text, textRect)

        pygame.display.update()
    Grid.__init__()
    game_loop_scene()

game_loop_scene()


