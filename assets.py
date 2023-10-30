import pygame
from constants import SCREEN_RESOLUTION, COLORS


Tblock = [[0,2,0],[2,2,2],]

class World:
    def __init__(self, columns, rows, cell_size):
        self.columns = columns
        self.rows = rows
        self.cell_size = cell_size
        self.width, self.height = SCREEN_RESOLUTION

        self.grid = [[0 for _ in range(columns)] for _ in range(rows)] # Son tuplas dentro de otra tupla
        # print(self.grid)
        self.grid[0][0] = 1 
        self.block = Tblock


    def draw(self, screen):
        for i in range(self.rows):
            for j in range(self.columns):
                posicion = (
                    j * self.cell_size + SCREEN_RESOLUTION[0] / 2 - self.columns * self.cell_size / 2,#calcula la posición en píxeles de una celda en la columna j de manera que esté centrada horizontalmente en la pantalla.
                    i * self.cell_size + SCREEN_RESOLUTION[1] / 2 - self.rows * self.cell_size / 2,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(screen,COLORS[self.grid[i][j]], posicion, 
                                 1 if self.grid[i][j] == 0 else 0,) #dibujamos el rectangulo donde va a estar la grilla ; el 1 es el grosor en px de la linea que delimita las celdas

    #Draw current block
        for i, block_row in enumerate(self.block):
            for j, block_element in enumerate(block_row):
                    posicion = (
                    j * self.cell_size + SCREEN_RESOLUTION[0] / 2 - self.columns * self.cell_size / 2,#calcula la posición en píxeles de una celda en la columna j de manera que esté centrada horizontalmente en la pantalla.
                    i * self.cell_size + SCREEN_RESOLUTION[1] / 2 - self.rows * self.cell_size / 2,
                    self.cell_size,
                    self.cell_size,
                                    )
            if block_element != 0:
                pygame.draw.rect(
                    screen, COLORS[block_element], posicion, 0
                )