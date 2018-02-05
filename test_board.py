import board

class Test_Board(object):

    def test_board_create(self):
        self.board_obj = board.Board(30,32,0)
        for r in range(0,30):
            for c in range(0,32):
                assert self.board_obj.board_matrix[r][c] == 0
