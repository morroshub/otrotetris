SCREEN_RESOLUTION = (600, 720)
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

# Define una clase para representar las piezas del Tetris
class TetrisPiece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

# Define las figuras del Tetris como instancias de la clase TetrisPiece
I_PIECE = TetrisPiece([[1, 1, 1, 1]], (0, 255, 255))  # Cian
J_PIECE = TetrisPiece([[0, 0, 1], [1, 1, 1]], (0, 0, 255))  # Azul
L_PIECE = TetrisPiece([[1, 0, 0], [1, 1, 1]], (255, 165, 0))  # Naranja
O_PIECE = TetrisPiece([[1, 1], [1, 1]], (255, 255, 0))  # Amarillo
T_PIECE = TetrisPiece([[0, 1, 0], [1, 1, 1]], (128, 0, 128))  # Púrpura
S_PIECE = TetrisPiece([[0, 1, 1], [1, 1, 0]], (0, 255, 0))  # Verde
Z_PIECE = TetrisPiece([[1, 1, 0], [0, 1, 1]], (255, 0, 0))  # Rojo
