WHITE = 'white'
BLACK = 'black'

DEFAULT_CHESS_BOARD_SIZE = 8
CHESS_BOARD_SIZE_16 = 16
CHESS_BOARD_SIZE_32 = 32

SHORT_CASTING_COL = 6
LONG_CASTING_COL = 2

PAWN_INITIAL_ROW = {
    WHITE: 6,
    BLACK: 1,
}

BIG_PIECES_INITIAL_ROW = {
    WHITE: 7,
    BLACK: 0,
}

PROMOTE_PAWN_ROWS = {
    DEFAULT_CHESS_BOARD_SIZE: (0, 7),
    CHESS_BOARD_SIZE_16: (8, 7),
}

RESULT_MOVE = 'moved'
RESULT_EAT = 'eat'
RESULT_PROMOTE = 'promote'
RESULT_CHECK = 'check'
RESULT_CHECKMATE = 'checkmate'

STATUS_PLAYING = 'playing'
STATUS_FINISH = 'playing'
STATUS_DRAW = 'draw'
STATUS_WIN = '{} wins'
STATUS_WHITE_WIN = STATUS_WIN.format(WHITE)
STATUS_BLACK_WIN = STATUS_WIN.format(BLACK)


def get_opposite_color(color):
    return BLACK if color == WHITE else WHITE


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


class InvalidCheckException(ChessException):
    pass


class InvalidPromoteException(ChessException):
    pass


class InvalidCastlingException(ChessException):
    pass


class InvalidStatusException(ChessException):
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
            (self.row == to_row and self.col != to_col)
            or (self.row != to_row and self.col == to_col)
        )

    def is_diagonal_move(self, to_row, to_col):
        return abs(self.row - to_row) == abs(self.col - to_col)

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

    def evaluate_move(self, to_row, to_col):
        # simple move
        if(
            to_col == self.col
            and to_row == (self.row + self.COLOR_DIRECTION[self.color])
        ):
            return (
                True,  # valid_move
                True,  # should_not_eat
                False,  # should_eat
                False,  # jump
                False,  # castling
                to_row in PROMOTE_PAWN_ROWS[self.board.size],  # promote
            )

        pawn_initial_row = PAWN_INITIAL_ROW[self.color]  # 6 (white) or 1 (black)
        cells_prop = self.board.size // DEFAULT_CHESS_BOARD_SIZE  # 16 or 8  / 8
        pawn_initial_rows = [
            pawn_initial_row * cells_prop + count
            for count in range(cells_prop)  # 2 or 1
        ]
        # double initial move
        if(
            to_col == self.col
            and to_row == (self.row + self.COLOR_DIRECTION[self.color] * 2)
            and self.row in pawn_initial_rows
            # not self._moved
        ):
            return (
                True,  # valid_move
                True,  # should_not_eat
                False,  # should_eat
                False,  # jump
                False,  # castling
                False,  # promote
            )

        # eat
        if(
            abs(to_col - self.col) == 1
            and to_row == (self.row + self.COLOR_DIRECTION[self.color])
        ):
            return (
                True,  # valid_move
                False,  # should_not_eat
                True,  # should_eat
                False,  # jump
                False,  # castling
                to_row in PROMOTE_PAWN_ROWS[self.board.size],  # promote
            )

        return (
            False,  # valid_move
            False,  # should_not_eat
            False,  # should_eat
            False,  # jump
            False,  # castling
            False,  # promote
        )


class Rook(Piece):
    PIECE_LETTER = 'r'
    INITIAL_COLUMN = 0

    def evaluate_move(self, to_row, to_col):
        return (
            self.is_horizontal_move(to_row, to_col),  # valid_move
            False,  # should_not_eat
            False,  # should_eat
            False,  # jump
            False,  # castling
            False,  # promote
        )


class Horse(Piece):
    PIECE_LETTER = 'h'
    INITIAL_COLUMN = 1

    def evaluate_move(self, to_row, to_col):
        valid_move = (
            abs(self.row - to_row) == 2 and abs(self.col - to_col) == 1
            or abs(self.row - to_row) == 1 and abs(self.col - to_col) == 2
        )
        return (
            valid_move,  # valid_move
            False,  # should_not_eat
            False,  # should_eat
            True,  # jump
            False,  # castling
            False,  # promote
        )


