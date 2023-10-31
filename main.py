import pygame
from typing import NoReturn
from constants import(
    SCREEN_RESOLUTION,
    FPS,
    LIGHT_BLACK,
)

from assets import World

def end_game() -> NoReturn:
    pygame.quit()
    quit()

# Init
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()

Grid = World()

# Timer event
time_delay = 50 # velocidad de caida
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)

def game_loop_scene() -> NoReturn:
    #Gameloop
    while True:
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

game_loop_scene()