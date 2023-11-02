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
    #Gameloop
    while not Grid.end:
        clock.tick(FPS)
        screen.fill(LIGHT_BLACK)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    end_game()
                if event.key == pygame.K_RIGHT:
                    Grid.move(1,0)
                if event.key == pygame.K_LEFT:
                    Grid.move(-1,0)
                if event.key == pygame.K_SPACE:
                    Grid.rotate()
            elif event.type == timer_event:
                Grid.move(0,1)
                


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