class Bishop(Piece):
    PIECE_LETTER = 'b'
    INITIAL_COLUMN = 2

    def evaluate_move(self, to_row, to_col):
        return (
            self.is_diagonal_move(to_row, to_col),  # valid_move
            False,  # should_not_eat
            False,  # should_eat
            False,  # jump
            False,  # castling
            False,  # promote
        )


class Queen(Piece):
    PIECE_LETTER = 'q'
    INITIAL_COLUMN = 3

    def evaluate_move(self, to_row, to_col):
        return (
            self.is_diagonal_move(to_row, to_col)
            or self.is_horizontal_move(to_row, to_col),  # valid_move
            False,  # should_not_eat
            False,  # should_eat
            False,  # jump
            False,  # castling
            False,  # promote
        )


class King(Piece):
    PIECE_LETTER = 'k'
    INITIAL_COLUMN = 4

    def evaluate_move(self, to_row, to_col):
        # castling
        # if not self.moved TODO
        if (
            self.board.size == DEFAULT_CHESS_BOARD_SIZE
            and abs(self.col - to_col) == 2
            and self.row == BIG_PIECES_INITIAL_ROW[self.color]
        ):
            return (
                True,  # valid_move
                False,  # should_not_eat
                False,  # should_eat
                False,  # jump
                True,  # castling
                False,  # promote
            )

        return (
            abs(self.row - to_row) == 1
            or abs(self.col - to_col) == 1,  # valid_move
            False,  # should_not_eat
            False,  # should_eat
            False,  # jump
            False,  # castling
            False,  # promote
        )


PIECES_BY_STR = {
    Pawn.PIECE_LETTER: Pawn,
    Rook.PIECE_LETTER: Rook,
    Horse.PIECE_LETTER: Horse,
    Bishop.PIECE_LETTER: Bishop,
    Queen.PIECE_LETTER: Queen,
    King.PIECE_LETTER: King,
}


class BoardFactory(object):

    @classmethod
    def with_pawns(cls, board=None):
        if not board:
            board = Board()
        for col in range(0, DEFAULT_CHESS_BOARD_SIZE):
            white_pawn = Pawn(board=board, color=WHITE)
            board.set_position(white_pawn, PAWN_INITIAL_ROW[WHITE], col)
            black_pawn = Pawn(board=board, color=BLACK)
            board.set_position(black_pawn, PAWN_INITIAL_ROW[BLACK], col)
        return board

    @classmethod
    def size_16_with_pawns(cls, board=None):
        if not board:
            board = Board(CHESS_BOARD_SIZE_16)
        cells_prop = int(CHESS_BOARD_SIZE_16 / DEFAULT_CHESS_BOARD_SIZE)
        for col in range(0, CHESS_BOARD_SIZE_16):
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
        cells_prop = int(CHESS_BOARD_SIZE_16 / DEFAULT_CHESS_BOARD_SIZE)

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

    @classmethod
    def size_8(cls):
        board = cls.with_pawns()
        board = cls.with_rooks(board)
        board = cls.with_horses(board)
        board = cls.with_bishops(board)
        board = cls.with_queens(board)
        board = cls.with_kings(board)
        return board

    @classmethod
    def deserialize(cls, serialized_board):
        board = Board(serialized_board['size'])
        board.actual_turn = serialized_board['actual_turn']
        for row in range(board.size):
            for col in range(board.size):
                piece_position = row * board.size + col
                serialized_piece = serialized_board['board'][piece_position]
                piece_class = PIECES_BY_STR.get(serialized_piece.lower(), None)
                if piece_class:
                    color = BLACK if serialized_piece.islower() else WHITE
                    board.set_position(piece_class(board=board, color=color), row, col)
        return board


