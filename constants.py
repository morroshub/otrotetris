SCREEN_RESOLUTION = (400, 500)
FPS = 30
LIGHT_BLACK = (64, 64, 64)

#BLOQUES - COLORES

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)


COLORS = [BLACK, RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE, PURPLE, GRAY, WHITE]


# Dimensiones de piezas
BLOCK_SIZE = 20  # Tamaño de las celdas de la cuadrícula
PIECE_SIZE = 4   # Tamaño de las piezas del Tetris (4x4)

# Matriz de ejemplos de piezas del Tetris
I_PIECE = [
    [1, 1, 1, 1],
]

J_PIECE = [
    [0, 0, 1],
    [1, 1, 1],
]

L_PIECE = [
    [1, 0, 0],
    [1, 1, 1],
]

O_PIECE = [
    [1, 1],
    [1, 1],
]

T_PIECE = [
    [0, 1, 0],
    [1, 1, 1],
]

S_PIECE = [
    [0, 1, 1],
    [1, 1, 0],
]

Z_PIECE = [
    [1, 1, 0],
    [0, 1, 1],
]