import board
import block
import figures
import base

class Test_Block(object):

    def test_block_create(self):
        self.board_obj = board.Board(30, 32, 0)
        self.block_obj = block.Block(0,self.board_obj.n_cols/2)
        initial_Xcoor = 0
        initial_Ycoor = self.board_obj.n_cols/2
        for figType in range(1,7):
            for config in range(1,5):
                self.block_obj.selec(figType,config,initial_Xcoor,initial_Ycoor)
                config = config%4
                for i in range(0,4):
                    xCoor = figures.fig[figType-1][config][i][0]
                    yCoor = self.board_obj.n_cols/2 + figures.fig[figType-1][config][i][1]
                    assert self.block_obj.board.board_matrix[xCoor][yCoor] == 1

    def assign_block_coor(self,x,y):
        return ((x,y),(x,y+1),(x+1,y),(x+1,y+1))

    def test_move_block(self):
        self.board_obj = board.Board(30, 32, 0)
        self.block_obj = block.Block(0,self.board_obj.n_cols/2)
        initial_Xcoor = 0
        initial_Ycoor = self.board_obj.n_cols/2
        self.block_obj.selec(3,0,initial_Xcoor,initial_Ycoor) #creating block

        initial_Ycoor -= 1 #moving left
        coor = self.assign_block_coor(initial_Xcoor,initial_Ycoor)
        self.block_obj.board.display_blocks()
        for i in range(0,4):
            assert self.block_obj.board.board_matrix[coor[i][0]][coor[i][1]] == 1

        initial_Xcoor += 1 #moving down
        coor = self.assign_block_coor(initial_Xcoor,initial_Ycoor)
        self.block_obj.board.display_blocks()
        for i in range(0,4):
            assert self.block_obj.board.board_matrix[coor[i][0]][coor[i][1]] == 1

    def test_block_rotate(self):
        self.board_obj = board.Board(30, 32, 0)
        self.block_obj = block.Block(0,self.board_obj.n_cols/2)
        initial_Xcoor = 0
        initial_Ycoor = self.board_obj.n_cols/2
        figType = 1
        config = 0
        self.block_obj.selec(figType,config,initial_Xcoor,initial_Ycoor) #creating block
        config += 1
        self.block_obj.board.display_blocks()
        assert self.block_obj.board.board_matrix[initial_Xcoor][initial_Ycoor] == 1
        assert self.block_obj.board.board_matrix[initial_Xcoor+1][initial_Ycoor] == 1
        assert self.block_obj.board.board_matrix[initial_Xcoor+2][initial_Ycoor] == 1
        assert self.block_obj.board.board_matrix[initial_Xcoor+3][initial_Ycoor] == 1
