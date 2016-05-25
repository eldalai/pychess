WHITE = 'white'
BLACK = 'black'

CHESS_BOARD_SIZE = 8

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
        if(
            to_col == self.col and
            to_row == (self.row + self.COLOR_DIRECTION[self.color])
        ):
            if not self.board.get_position(to_row, to_col).is_empty:
                raise CellNotEmptyException()

            self.board.move_piece(self, to_row, to_col)
            return

        # double initial move
        if(
            to_col == self.col and
            to_row == (self.row + self.COLOR_DIRECTION[self.color] * 2) and
            self.row == PAWN_INITIAL_ROW[self.color]
        ):
            if not self.board.get_position(to_row, to_col).is_empty:
                raise CellNotEmptyException()
            if not self.board.get_position(to_row - self.COLOR_DIRECTION[self.color], to_col).is_empty:
                raise CellNotEmptyException()

            self.board.move_piece(self, to_row, to_col)
            return

        # eat
        if(
            (
                to_col == self.col - 1 or
                to_col == self.col + 1
            ) and
            to_row == (self.row + self.COLOR_DIRECTION[self.color])
        ):
            if self.board.get_position(to_row, to_col).is_empty:
                raise CellEmptyException()
            if self.board.get_position(to_row, to_col).piece.color == self.color:
                raise InvalidEatException()

            self.board.move_piece(self, to_row, to_col)
            return

        raise InvalidMoveException()


class Rook(Piece):
    PIECE_LETTER = 'r'
    INITIAL_COLUMN = 0

    def move(self, to_row, to_col):
        if(
            (self.row == to_row and self.col != to_col) or
            (self.row != to_row and self.col == to_col)
        ):
            destiny_cell = self.board.get_position(to_row, to_col)
            # eat
            if(
                not destiny_cell.is_empty and
                destiny_cell.piece.color == self.color
            ):
                raise InvalidEatException()

            self.board.move_piece(self, to_row, to_col)
            return

        raise InvalidMoveException()


class Horse(Piece):
    PIECE_LETTER = 'h'
    INITIAL_COLUMN = 1


class Bishop(Piece):
    PIECE_LETTER = 'b'
    INITIAL_COLUMN = 2

    def move(self, to_row, to_col):
        if abs(self.row - to_row) == abs(self.col - to_col):
            destiny_cell = self.board.get_position(to_row, to_col)
            # eat
            if(
                not destiny_cell.is_empty and
                destiny_cell.piece.color == self.color
            ):
                raise InvalidEatException()

            self.board.move_piece(self, to_row, to_col)
            return

        raise InvalidMoveException()


class Queen(Piece):
    PIECE_LETTER = 'q'
    INITIAL_COLUMN = 3


class King(Piece):
    PIECE_LETTER = 'k'
    INITIAL_COLUMN = 4


class BoardFactory(object):

    @classmethod
    def with_pawns(cls, board=None):
        if not board:
            board = Board()
        for col in xrange(0, CHESS_BOARD_SIZE):
            white_pawn = Pawn(board=board, color=WHITE)
            board.set_position(white_pawn, PAWN_INITIAL_ROW[WHITE], col)
            black_pawn = Pawn(board=board, color=BLACK)
            board.set_position(black_pawn, PAWN_INITIAL_ROW[BLACK], col)
        return board

    @classmethod
    def with_rooks(cls, board=None):
        if not board:
            board = Board()
        for col in (Rook.INITIAL_COLUMN, CHESS_BOARD_SIZE - Rook.INITIAL_COLUMN - 1,):
            white_rook = Rook(board=board, color=WHITE)
            board.set_position(white_rook, BIG_PIECES_INITIAL_ROW[WHITE], col)
            black_rook = Rook(board=board, color=BLACK)
            board.set_position(black_rook, BIG_PIECES_INITIAL_ROW[BLACK], col)
        return board


    @classmethod
    def with_horses(cls, board=None):
        if not board:
            board = Board()
        for col in (Horse.INITIAL_COLUMN, CHESS_BOARD_SIZE - Horse.INITIAL_COLUMN - 1,):
            white_horse = Horse(board=board, color=WHITE)
            board.set_position(white_horse, BIG_PIECES_INITIAL_ROW[WHITE], col)
            black_horse = Horse(board=board, color=BLACK)
            board.set_position(black_horse, BIG_PIECES_INITIAL_ROW[BLACK], col)
        return board

    @classmethod
    def with_bishops(cls, board=None):
        if not board:
            board = Board()
        for col in (Bishop.INITIAL_COLUMN, CHESS_BOARD_SIZE - Bishop.INITIAL_COLUMN - 1,):
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

    def __init__(self):
        self.actual_turn = WHITE
        self._board = [
            [Cell(board=self, row=j, col=i) for i in range(CHESS_BOARD_SIZE)]
            for j in range(CHESS_BOARD_SIZE)
        ]

    def get_position(self, row, col):
        return self._board[row][col]

    def set_position(self, piece, row, col):
        self.get_position(row, col).set_piece(piece)

    def move(self, from_row, from_col, to_row, to_col):
        for arg in [from_row, from_col, to_row, to_col]:
            if arg < 0 or arg > CHESS_BOARD_SIZE - 1:
                raise InvalidArgumentException()
        self.get_position(from_row, from_col).move(to_row, to_col)
        if self.actual_turn == WHITE:
            self.actual_turn = BLACK
        else:
            self.actual_turn = WHITE

    def move_piece(self, piece, to_row, to_col):
        self.get_position(piece.row, piece.col).set_empty()
        self.set_position(piece, to_row, to_col)

    def __str__(self):
        _str = 'B*12345678*\n'
        for row in xrange(0, CHESS_BOARD_SIZE):
            _str += '%d|' % (row + 1)
            for col in xrange(0, CHESS_BOARD_SIZE):
                _str += str(self._board[row][col])
            _str += '|\n'

        _str += 'W*--------*\n'
        return _str
