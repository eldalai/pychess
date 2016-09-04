WHITE = 'white'
BLACK = 'black'

DEFAULT_CHESS_BOARD_SIZE = 8
CHESS_BOARD_SIZE_16 = 16
CHESS_BOARD_SIZE_32 = 32

PAWN_INITIAL_ROW = {
    WHITE: 6,
    BLACK: 1,
}

BIG_PIECES_INITIAL_ROW = {
    WHITE: 7,
    BLACK: 0,
}


class ChessException(Exception):
    pass


class CellEmptyException(ChessException):
    pass


class CellNotEmptyException(ChessException):
    pass


class InvalidTurnException(ChessException):
    pass


class InvalidMoveException(ChessException):
    pass


class InvalidEatException(ChessException):
    pass


class InvalidArgumentException(ChessException):
    pass


class Cell(object):
    def __init__(self, board, row, col):
        self._piece = None
        self._board = board
        self.row = row
        self.col = col

    def set_piece(self, piece):
        self._piece = piece
        piece.set_cell(self)

    @property
    def piece(self):
        return self._piece

    def get_piece(self):
        return self._piece

    def set_empty(self):
        self._piece = None

    @property
    def is_empty(self):
        return self._piece is None

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
    def __init__(self, board, color):
        self.board = board
        self.color = color

    def set_cell(self, cell):
        self._cell = cell

    @property
    def row(self):
        return self._cell.row

    @property
    def col(self):
        return self._cell.col

    def is_horizontal_move(self, to_row, to_col):
        return(
            (self.row == to_row and self.col != to_col) or
            (self.row != to_row and self.col == to_col)
        )

    def is_diagonal_move(self, to_row, to_col):
        return abs(self.row - to_row) == abs(self.col - to_col)

    def _do_move(
        self,
        to_row,
        to_col,
        jump=False,
        should_eat=False,
        should_not_eat=False,
    ):
        destiny_cell = self.board.get_position(to_row, to_col)
        if(
            destiny_cell.is_empty and
            should_eat
        ):
            raise CellEmptyException
        if(
            not destiny_cell.is_empty and
            should_not_eat
        ):
            raise CellNotEmptyException
        # eat
        if(
            not destiny_cell.is_empty and
            destiny_cell.piece.color == self.color
        ):
            raise InvalidEatException()

        self.board.move_piece(self, to_row, to_col, jump)

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

    def __init__(self, board, color):
        super(Pawn, self).__init__(board, color)
        self._moved = False

    def _do_move(
        self,
        to_row,
        to_col,
        jump=False,
        should_eat=False,
        should_not_eat=False,
    ):
        super(Pawn, self)._do_move(to_row, to_col, jump, should_eat, should_not_eat)
        self._moved = True

    def move(self, to_row, to_col):
        # simple move
        if(
            to_col == self.col and
            to_row == (self.row + self.COLOR_DIRECTION[self.color])
        ):
            return self._do_move(to_row, to_col, should_not_eat=True)

        # double initial move
        if(
            to_col == self.col and
            to_row == (self.row + self.COLOR_DIRECTION[self.color] * 2) and
            not self._moved
        ):
            return self._do_move(to_row, to_col, should_not_eat=True)

        # eat
        if(
            abs(to_col - self.col) == 1 and
            to_row == (self.row + self.COLOR_DIRECTION[self.color])
        ):
            return self._do_move(to_row, to_col, should_eat=True)

        raise InvalidMoveException()


class Rook(Piece):
    PIECE_LETTER = 'r'
    INITIAL_COLUMN = 0

    def move(self, to_row, to_col):
        if not self.is_horizontal_move(to_row, to_col):
            raise InvalidMoveException()
        self._do_move(to_row, to_col)


class Horse(Piece):
    PIECE_LETTER = 'h'
    INITIAL_COLUMN = 1

    def move(self, to_row, to_col):
        if not (
            abs(self.row - to_row) == 2 and abs(self.col - to_col) == 1 or
            abs(self.row - to_row) == 1 and abs(self.col - to_col) == 2
        ):
            raise InvalidMoveException()
        self._do_move(to_row, to_col, jump=True)


class Bishop(Piece):
    PIECE_LETTER = 'b'
    INITIAL_COLUMN = 2

    def move(self, to_row, to_col):
        if not self.is_diagonal_move(to_row, to_col):
            raise InvalidMoveException()
        self._do_move(to_row, to_col)


