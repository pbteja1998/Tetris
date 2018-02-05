import pygame,sys,os,time

from pygame.locals import *
from random import randint
import block, board

n_rows = board.n_rows
n_cols = board.n_cols
width = board.width
height = board.height

pygame.init()
screen = board.screen
background = board.background

class GamePlay(block.Block,board.Board):
    def __init__(self,board):
        self.score = board.score
        self.board = board
        self.speed = 1
        self.initial_speed = 0.3
        self.pause = 0

    def checkRowFull(self):
        for r in range(0,n_rows):
            flag = 1
            for c in range(0,n_cols):
                if self.board.board_matrix[r][c] != -1:
                    flag = 0
            if flag == 1:
                board.score += 100
                del board.board_matrix[r]
                row=[0 for s in range(n_cols)] #creating empty row
                board.board_matrix.insert(0,row) #inserting above created row

    def text_objects(self,text, font):
        textSurface = font.render(text, True,(0,0,255), (255,255,255))
        return textSurface, textSurface.get_rect()

    def message_display(self,text,center,fontSize):
        largeText = pygame.font.Font('freesansbold.ttf',fontSize)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = center
        self.board.display_blocks()
        screen.blit(background,(0,0))
        screen.blit(TextSurf, TextRect)
        self.board.display_blocks()
        pygame.display.update()
        time.sleep(0.4)

    def pygame_events(self):
        while True:

            if board.level == 11:
                self.message_display("Game Over",(width/2,height-20),50)
                break

            screen.blit(background,(0,0))

            if board.score == 0:
                self.message_display('Level: %s'%board.level,(width/2,height-20),50)

            self.checkRowFull()

            self.message_display('Score: %d'%int(board.score),(width/2,height-20),50)

            if board.score >= board.level*50*(board.level+1):
                board.level += 1
                if self.initial_speed <= 0.1:
                    self.initial_speed -= 0.01
                else:
                    self.initial_speed -= 0.1
                self.message_display('Level: %s'%board.level,(width/2,height-20),50)

            xCoor = 0
            yCoor = n_cols/2
            left = 0
            right = 0
            figType = randint(1,6)
            config = randint(1,4)
            screen.blit(background,(0,0))

            if not self.check(figType,config,xCoor,yCoor):
                self.message_display("Game Over",(width/2,height-20),50)
                print "Score:",int(board.score)
                break
            self.selec(figType,config,xCoor,yCoor)
            self.board.display_blocks()
            self.speed = 1

            while True:
                if self.checkPiecePos('h'):
                    self.fill(figType,config,xCoor,yCoor)
                    break
                else:
                    xCoor = xCoor + 1

                screen.blit(background,(0,0))

                for event in pygame.event.get():
                    screen.blit(background,(0,0))

                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == KEYDOWN:

                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()

                        if event.key == K_a: #if "A" is pressed
                            if not self.checkPiecePos('l'):
                                left = -1

                        if event.key == K_d: #if "D" is pressed
                            if not self.checkPiecePos('r'):
                                right = 1

                        if event.key == K_SPACE: #if "SPACEBAR" is pressed
                            self.speed = 100

                        if event.key == K_s and figType!=3:
                            config = config + 1
                            if not self.check(figType,config,xCoor,yCoor):
                                config = config - 1

                self.clean_up()
                time.sleep(float(self.initial_speed)/self.speed) #stop for 0.1/spped amount of time

                yCoor = yCoor + left + right
                left = right = 0
                self.selec(figType,config,xCoor,yCoor)
                self.board.display_blocks()

board = board.get_object()
block = block.Block(0,n_cols/2)
board.display_blocks()
game = GamePlay(board)
game.pygame_events()
