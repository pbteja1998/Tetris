import board
import base

class Test_Gameplay(object):
    def test_row_clear(self):
        self.board_obj = board.Board(30, 32, 0)
        self.gameplay_obj = base.GamePlay(self.board_obj)
        for c in range(0,32):
            self.gameplay_obj.board.board_matrix[29][c] = -1

        row = self.gameplay_obj.board.board_matrix[28]
        print row

        self.gameplay_obj.checkRowFull()

        assert base.board.score == 100
        for c in range(0,30):
            assert base.board.board_matrix[29][c] == row[c]
    
