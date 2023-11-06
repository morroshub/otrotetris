import pygame
from constants import *
from typing import Literal
import random

block_list = [I_PIECE,J_PIECE,L_PIECE,O_PIECE,T_PIECE,S_PIECE,Z_PIECE]

# Jblock,Lblock,Oblock,Sblock
# logica_rotacion = list(zip(*tblock[::-1])) Esto invierte nuestra lista de [[0,2,0],[2,2,2]] a [[2,2,2],[0,2,0]]
class World:
    def __init__(self) -> None:
        self.end = False 
        self.rows = 20
        self.columns = 10
        self.cell_size = 30
        self.score = 0 
        self.size = (self.columns * self.cell_size, self.rows * self.cell_size)

        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)] # Son tuplas dentro de otra tupla
        #print(self.grid)

        #self.grid[-1] = [1 for _ in range(self.columns)]
        #self.grid[-1][0] = 0
        buffer_block = random.choice(block_list)
        self.next_block = buffer_block.shape
        self.next_block_color = buffer_block.color
        buffer_block = random.choice(block_list)
        self.block = buffer_block.shape
        self.block_color = buffer_block.color
        self.block_offset = [int(self.columns/2)-1, 0]
    
    def move (self, x, y) -> None:
        self.block_offset[0] += x
        if self.collision():
            self.block_offset[0] -=x
        
        self.block_offset[1] += y
        if self.collision():
            self.block_offset[1] -= y
            if self.block_offset[1] <= len(self.block):
                self.end = True
            self.fix_block()
            self.clear_rows()

            self.block = self.next_block
            self.block_color = self.next_block_color
            buffer_block = random.choice(block_list)
            self.next_block = buffer_block.shape
            self.next_block_color = buffer_block.color
            self.block_offset = [int(self.columns/2)-1, 0]
        
    def clear_rows(self) -> None:
        for i, row in enumerate(self.grid):
            if all(row): # (all) Si todos los valores son distintos a null o 0 devuelve True.
                self.grid.pop(i)
                self.grid.insert(0, [0 for _ in range(self.columns)])
                self.score += self.columns
                print(self.score)
    

    def fix_block(self) -> None:
        for i, block_row in enumerate(self.block):
            for j, block_element in enumerate(block_row):
                if block_element != 0:
                    self.grid[i +self.block_offset[1]][j+ self.block_offset[0]] = block_row

        
    def rotate(self) -> None:
        before_state = self.block
        self.block = list(zip(*self.block[::-1]))  # Rotar la pieza
        if self.collision():
            self.block = before_state  # Restaurar la pieza a su estado anterior


    def collision(self) -> Literal[True] | None:
        #Detect end of screen
        if self.block_offset[0] < 0:
            return True
        if self.block_offset[0] >= self.columns - len(self.block[0]) + 1:
            return True
        # Vertical collision
        if self.block_offset[1] > self.rows - len(self.block):
            return True
        # Detect if there are block on the sides
        for i, block_row in enumerate(self.block):
            for j, block_element in enumerate(block_row):
                if block_element != 0:
                    if self.grid[i + self.block_offset[1]][j + self.block_offset[0]] != 0:
                        return True
    

    def draw(self, screen):
        for i in range(0,self.rows):
            for j in range(self.columns):
                posicion = (
                    j * self.cell_size + SCREEN_RESOLUTION[0] / 2 - self.columns * self.cell_size / 2,#calcula la posición en píxeles de una celda en la columna j de manera que esté centrada horizontalmente en la pantalla.
                    i * self.cell_size + SCREEN_RESOLUTION[1] / 2 - self.rows * self.cell_size / 2,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(screen,COLORS[0], posicion, 1 if self.grid[i][j] == 0 else 0) 
        # Draw next block
        for i, block_row in enumerate(self.next_block):
            for j, block_element in enumerate(block_row):
                posicion = (
                    j * self.cell_size + SCREEN_RESOLUTION[0] / 1.9 + self.size[0] / 2 + self.cell_size,
                    i * self.cell_size + SCREEN_RESOLUTION[0] / 2 + self.size[1] / 2 + self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                if block_element != 0:
                    pygame.draw.rect(screen, self.next_block_color, posicion, 0)

        # Draw current block
        for i, block_row in enumerate(self.block):
            for j, block_element in enumerate(block_row):
                posicion = (
                    j * self.cell_size + SCREEN_RESOLUTION[0] / 2 - self.size[0] / 2 + self.block_offset[0] * self.cell_size,
                    i * self.cell_size + SCREEN_RESOLUTION[1] / 2 - self.size[1] / 2 + self.block_offset[1] * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                if block_element != 0:
                    pygame.draw.rect(screen, self.block_color, posicion, 0)