class Queen(Piece):
    PIECE_LETTER = 'q'
    INITIAL_COLUMN = 3

    def move(self, to_row, to_col):
        if(
            not self.is_diagonal_move(to_row, to_col) and
            not self.is_horizontal_move(to_row, to_col)
        ):
            raise InvalidMoveException()
        self._do_move(to_row, to_col)


class King(Piece):
    PIECE_LETTER = 'k'
    INITIAL_COLUMN = 4

    def move(self, to_row, to_col):
        if(
            not self.is_diagonal_move(to_row, to_col) and
            not self.is_horizontal_move(to_row, to_col) and
            abs(self.row - to_row) > 1 and
            abs(self.col - to_col) > 1
        ):
            raise InvalidMoveException()
        self._do_move(to_row, to_col)


class BoardFactory(object):

    @classmethod
    def with_pawns(cls, board=None):
        if not board:
            board = Board()
        for col in xrange(0, DEFAULT_CHESS_BOARD_SIZE):
            white_pawn = Pawn(board=board, color=WHITE)
            board.set_position(white_pawn, PAWN_INITIAL_ROW[WHITE], col)
            black_pawn = Pawn(board=board, color=BLACK)
            board.set_position(black_pawn, PAWN_INITIAL_ROW[BLACK], col)
        return board

    @classmethod
    def size_16_with_pawns(cls, board=None):
        if not board:
            board = Board(CHESS_BOARD_SIZE_16)
        cells_prop = CHESS_BOARD_SIZE_16 / DEFAULT_CHESS_BOARD_SIZE
        for col in xrange(0, CHESS_BOARD_SIZE_16):
            for row in range(cells_prop):  # 0, 1
                white_pawn = Pawn(board=board, color=WHITE)
                board.set_position(white_pawn, PAWN_INITIAL_ROW[WHITE] * cells_prop + row, col)
                white_pawn = Pawn(board=board, color=BLACK)
                board.set_position(white_pawn, PAWN_INITIAL_ROW[BLACK] * cells_prop + row, col)
        return board

    @classmethod
    def size_16_with_rooks(cls, board=None):
        return cls.size_16_with_big_pieces(Rook, board)

    @classmethod
    def size_16_with_horses(cls, board=None):
        return cls.size_16_with_big_pieces(Horse, board)

    @classmethod
    def size_16_with_bishops(cls, board=None):
        return cls.size_16_with_big_pieces(Bishop, board)

    @classmethod
    def size_16_with_queens(cls, board=None):
        return cls.size_16_with_big_pieces(Queen, board, mirror_positions=False)

    @classmethod
    def size_16_with_kings(cls, board=None):
        return cls.size_16_with_big_pieces(King, board, mirror_positions=False)

    @classmethod
    def size_16(cls, board=None):
        board = cls.size_16_with_pawns()
        board = cls.size_16_with_rooks(board)
        board = cls.size_16_with_horses(board)
        board = cls.size_16_with_bishops(board)
        board = cls.size_16_with_queens(board)
        board = cls.size_16_with_kings(board)
        return board

    @classmethod
    def size_16_with_big_pieces(cls, piece_class, board=None, mirror_positions=True):
        if not board:
            board = Board(CHESS_BOARD_SIZE_16)
        cells_prop = CHESS_BOARD_SIZE_16 / DEFAULT_CHESS_BOARD_SIZE

        piece_positions = [piece_class.INITIAL_COLUMN * cells_prop]
        if mirror_positions:
            piece_positions.append(CHESS_BOARD_SIZE_16 - piece_class.INITIAL_COLUMN * cells_prop - cells_prop)

        for col in range(0, 2):
            for row in range(cells_prop):  # 0, 1
                for piece_position in piece_positions:
                    white_rook = piece_class(board=board, color=WHITE)
                    board.set_position(
                        white_rook,
                        BIG_PIECES_INITIAL_ROW[WHITE] * cells_prop + row,
                        col + piece_position
                    )
                    black_rook = piece_class(board=board, color=BLACK)
                    board.set_position(
                        black_rook,
                        BIG_PIECES_INITIAL_ROW[BLACK] * cells_prop + row,
                        col + piece_position
                    )
        return board

    @classmethod
    def with_rooks(cls, board=None):
        if not board:
            board = Board()
        for col in (Rook.INITIAL_COLUMN, DEFAULT_CHESS_BOARD_SIZE - Rook.INITIAL_COLUMN - 1,):
            white_rook = Rook(board=board, color=WHITE)
            board.set_position(white_rook, BIG_PIECES_INITIAL_ROW[WHITE], col)
            black_rook = Rook(board=board, color=BLACK)
            board.set_position(black_rook, BIG_PIECES_INITIAL_ROW[BLACK], col)
        return board


    @classmethod
    def with_horses(cls, board=None):
        if not board:
            board = Board()
        for col in (Horse.INITIAL_COLUMN, DEFAULT_CHESS_BOARD_SIZE - Horse.INITIAL_COLUMN - 1,):
            white_horse = Horse(board=board, color=WHITE)
            board.set_position(white_horse, BIG_PIECES_INITIAL_ROW[WHITE], col)
            black_horse = Horse(board=board, color=BLACK)
            board.set_position(black_horse, BIG_PIECES_INITIAL_ROW[BLACK], col)
        return board

    @classmethod
    def with_bishops(cls, board=None):
        if not board:
            board = Board()
        for col in (Bishop.INITIAL_COLUMN, DEFAULT_CHESS_BOARD_SIZE - Bishop.INITIAL_COLUMN - 1,):
            white_bishop = Bishop(board=board, color=WHITE)
            board.set_position(white_bishop, BIG_PIECES_INITIAL_ROW[WHITE], col)
            black_bishop = Bishop(board=board, color=BLACK)
            board.set_position(black_bishop, BIG_PIECES_INITIAL_ROW[BLACK], col)
        return board

    @classmethod
    def with_queens(cls, board=None):
        if not board:
            board = Board()
        white_queen = Queen(board=board, color=WHITE)
        board.set_position(white_queen, BIG_PIECES_INITIAL_ROW[WHITE], Queen.INITIAL_COLUMN)
        black_queen = Queen(board=board, color=BLACK)
        board.set_position(black_queen, BIG_PIECES_INITIAL_ROW[BLACK], Queen.INITIAL_COLUMN)
        return board


    @classmethod
    def with_kings(cls, board=None):
        if not board:
            board = Board()
        white_king = King(board=board, color=WHITE)
        board.set_position(white_king, BIG_PIECES_INITIAL_ROW[WHITE], King.INITIAL_COLUMN)
        black_king = King(board=board, color=BLACK)
        board.set_position(black_king, BIG_PIECES_INITIAL_ROW[BLACK], King.INITIAL_COLUMN)
        return board


