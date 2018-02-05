import board

fig1 = ( ((0,0),(0,1),(0,2),(0,3)) ,
        ((0,0),(1,0),(2,0),(3,0)) )
fig2 = (((0,0),(0,1),(0,-1),(1,0)),
        ((0,0),(1,0),(2,0),(1,-1)),
        ((0,0),(1,0),(1,-1),(1,1)),
        ((0,0),(1,0),(1,1),(2,0)))
fig3 = ((0,0),(0,1),(1,0),(1,1))
fig4 = (((0,0),(0,1),(1,1),(1,2)),
        ((0,0),(1,0),(1,-1),(2,-1)))
fig5 = (((0,0),(0,-1),(0,1),(1,1)),
        ((0,0),(1,0),(2,0),(2,-1)),
        ((0,0),(1,0),(1,1),(1,2)),
        ((0,0),(0,1),(1,0),(2,0)))
fig6 = (((0,0),(0,1),(1,0),(1,-1)),
        ((0,0),(1,0),(1,1),(2,1)))
n_rows = board.n_rows
n_cols = board.n_cols

class Fig:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.board = board.get_object()

    def select(self,config,x,y):
        """selects the type of block with specific configuration"""

    def fillPiecePos(self,config,x,y):
        """Fills the matrix corresponding to a particular figure"""

    def check_rotation(self,config,x,y):
        """Checks whether rotation is possible or not"""

class Fig1:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.board = board.get_object()

    def select(self,config,x,y):
        config = config%2
        for i in range(0,4):
            self.draw(x+fig1[config][i][0],y+fig1[config][i][1])

    def fillPiecePos(self,config,x,y):
        config = config%2
        for i in range(0,4):
            self.fix(x+fig1[config][i][0],y+fig1[config][i][1])

    def check_rotation(self,config,x,y):
        config = config%2
        for i in range(0,4):
            if x + fig1[config][i][0] < 0 or x + fig1[config][i][0] > n_rows-1 or y + fig1[config][i][1] < 0 or y + fig1[config][i][1] > n_cols-1:
                return 0
            elif self.board.board_matrix[x + fig1[config][i][0]][y + fig1[config][i][1]] == -1 or self.board.board_matrix[x + fig1[config][i][0]][y + fig1[config][i][1]] == -1:
                return 0
        return 1

class Fig2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.board = board.get_object()

    def select(self,config,x,y):
        config = config%4
        for i in range(0,4):
            self.draw(x+fig2[config][i][0],y+fig2[config][i][1])

    def fillPiecePos(self,config,x,y):
        config = config%4
        for i in range(0,4):
            self.fix(x+fig2[config][i][0],y+fig2[config][i][1])

    def check_rotation(self,config,x,y):
        config = config%4
        for i in range(0,4):
            if x + fig2[config][i][0] < 0 or x + fig2[config][i][0] > n_rows-1 or y + fig2[config][i][1] < 0 or y + fig2[config][i][1] > n_cols-1:
                return 0
            elif self.board.board_matrix[x + fig2[config][i][0]][y + fig2[config][i][1]] == -1 or self.board.board_matrix[x + fig2[config][i][0]][y + fig2[config][i][1]] == -1:
                return 0
        return 1

class Fig3:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.board = board.get_object()
    def select(self,config,x,y):
        self.draw(x,y); self.draw(x,y+1); self.draw(x+1,y); self.draw(x+1,y+1)

    def fillPiecePos(self,config,x,y):
        self.fix(x,y); self.fix(x,y+1); self.fix(x+1,y); self.fix(x+1,y+1)

    def check_rotation(self,config,x,y):
        for i in range(0,4):
            if x + fig3[i][0] < 0 or x + fig3[i][0] > n_rows-1 or y + fig3[i][1] < 0 or y + fig3[i][1] > n_cols-1:
                return 0
            elif self.board.board_matrix[x + fig3[i][0]][y + fig3[i][1]] == -1 or self.board.board_matrix[x + fig3[i][0]][y + fig3[i][1]] == -1:
                return 0
        return 1


class Fig4:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.board = board.get_object()

    def select(self,config,x,y):
        config = config%2
        for i in range(0,4):
            self.draw(x+fig4[config][i][0],y+fig4[config][i][1])

    def fillPiecePos(self,config,x,y):
        config = config%2
        for i in range(0,4):
            self.fix(x+fig4[config][i][0],y+fig4[config][i][1])

    def check_rotation(self,config,x,y):
        config = config%2
        for i in range(0,4):
            if x + fig4[config][i][0] < 0 or x + fig4[config][i][0] > n_rows-1 or y + fig4[config][i][1] < 0 or y + fig4[config][i][1] > n_cols-1:
                return 0
            elif self.board.board_matrix[x + fig4[config][i][0]][y + fig4[config][i][1]] == -1 or self.board.board_matrix[x + fig4[config][i][0]][y + fig4[config][i][1]] == -1:
                return 0
        return 1

class Fig5:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.board = board.get_object()

    def select(self,config,x,y):
        config = config%4
        for i in range(0,4):
            self.draw(x+fig5[config][i][0],y+fig5[config][i][1])

    def fillPiecePos(self,config,x,y):
        config = config%4
        for i in range(0,4):
            self.fix(x+fig5[config][i][0],y+fig5[config][i][1])

    def check_rotation(self,config,x,y):
        config = config%4
        for i in range(0,4):
            if x + fig5[config][i][0] < 0 or x + fig5[config][i][0] > n_rows-1 or y + fig5[config][i][1] < 0 or y + fig5[config][i][1] > n_cols-1:
                return 0
            elif self.board.board_matrix[x + fig5[config][i][0]][y + fig5[config][i][1]] == -1 or self.board.board_matrix[x + fig5[config][i][0]][y + fig5[config][i][1]] == -1:
                return 0
        return 1
class Fig6:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.board = board.get_object()

    def select(self,config,x,y):
        config = config%2
        for i in range(0,4):
            self.draw(x+fig6[config][i][0],y+fig6[config][i][1])


    def fillPiecePos(self,config,x,y):
        config = config%2
        for i in range(0,4):
            self.fix(x+fig6[config][i][0],y+fig6[config][i][1])

    def check_rotation(self,config,x,y):
        config = config%2
        for i in range(0,4):
            if x + fig6[config][i][0] < 0 or x + fig6[config][i][0] > n_rows-1 or y + fig6[config][i][1] < 0 or y + fig6[config][i][1] > n_cols-1:
                return 0
            elif self.board.board_matrix[x + fig6[config][i][0]][y + fig6[config][i][1]] == -1 or self.board.board_matrix[x + fig6[config][i][0]][y + fig6[config][i][1]] == -1:
                return 0
        return 1
