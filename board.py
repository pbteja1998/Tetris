import pygame
from pygame.locals import *

n_rows = 30
n_cols = 32
cell_size = 20
width = (n_rows+2)*(cell_size)
height = (n_cols+1)*(cell_size)
screen = pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Tetris')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

class Board:
    def __init__(self,n_rows,n_cols,score):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.width = width
        self.height = height
        self.score = 0
        self.level = 1
        self.screen = screen
        self.background = background
        self.board_matrix = [ [ 0 for c in range(self.n_cols) ] for r in range(self.n_rows) ]

    def display_blocks(self):
        screen.lock()
        for r in range(n_rows):
            for c in range(n_cols):
                if self.board_matrix[r][c] == 0:
                    pygame.draw.rect(screen, (0,0,0), Rect((c*cell_size,r*cell_size), (cell_size-1,cell_size-1)))
                if self.board_matrix[r][c] == 1 or self.board_matrix[r][c] == -1:
                    pygame.draw.rect(screen, (255,0,0), Rect((c*cell_size,r*cell_size), (cell_size-1,cell_size-1)))
        pygame.display.update()
        screen.unlock()


board = Board(n_rows,n_cols,0)

def get_object():
    return board