class Board(object):

    def __init__(self, size=DEFAULT_CHESS_BOARD_SIZE):
        self.actual_turn = WHITE
        self.size = size
        self._board = [
            [Cell(board=self, row=j, col=i) for i in range(size)]
            for j in range(size)
        ]

    def get_position(self, row, col):
        return self._board[row][col]

    def set_position(self, piece, row, col):
        self.get_position(row, col).set_piece(piece)

    def move(self, from_row, from_col, to_row, to_col):
        if from_row == to_row and to_col == from_col:
            raise InvalidArgumentException()
        for arg in [from_row, from_col, to_row, to_col]:
            if arg < 0 or arg > self.size - 1:
                raise InvalidArgumentException()
        self.get_position(from_row, from_col).move(to_row, to_col)
        if self.actual_turn == WHITE:
            self.actual_turn = BLACK
        else:
            self.actual_turn = WHITE

    def move_piece(self, piece, to_row, to_col, jump=False):
        if not jump:
            if piece.row == to_row:
                row_range = [to_row]
            else:
                step_row = -1 if piece.row > to_row else 1
                row_range = range(piece.row, to_row, step_row)

            if piece.col == to_col:
                col_range = [to_col]
            else:
                step_col = -1 if piece.col > to_col else 1
                col_range = range(piece.col, to_col, step_col)

            for mid_row in row_range:
                for mid_col in col_range:
                    if(
                        not(mid_row == piece.row and mid_col == piece.col) and
                        not self.get_position(mid_row, mid_col).is_empty
                    ):
                        raise InvalidMoveException()
        self.get_position(piece.row, piece.col).set_empty()
        self.set_position(piece, to_row, to_col)

    def __str__(self):
        _str = 'B*{}*\n'.format(
            ''.join([str(a % 10) for a in xrange(1, self.size + 1)])
        )
        for row in xrange(1, self.size + 1):
            _str += '%d|' % (row % 10)
            for col in xrange(1, self.size + 1):
                _str += str(self._board[row - 1][col - 1])
            _str += '|\n'

        _str += 'W*{}*\n'.format('-' * self.size)
        return _str
