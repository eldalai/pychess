import unittest

WHITE = 'white'
BLACK = 'black'


class MoveException(Exception):
    pass


class CellEmptyException(MoveException):
    pass


class InvalidTurnException(MoveException):
    pass


class Cell(object):
    def __init__(self, board):
        self._piece = None
        self._board = board

    def set_piece(self, piece):
        self._piece = piece

    def set_empty(self):
        self._piece = None

    def move(self, to_row, to_col):
        if not self._piece:
            raise CellEmptyException()
        if self._board.actual_turn != self._piece.color:
            raise InvalidTurnException()

        self._piece.move(to_row, to_col)

    def __str__(self):
        if self._piece:
            return str(self._piece)
        else:
            return ' '


class Piece(object):
    def __init__(self, board, color, row, col):
        self.board = board
        self.color = color
        self.row = row
        self.col = col

    def set_position(self, to_x, to_y):
        self.row = to_x
        self.col = to_y

    def __str__(self):
        if self.color == WHITE:
            return self.PIECE_LETTER.upper()
        else:
            return self.PIECE_LETTER.lower()


class Pawn(Piece):
    PIECE_LETTER = 'p'
    COLOR_DIRECTION = {
        WHITE: -1,
        BLACK: +1,
    }

    def move(self, to_row, to_col):
        # simple move
        if to_col != self.col:
            raise MoveException()
        if(
            to_col == self.col and
            to_row == (self.row + self.COLOR_DIRECTION[self.color])
        ):
            self.board.set_piece(self, to_row, to_col)
            return

        raise MoveException()


class Board(object):

    def __init__(self):
        self.actual_turn = WHITE
        self._board = [[Cell(board=self) for i in range(8)] for j in range(8)]
        for col in xrange(0, 8):
            white_pawn = Pawn(board=self, color=WHITE, row=6, col=col)
            self.set_position(white_pawn, 6, col)
            black_pawn = Pawn(board=self, color=BLACK, row=1, col=col)
            self.set_position(black_pawn, 1, col)

    def get_position(self, col, row):
        return self._board[col][row]

    def set_position(self, piece, col, row):
        self.get_position(col, row).set_piece(piece)
        piece.set_position(col, row)

    def move(self, from_col, from_row, to_col, to_row):
        self.get_position(from_col, from_row).move(to_col, to_row)
        if self.actual_turn == WHITE:
            self.actual_turn = BLACK
        else:
            self.actual_turn = WHITE

    def set_piece(self, piece, to_col, to_row):
        self.get_position(piece.row, piece.col).set_empty()
        self.set_position(piece, to_col, to_row)

    def __str__(self):
        _str = 'B*12345678*\n'
        for row in xrange(0, 8):
            _str += '%d|' % (row + 1)
            for col in xrange(0, 8):
                _str += str(self._board[row][col])
            _str += '|\n'

        _str += 'W*--------*\n'
        return _str


class TestChess(unittest.TestCase):

    def test_board_with_pawns(self):
        board = Board()
        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppppppp|\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|PPPPPPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_move__unexistence_pawn(self):
        board = Board()

        with self.assertRaises(CellEmptyException):
            board.move(0, 0, 1, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppppppp|\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|PPPPPPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_color_move_pawn(self):
        board = Board()

        with self.assertRaises(InvalidTurnException):
            board.move(1, 3, 2, 3)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppppppp|\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|PPPPPPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_simple_move_pawn(self):
        board = Board()

        board.move(6, 3, 5, 3)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppppppp|\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|   P    |\n'\
            '7|PPP PPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_simple_move_pawn_twice(self):
        board = Board()

        board.move(6, 3, 5, 3)
        board.move(1, 3, 2, 3)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|ppp pppp|\n'\
            '3|   p    |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|   P    |\n'\
            '7|PPP PPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )


if __name__ == '__main__':
    unittest.main()
