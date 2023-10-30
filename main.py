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


Grid = World(columns=10, rows=20, cell_size=20)

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


        #Creacion de figuras
        Grid.draw(screen)
        pygame.display.update()

game_loop_scene()