class Board(object):

    def __init__(self, size=DEFAULT_CHESS_BOARD_SIZE, actual_turn=WHITE):
        self.actual_turn = actual_turn
        self.size = size
        self._board = [
            [Cell(board=self, row=j, col=i) for i in range(size)]
            for j in range(size)
        ]
        self.status = STATUS_PLAYING

    def get_position(self, row, col):
        return self._board[row][col]

    def set_position(self, piece, row, col):
        self.get_position(row, col).set_piece(piece)

    def validate_move_destiny(
        self,
        to_row,
        to_col,
        piece,
        should_not_eat=False,
        should_eat=False,
    ):
        destiny_cell = self.get_position(to_row, to_col)
        if(
            destiny_cell.is_empty
            and should_eat
        ):
            raise CellEmptyException
        if(
            not destiny_cell.is_empty
            and should_not_eat
        ):
            raise CellNotEmptyException
        # eat
        if(
            not destiny_cell.is_empty
            and destiny_cell.piece.color == piece.color
        ):
            raise InvalidEatException()

    def _validate_move_args(self, from_row, from_col, to_row, to_col):
        if from_row == to_row and to_col == from_col:
            return False
        for arg in [from_row, from_col, to_row, to_col]:
            if arg < 0 or arg > self.size - 1:
                return False
        return True

    def get_piece_to_move(self, from_row, from_col):
        cell = self.get_position(from_row, from_col)
        if not cell.piece:
            raise CellEmptyException()
        if self.actual_turn != cell.piece.color:
            raise InvalidTurnException()
        return cell.piece

    def validate_move(self, piece, to_row, to_col):
        (
            valid_move,
            should_not_eat,
            should_eat,
            jump,
            castling,
            promote,
        ) = piece.evaluate_move(to_row, to_col)
        if not valid_move:
            raise InvalidMoveException()
        self.validate_move_destiny(
            to_row,
            to_col,
            piece,
            should_not_eat,
            should_eat,
        )
        if not jump:
            self._verify_piece_in_path(piece, to_row, to_col)
        return castling, promote

    def _move(self, from_row, from_col, to_row, to_col, promotion_piece=None):
        if not self._validate_move_args(from_row, from_col, to_row, to_col):
            raise InvalidArgumentException()
        piece = self.get_piece_to_move(from_row, from_col)

        castling, promote = self.validate_move(piece, to_row, to_col)
        if promote:
            if self.size != DEFAULT_CHESS_BOARD_SIZE:
                if not promotion_piece:
                    promotion_piece = Queen.PIECE_LETTER
                else:
                    raise InvalidPromoteException()
            else:
                if not promotion_piece:
                    raise InvalidPromoteException()
        if castling:
            if to_col == SHORT_CASTING_COL:
                castling_rook_position = self.get_position(to_row, DEFAULT_CHESS_BOARD_SIZE - 1)
            else:
                castling_rook_position = self.get_position(to_row, 0)
            if(
                castling_rook_position.is_empty
                or not isinstance(castling_rook_position.piece, Rook)
                or not castling_rook_position.piece.color == piece.color
            ):
                raise InvalidCastlingException()
        return self.move_piece(piece, to_row, to_col, castling, promote, promotion_piece)

    def move(self, from_row, from_col, to_row, to_col, promotion_piece=None):
        if self.status != STATUS_PLAYING:
            raise InvalidStatusException('Game is over. Status is {}'.format(self.status))
        (
            move_result,
            revert_move_args,
        ) = self._move(from_row, from_col, to_row, to_col, promotion_piece)
        self.actual_turn = get_opposite_color(self.actual_turn)
        if self.is_check():
            if self.is_checkmate():
                self.status = STATUS_WIN.format(
                    get_opposite_color(self.actual_turn)
                )
                return (RESULT_CHECKMATE, King.PIECE_LETTER)
            piece = revert_move_args[0]
            return (RESULT_CHECK, piece.PIECE_LETTER)
        return move_result

    def _verify_piece_in_path(self, piece, to_row, to_col):
        if piece.row == to_row:
            step_row = 0
        else:
            step_row = -1 if piece.row > to_row else 1

        if piece.col == to_col:
            step_col = 0
        else:
            step_col = -1 if piece.col > to_col else 1

        mid_col = piece.col + step_col
        mid_row = piece.row + step_row
        while mid_col != to_col or mid_row != to_row:
            if not self.get_position(mid_row, mid_col).is_empty:
                raise InvalidMoveException()
            mid_col += step_col
            mid_row += step_row

    def get_color_pieces(self, color):
        pieces = []
        for row in self._board:
            for cell in row:
                if (
                    not cell.is_empty
                    and cell.piece.color == color
                ):
                    pieces.append(cell.piece)
        return pieces

    def get_king(self, color):
        for row in self._board:
            for cell in row:
                if (
                    not cell.is_empty
                    and cell.piece.color == color
                    and isinstance(cell.piece, King)
                ):
                    return cell.piece

    def _get_all_positions(self):
        result = []
        for row in range(self.size):
            for col in range(self.size):
                result.append((row, col,))
        return result

    def is_checkmate(self):
        for piece in self.get_color_pieces(self.actual_turn):
            for to_row, to_col in self._get_all_positions():
                try:
                    (
                        move_result,
                        revert_move_args,
                    ) = self._move(piece.row, piece.col, to_row, to_col, 'q')
                    if not self.is_check():
                        self._revert_move(*revert_move_args)
                        return False
                except Exception:
                    pass  # Invalid move
        return True

    def is_check(self):
        actual_turn_king = self.get_king(self.actual_turn)
        if not actual_turn_king:
            # testing... not real
            return False
        for piece in self.get_color_pieces(
            get_opposite_color(self.actual_turn)
        ):
            try:
                self.validate_move(piece, actual_turn_king.row, actual_turn_king.col)
                return True
            except Exception:
                pass
        return False

    def move_piece(self, piece, to_row, to_col, castling, promote, promotion_piece):
        from_row = piece.row
        from_col = piece.col
        self.get_position(piece.row, piece.col).set_empty()
        new_position = self.get_position(to_row, to_col)
        if new_position.is_empty:
            move_result = (RESULT_MOVE, piece.PIECE_LETTER)
            eaten_piece = None
        else:
            move_result = (RESULT_EAT, new_position.piece.PIECE_LETTER)
            eaten_piece = new_position.piece

        if not promote:
            new_position.set_piece(piece)
        else:
            piece_class = PIECES_BY_STR[promotion_piece]
            new_position.set_piece(piece_class(self, self.actual_turn))

        if castling:
            if to_col == SHORT_CASTING_COL:
                castling_rook_position = self.get_position(to_row, DEFAULT_CHESS_BOARD_SIZE - 1)
                castling_rook = castling_rook_position.piece
                castling_rook_position.set_empty()
                self.set_position(castling_rook, to_row, SHORT_CASTING_COL - 1)
            else:
                castling_rook_position = self.get_position(to_row, 0)
                castling_rook = castling_rook_position.piece
                castling_rook_position.set_empty()
                self.set_position(castling_rook, to_row, LONG_CASTING_COL + 1)
        if self.size == DEFAULT_CHESS_BOARD_SIZE:
            if self.is_check():
                # # if check, revert move
                self._revert_move(piece, from_row, from_col, eaten_piece, to_row, to_col)
                # TODO: revert rook move on castling rook
                raise InvalidCheckException()
        return (
            move_result,
            (piece, from_row, from_col, eaten_piece, to_row, to_col,)
        )

    def _revert_move(self, piece, from_row, from_col, eaten_piece, to_row, to_col):
        self.set_position(piece, from_row, from_col)
        if eaten_piece:
            self.set_position(eaten_piece, to_row, to_col)
        else:
            self.get_position(to_row, to_col).set_empty()

    def __str__(self):
        _str = 'B*{}*\n'.format(
            ''.join([str(a % 10) for a in range(1, self.size + 1)])
        )
        for row in range(1, self.size + 1):
            _str += '%d|' % (row % 10)
            for col in range(1, self.size + 1):
                _str += str(self._board[row - 1][col - 1])
            _str += '|\n'

        _str += 'W*{}*\n'.format('-' * self.size)
        return _str

    def get_simple(self):
        _str = ''
        for row in range(self.size):
            for col in range(self.size):
                _str += str(self._board[row][col])
        return _str

    def serialize(self):
        return {
            'actual_turn': self.actual_turn,
            'size': self.size,
            'board': self.get_simple(),
        }
