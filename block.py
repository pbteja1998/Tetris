import pygame,sys,os,time,board,figures
from pygame.locals import *
from random import randint
n_rows = board.n_rows
n_cols = board.n_cols

screen = board.screen
background = board.background

class Block(figures.Fig1,figures.Fig2,figures.Fig3,figures.Fig4,figures.Fig5,figures.Fig6):
    def __init__(self,x,y):
        figures.Fig1.__init__(self,x,y)
        figures.Fig2.__init__(self,x,y)
        self.x = x
        self.y = y
        self.board = board.get_object()
    def clean_up(self):
        for r in range(self.board.n_rows):
            for c in range(self.board.n_cols):
                if self.board.board_matrix[r][c] == 1:
                    self.board.board_matrix[r][c] = 0

    def fill(self,figType,config,x,y):
        if figType == 1:
            figures.Fig1.fillPiecePos(self,config,x,y)
        if figType == 2:
            figures.Fig2.fillPiecePos(self,config,x,y)
        if figType == 3:
            figures.Fig3.fillPiecePos(self,config,x,y)
        if figType == 4:
            figures.Fig4.fillPiecePos(self,config,x,y)
        if figType == 5:
            figures.Fig5.fillPiecePos(self,config,x,y)
        if figType == 6:
            figures.Fig6.fillPiecePos(self,config,x,y)

    def draw(self,x,y):
        self.board.board_matrix[x][y]=1

    def fix(self,x,y):
        self.board.board_matrix[x][y]=-1
        self.board.score += 10/(4.0)

    def selec(self,figType,config,x,y):
        if figType == 1:
            figures.Fig1.select(self,config,x,y)
        if figType == 2:
            figures.Fig2.select(self,config,x,y)
        if figType == 3:
            figures.Fig3.select(self,config,x,y)
        if figType == 4:
            figures.Fig4.select(self,config,x,y)
        if figType == 5:
            figures.Fig5.select(self,config,x,y)
        if figType == 6:
            figures.Fig6.select(self,config,x,y)

    def check(self,figType,config,x,y):
        if figType == 1:
            return figures.Fig1.check_rotation(self,config,x,y)
        if figType == 2:
            return figures.Fig2.check_rotation(self,config,x,y)
        if figType == 3:
            return figures.Fig3.check_rotation(self,config,x,y)
        if figType == 4:
            return figures.Fig4.check_rotation(self,config,x,y)
        if figType == 5:
            return figures.Fig5.check_rotation(self,config,x,y)
        if figType == 6:
            return figures.Fig6.check_rotation(self,config,x,y)

    def checkPiecePos(self,a):
        for r in range(0,n_rows):
            for c in range(0,n_cols):
                if a == 'l': #checking left wall
                    if self.board.board_matrix[r][c] == 1 and self.board.board_matrix[r+1][c-1] == -1 or self.board.board_matrix[r][0] == 1:
                        return 1
                elif a == 'r': #checking right wall
                    if self.board.board_matrix[r][c] == 1 and self.board.board_matrix[r+1][c+1] == -1 or self.board.board_matrix[r][n_cols-1] == 1:
                        return -1
                elif a == 'h': #checking bottom wall
                    if self.board.board_matrix[r][c] == 1 and self.board.board_matrix[r+1][c] == -1 or self.board.board_matrix[n_rows-1][c] == 1:
                        return 1
                else:
                    if self.board.board_matrix[0][c] == -1:
                        return 1
