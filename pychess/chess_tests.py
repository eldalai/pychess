import unittest

from chess import (
    WHITE,
    BLACK,
    Board,
    BoardFactory,
    CellEmptyException,
    CellNotEmptyException,
    InvalidArgumentException,
    InvalidEatException,
    InvalidMoveException,
    InvalidTurnException,
    ChessException,
    Pawn,
)


class TestBigBoard(unittest.TestCase):

    def test_board_16_16(self):
        board = Board(size=16)
        expected_board = \
            'B*1234567890123456*\n' \
            '1|                |\n'\
            '2|                |\n'\
            '3|                |\n'\
            '4|                |\n'\
            '5|                |\n'\
            '6|                |\n'\
            '7|                |\n'\
            '8|                |\n'\
            '9|                |\n'\
            '0|                |\n'\
            '1|                |\n'\
            '2|                |\n'\
            '3|                |\n'\
            '4|                |\n'\
            '5|                |\n'\
            '6|                |\n'\
            'W*----------------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_board_16_16_with_pawns(self):
        board = BoardFactory.size_16_with_pawns()
        expected_board = \
            'B*1234567890123456*\n' \
            '1|                |\n'\
            '2|                |\n'\
            '3|pppppppppppppppp|\n'\
            '4|pppppppppppppppp|\n'\
            '5|                |\n'\
            '6|                |\n'\
            '7|                |\n'\
            '8|                |\n'\
            '9|                |\n'\
            '0|                |\n'\
            '1|                |\n'\
            '2|                |\n'\
            '3|PPPPPPPPPPPPPPPP|\n'\
            '4|PPPPPPPPPPPPPPPP|\n'\
            '5|                |\n'\
            '6|                |\n'\
            'W*----------------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_board_16_16_with_pawns_rooks(self):
        board = BoardFactory.size_16_with_pawns()
        board = BoardFactory.size_16_with_rooks(board)
        expected_board = \
            'B*1234567890123456*\n' \
            '1|rr            rr|\n'\
            '2|rr            rr|\n'\
            '3|pppppppppppppppp|\n'\
            '4|pppppppppppppppp|\n'\
            '5|                |\n'\
            '6|                |\n'\
            '7|                |\n'\
            '8|                |\n'\
            '9|                |\n'\
            '0|                |\n'\
            '1|                |\n'\
            '2|                |\n'\
            '3|PPPPPPPPPPPPPPPP|\n'\
            '4|PPPPPPPPPPPPPPPP|\n'\
            '5|RR            RR|\n'\
            '6|RR            RR|\n'\
            'W*----------------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_board_16_16_with_pawns_rooks_horses(self):
        board = BoardFactory.size_16_with_pawns()
        board = BoardFactory.size_16_with_rooks(board)
        board = BoardFactory.size_16_with_horses(board)
        expected_board = \
            'B*1234567890123456*\n' \
            '1|rrhh        hhrr|\n'\
            '2|rrhh        hhrr|\n'\
            '3|pppppppppppppppp|\n'\
            '4|pppppppppppppppp|\n'\
            '5|                |\n'\
            '6|                |\n'\
            '7|                |\n'\
            '8|                |\n'\
            '9|                |\n'\
            '0|                |\n'\
            '1|                |\n'\
            '2|                |\n'\
            '3|PPPPPPPPPPPPPPPP|\n'\
            '4|PPPPPPPPPPPPPPPP|\n'\
            '5|RRHH        HHRR|\n'\
            '6|RRHH        HHRR|\n'\
            'W*----------------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_board_16_16_with_pawns_rooks_horses_bishops(self):
        board = BoardFactory.size_16_with_pawns()
        board = BoardFactory.size_16_with_rooks(board)
        board = BoardFactory.size_16_with_horses(board)
        board = BoardFactory.size_16_with_bishops(board)
        expected_board = \
            'B*1234567890123456*\n' \
            '1|rrhhbb    bbhhrr|\n'\
            '2|rrhhbb    bbhhrr|\n'\
            '3|pppppppppppppppp|\n'\
            '4|pppppppppppppppp|\n'\
            '5|                |\n'\
            '6|                |\n'\
            '7|                |\n'\
            '8|                |\n'\
            '9|                |\n'\
            '0|                |\n'\
            '1|                |\n'\
            '2|                |\n'\
            '3|PPPPPPPPPPPPPPPP|\n'\
            '4|PPPPPPPPPPPPPPPP|\n'\
            '5|RRHHBB    BBHHRR|\n'\
            '6|RRHHBB    BBHHRR|\n'\
            'W*----------------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_board_16_16_with_pawns_rooks_horses_bishops_queens(self):
        board = BoardFactory.size_16_with_pawns()
        board = BoardFactory.size_16_with_rooks(board)
        board = BoardFactory.size_16_with_horses(board)
        board = BoardFactory.size_16_with_bishops(board)
        board = BoardFactory.size_16_with_queens(board)
        expected_board = \
            'B*1234567890123456*\n' \
            '1|rrhhbbqq  bbhhrr|\n'\
            '2|rrhhbbqq  bbhhrr|\n'\
            '3|pppppppppppppppp|\n'\
            '4|pppppppppppppppp|\n'\
            '5|                |\n'\
            '6|                |\n'\
            '7|                |\n'\
            '8|                |\n'\
            '9|                |\n'\
            '0|                |\n'\
            '1|                |\n'\
            '2|                |\n'\
            '3|PPPPPPPPPPPPPPPP|\n'\
            '4|PPPPPPPPPPPPPPPP|\n'\
            '5|RRHHBBQQ  BBHHRR|\n'\
            '6|RRHHBBQQ  BBHHRR|\n'\
            'W*----------------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_board_16_16_with_pawns_rooks_horses_bishop_queens_kings(self):
        board = BoardFactory.size_16_with_pawns()
        board = BoardFactory.size_16_with_rooks(board)
        board = BoardFactory.size_16_with_horses(board)
        board = BoardFactory.size_16_with_bishops(board)
        board = BoardFactory.size_16_with_queens(board)
        board = BoardFactory.size_16_with_kings(board)
        expected_board = \
            'B*1234567890123456*\n' \
            '1|rrhhbbqqkkbbhhrr|\n'\
            '2|rrhhbbqqkkbbhhrr|\n'\
            '3|pppppppppppppppp|\n'\
            '4|pppppppppppppppp|\n'\
            '5|                |\n'\
            '6|                |\n'\
            '7|                |\n'\
            '8|                |\n'\
            '9|                |\n'\
            '0|                |\n'\
            '1|                |\n'\
            '2|                |\n'\
            '3|PPPPPPPPPPPPPPPP|\n'\
            '4|PPPPPPPPPPPPPPPP|\n'\
            '5|RRHHBBQQKKBBHHRR|\n'\
            '6|RRHHBBQQKKBBHHRR|\n'\
            'W*----------------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_board_16_16_complete(self):
        board = BoardFactory.size_16()
        expected_board = \
            'B*1234567890123456*\n' \
            '1|rrhhbbqqkkbbhhrr|\n'\
            '2|rrhhbbqqkkbbhhrr|\n'\
            '3|pppppppppppppppp|\n'\
            '4|pppppppppppppppp|\n'\
            '5|                |\n'\
            '6|                |\n'\
            '7|                |\n'\
            '8|                |\n'\
            '9|                |\n'\
            '0|                |\n'\
            '1|                |\n'\
            '2|                |\n'\
            '3|PPPPPPPPPPPPPPPP|\n'\
            '4|PPPPPPPPPPPPPPPP|\n'\
            '5|RRHHBBQQKKBBHHRR|\n'\
            '6|RRHHBBQQKKBBHHRR|\n'\
            'W*----------------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )


class TestBoard(unittest.TestCase):

    def test_empty_board(self):
        board = Board()
        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_board_invalid_argument(self):
        board = BoardFactory.with_pawns()
        with self.assertRaises(InvalidArgumentException):
            board.move(-1, 1, 1, 1)

        with self.assertRaises(InvalidArgumentException):
            board.move(8, 1, 2, 2)

        with self.assertRaises(InvalidArgumentException):
            board.move(6, -1, 3, 3)

        with self.assertRaises(InvalidArgumentException):
            board.move(4, 10, 4, 4)

        with self.assertRaises(InvalidArgumentException):
            board.move(6, 3, -1, 4)

        with self.assertRaises(InvalidArgumentException):
            board.move(6, 3, 5, -4)

        with self.assertRaises(InvalidArgumentException):
            board.move(6, 3, 6, 3)


class TestPawns(unittest.TestCase):

    def test_board_with_pawns(self):
        board = BoardFactory.with_pawns()
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

    def test_try_move_unexistence_pawn(self):
        board = BoardFactory.with_pawns()

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
        board = BoardFactory.with_pawns()

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
        board = BoardFactory.with_pawns()
        # move white pawn
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
        board = BoardFactory.with_pawns()

        # move white pawn
        board.move(6, 3, 5, 3)
        # move black pawn
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

    def test_simple_move_pawn_twice_black_again(self):
        board = BoardFactory.with_pawns()

        # move white pawn
        board.move(6, 3, 5, 3)
        # try to move black pawn again
        with self.assertRaises(InvalidTurnException):
            board.move(5, 3, 4, 3)
        # move black pawn
        board.move(1, 3, 2, 3)
        # try to move black pawn again
        with self.assertRaises(InvalidTurnException):
            board.move(2, 3, 2, 4)

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

    def test_simple_move_pawn_still_stop_by_piece(self):
        board = BoardFactory.with_pawns()

        # move white pawn
        board.move(6, 3, 5, 3)
        # move black pawn
        board.move(1, 3, 2, 3)
        # move white pawn
        board.move(5, 3, 4, 3)
        # move black pawn
        board.move(2, 3, 3, 3)

        with self.assertRaises(CellNotEmptyException):
            # try to move white pawn over black pawn
            board.move(4, 3, 3, 3)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|ppp pppp|\n'\
            '3|        |\n'\
            '4|   p    |\n'\
            '5|   P    |\n'\
            '6|        |\n'\
            '7|PPP PPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_pawn_eat_pawn(self):
        board = BoardFactory.with_pawns()

        # move white pawn
        board.move(6, 3, 5, 3)
        # move black pawn
        board.move(1, 4, 2, 4)
        # move white pawn
        board.move(5, 3, 4, 3)
        # move black pawn
        board.move(2, 4, 3, 4)

        # white pawn eat black pawn
        board.move(4, 3, 3, 4)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppp ppp|\n'\
            '3|        |\n'\
            '4|    P   |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|PPP PPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_pawn_invalid_eat(self):
        board = BoardFactory.with_pawns()

        # move white pawn
        board.move(6, 3, 5, 3)
        # move black pawn
        board.move(1, 4, 2, 4)
        # move white pawn
        board.move(5, 3, 4, 3)
        # move black pawn
        board.move(2, 4, 3, 4)

        with self.assertRaises(CellEmptyException):
            # white pawn try eat empty cell
            board.move(4, 3, 3, 2)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppp ppp|\n'\
            '3|        |\n'\
            '4|    p   |\n'\
            '5|   P    |\n'\
            '6|        |\n'\
            '7|PPP PPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_pawn_invalid_eat_same_color(self):
        board = BoardFactory.with_pawns()

        # move white pawn
        board.move(6, 3, 5, 3)
        # move black pawn
        board.move(1, 4, 2, 4)
        with self.assertRaises(InvalidEatException):
            # white pawn try eat same color
            board.move(6, 2, 5, 3)
        with self.assertRaises(InvalidEatException):
            # white pawn try eat same color
            board.move(6, 4, 5, 3)
        # move white pawn
        board.move(6, 0, 5, 0)

        with self.assertRaises(InvalidEatException):
            # black pawn try eat same color
            board.move(1, 3, 2, 4)
        with self.assertRaises(InvalidEatException):
            # black pawn try eat same color
            board.move(1, 5, 2, 4)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppp ppp|\n'\
            '3|    p   |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|P  P    |\n'\
            '7| PP PPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_double_initial_move_pawn(self):
        board = BoardFactory.with_pawns()
        # move white pawn
        board.move(6, 3, 4, 3)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppppppp|\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|   P    |\n'\
            '6|        |\n'\
            '7|PPP PPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_double_initial_move_pawn_twice(self):
        board = BoardFactory.with_pawns()
        # double move white pawn
        board.move(6, 3, 4, 3)
        # double move black pawn
        board.move(1, 4, 3, 4)
        with self.assertRaises(InvalidMoveException):
            # double move white pawn
            board.move(4, 3, 2, 3)
        board.move(4, 3, 3, 3)
        with self.assertRaises(InvalidMoveException):
            # double move white pawn
            board.move(3, 4, 5, 4)
        board.move(3, 4, 4, 4)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppp ppp|\n'\
            '3|        |\n'\
            '4|   P    |\n'\
            '5|    p   |\n'\
            '6|        |\n'\
            '7|PPP PPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_double_move_pawn_still_stop_by_piece(self):
        board = BoardFactory.with_pawns()

        # move white pawn
        board.move(6, 3, 4, 3)
        # move black pawn
        board.move(1, 4, 3, 4)
        # move white pawn
        board.move(4, 3, 3, 3)
        # move black pawn
        board.move(3, 4, 4, 4)

        with self.assertRaises(CellNotEmptyException):
            # try to move white pawn over black pawn
            board.move(6, 4, 4, 4)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppp ppp|\n'\
            '3|        |\n'\
            '4|   P    |\n'\
            '5|    p   |\n'\
            '6|        |\n'\
            '7|PPP PPPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_double_move_pawn_or_simple(self):
        board = BoardFactory.with_pawns()

        # move white pawn
        board.move(6, 3, 4, 3)
        # move black pawn
        board.move(1, 4, 3, 4)
        # move white pawn
        board.move(4, 3, 3, 3)
        # move black pawn
        board.move(3, 4, 4, 4)
        # move white pawn
        board.move(6, 4, 5, 4)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|pppp ppp|\n'\
            '3|        |\n'\
            '4|   P    |\n'\
            '5|    p   |\n'\
            '6|    P   |\n'\
            '7|PPP  PPP|\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )


class TestRooks(unittest.TestCase):

    def test_board_with_rooks(self):
        board = BoardFactory.with_rooks()
        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|R      R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_move_unexistence_rook(self):
        board = BoardFactory.with_rooks()

        with self.assertRaises(CellEmptyException):
            board.move(1, 1, 2, 2)

        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|R      R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_color_move_rook(self):
        board = BoardFactory.with_rooks()

        with self.assertRaises(InvalidTurnException):
            board.move(0, 0, 0, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|R      R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_diagonal_move_rook(self):
        board = BoardFactory.with_rooks()

        with self.assertRaises(InvalidMoveException):
            board.move(7, 0, 6, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|R      R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_move_rook(self):
        board = BoardFactory.with_rooks()

        with self.assertRaises(InvalidMoveException):
            board.move(7, 0, 5, 4)

        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|R      R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_same_color_move_rook(self):
        board = BoardFactory.with_rooks()

        with self.assertRaises(InvalidEatException):
            board.move(7, 0, 7, 7)

        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|R      R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_simple_move_rook_up(self):
        board = BoardFactory.with_rooks()

        board.move(7, 0, 6, 0)

        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|R       |\n'\
            '8|       R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_simple_move_rook_twice(self):
        board = BoardFactory.with_rooks()

        # move white rook up
        board.move(7, 0, 6, 0)
        # move black rook down
        board.move(0, 0, 1, 0)

        expected_board = \
            'B*12345678*\n' \
            '1|       r|\n'\
            '2|r       |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|R       |\n'\
            '8|       R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_simple_move_rook_twice_black_again(self):
        board = BoardFactory.with_rooks()

        # move white rook up
        board.move(7, 0, 6, 0)
        # try to move black pawn again
        with self.assertRaises(InvalidTurnException):
            board.move(6, 0, 5, 0)

        # move black rook down
        board.move(0, 0, 1, 0)
        # try to move black pawn again
        with self.assertRaises(InvalidTurnException):
            board.move(1, 0, 2, 0)

        expected_board = \
            'B*12345678*\n' \
            '1|       r|\n'\
            '2|r       |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|R       |\n'\
            '8|       R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_rook_eat_rook(self):
        board = BoardFactory.with_rooks()
        # white rook eat black rook
        board.move(7, 0, 0, 0)
        # black rook eat white rook
        board.move(0, 7, 7, 7)

        expected_board = \
            'B*12345678*\n' \
            '1|R       |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|       r|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_invalid_move_vertical_rook_another_in_middle(self):
        board = BoardFactory.with_rooks()

        white_pawn = Pawn(board=board, color=WHITE)
        board.set_position(white_pawn, 6, 0)
        black_pawn = Pawn(board=board, color=BLACK)
        board.set_position(black_pawn, 5, 0)

        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|p       |\n'\
            '7|P       |\n'\
            '8|R      R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

        # move white rook a little
        with self.assertRaises(InvalidMoveException):
            board.move(7, 0, 5, 0)

        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|p       |\n'\
            '7|P       |\n'\
            '8|R      R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_invalid_move_horizontal_rook_another_in_middle(self):
        board = BoardFactory.with_rooks()

        white_pawn = Pawn(board=board, color=WHITE)
        board.set_position(white_pawn, 7, 1)
        black_pawn = Pawn(board=board, color=BLACK)
        board.set_position(black_pawn, 7, 2)
        white_pawn = Pawn(board=board, color=WHITE)
        board.set_position(white_pawn, 7, 3)

        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|RPpP   R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

        # move white rook a little
        with self.assertRaises(InvalidMoveException):
            board.move(7, 0, 7, 2)
        # move white rook a little
        with self.assertRaises(InvalidMoveException):
            board.move(7, 7, 7, 2)

        expected_board = \
            'B*12345678*\n' \
            '1|r      r|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|RPpP   R|\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )


class TestHorses(unittest.TestCase):

    def test_board_with_horses(self):
        board = BoardFactory.with_horses()
        expected_board = \
            'B*12345678*\n' \
            '1| h    h |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8| H    H |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_move_unexistence_horse(self):
        board = BoardFactory.with_horses()

        with self.assertRaises(CellEmptyException):
            board.move(1, 1, 2, 2)

        expected_board = \
            'B*12345678*\n' \
            '1| h    h |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8| H    H |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_color_move_horse(self):
        board = BoardFactory.with_horses()

        with self.assertRaises(InvalidTurnException):
            board.move(0, 1, 1, 1)

        expected_board = \
            'B*12345678*\n' \
            '1| h    h |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8| H    H |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_vertical_move_horse(self):
        board = BoardFactory.with_horses()

        with self.assertRaises(InvalidMoveException):
            board.move(7, 1, 6, 1)

        expected_board = \
            'B*12345678*\n' \
            '1| h    h |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8| H    H |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_simple_move_horse(self):
        board = BoardFactory.with_horses()

        board.move(7, 1, 5, 2)

        expected_board = \
            'B*12345678*\n' \
            '1| h    h |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|  H     |\n'\
            '7|        |\n'\
            '8|      H |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_simple_move_horse_with_jump(self):
        board = BoardFactory.with_horses()
        BoardFactory.with_pawns(board)

        board.move(7, 1, 5, 2)

        expected_board = \
            'B*12345678*\n' \
            '1| h    h |\n'\
            '2|pppppppp|\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|  H     |\n'\
            '7|PPPPPPPP|\n'\
            '8|      H |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

        board.move(0, 1, 2, 0)
        expected_board = \
            'B*12345678*\n' \
            '1|      h |\n'\
            '2|pppppppp|\n'\
            '3|h       |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|  H     |\n'\
            '7|PPPPPPPP|\n'\
            '8|      H |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

        board.move(5, 2, 3, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|      h |\n'\
            '2|pppppppp|\n'\
            '3|h       |\n'\
            '4| H      |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|PPPPPPPP|\n'\
            '8|      H |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )
        board.move(2, 0, 3, 2)
        board.move(3, 1, 2, 3)

        expected_board = \
            'B*12345678*\n' \
            '1|      h |\n'\
            '2|pppppppp|\n'\
            '3|   H    |\n'\
            '4|  h     |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|PPPPPPPP|\n'\
            '8|      H |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )


class TestBishops(unittest.TestCase):

    def test_board_with_bishops(self):
        board = BoardFactory.with_bishops()
        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|  B  B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_move_unexistence_bishop(self):
        board = BoardFactory.with_bishops()

        with self.assertRaises(CellEmptyException):
            board.move(1, 1, 2, 2)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|  B  B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_color_move_bishop(self):
        board = BoardFactory.with_bishops()

        with self.assertRaises(InvalidTurnException):
            board.move(0, 2, 1, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|  B  B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_horizontal_move_bishop(self):
        board = BoardFactory.with_bishops()

        with self.assertRaises(InvalidMoveException):
            board.move(7, 2, 7, 1)
        with self.assertRaises(InvalidMoveException):
            board.move(7, 2, 7, 3)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|  B  B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_vertical_move_bishop(self):
        board = BoardFactory.with_bishops()

        with self.assertRaises(InvalidMoveException):
            board.move(7, 2, 6, 2)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|  B  B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_move_bishop(self):
        board = BoardFactory.with_bishops()

        with self.assertRaises(InvalidMoveException):
            board.move(7, 2, 5, 5)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|  B  B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_same_color_move_bishop(self):
        board = BoardFactory.with_pawns()
        board = BoardFactory.with_bishops(board)

        with self.assertRaises(InvalidEatException):
            board.move(7, 2, 6, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|pppppppp|\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|PPPPPPPP|\n'\
            '8|  B  B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_simple_move_bishop(self):
        board = BoardFactory.with_bishops()

        board.move(7, 2, 6, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7| B      |\n'\
            '8|     B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_simple_move_twice_bishop(self):
        board = BoardFactory.with_bishops()

        # move white bishop up
        board.move(7, 2, 6, 1)
        # move black bishop down
        board.move(0, 2, 1, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|     b  |\n'\
            '2| b      |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7| B      |\n'\
            '8|     B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_simple_move_bishop_twice_black_again(self):
        board = BoardFactory.with_bishops()

        # move white bishop
        board.move(7, 2, 6, 1)
        # try to move white bishop again
        with self.assertRaises(InvalidTurnException):
            board.move(6, 1, 5, 2)

        # move black bishop down
        board.move(0, 2, 1, 1)
        # try to move black bishop again
        with self.assertRaises(InvalidTurnException):
            board.move(1, 1, 2, 2)

        expected_board = \
            'B*12345678*\n' \
            '1|     b  |\n'\
            '2| b      |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7| B      |\n'\
            '8|     B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_bishop_eat_bishop(self):
        board = BoardFactory.with_bishops()

        black_pawn = Pawn(board=board, color=BLACK)
        board.set_position(black_pawn, 6, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7| p      |\n'\
            '8|  B  B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

        # move white bishop
        board.move(7, 2, 6, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7| B      |\n'\
            '8|     B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_invalid_move_bishop_another_in_middle(self):
        board = BoardFactory.with_bishops()

        white_pawn = Pawn(board=board, color=WHITE)
        board.set_position(white_pawn, 6, 1)
        black_pawn = Pawn(board=board, color=BLACK)
        board.set_position(black_pawn, 5, 0)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|p       |\n'\
            '7| P      |\n'\
            '8|  B  B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

        # move white bishop
        with self.assertRaises(InvalidMoveException):
            board.move(7, 2, 5, 0)

        expected_board = \
            'B*12345678*\n' \
            '1|  b  b  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|p       |\n'\
            '7| P      |\n'\
            '8|  B  B  |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )


class TestQueens(unittest.TestCase):

    def test_board_with_queen(self):
        board = BoardFactory.with_queens()
        expected_board = \
            'B*12345678*\n' \
            '1|   q    |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|   Q    |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_invalid_color_move_queen(self):
        board = BoardFactory.with_queens()

        with self.assertRaises(InvalidTurnException):
            board.move(0, 3, 1, 1)

        expected_board = \
            'B*12345678*\n' \
            '1|   q    |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|   Q    |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_horizontal_move(self):
        board = BoardFactory.with_queens()

        board.move(7, 3, 7, 1)
        board.move(0, 3, 0, 7)

        expected_board = \
            'B*12345678*\n' \
            '1|       q|\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8| Q      |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_vertical_move_queen(self):
        board = BoardFactory.with_queens()

        board.move(7, 3, 6, 3)
        board.move(0, 3, 3, 3)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|   q    |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|   Q    |\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_diagonal_move_queen(self):
        board = BoardFactory.with_queens()

        board.move(7, 3, 5, 5)

        expected_board = \
            'B*12345678*\n' \
            '1|   q    |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|     Q  |\n'\
            '7|        |\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )


class TestKings(unittest.TestCase):

    def test_board_with_king(self):
        board = BoardFactory.with_kings()
        expected_board = \
            'B*12345678*\n' \
            '1|    k   |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|    K   |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_horizontal_move(self):
        board = BoardFactory.with_kings()

        board.move(7, 4, 7, 3)
        board.move(0, 4, 0, 5)

        expected_board = \
            'B*12345678*\n' \
            '1|     k  |\n'\
            '2|        |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|        |\n'\
            '8|   K    |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_vertical_move_queen(self):
        board = BoardFactory.with_kings()

        board.move(7, 4, 6, 4)
        board.move(0, 4, 1, 4)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|    k   |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|    K   |\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

    def test_try_diagonal_move_king(self):
        board = BoardFactory.with_kings()

        board.move(7, 4, 6, 3)
        board.move(0, 4, 1, 5)

        expected_board = \
            'B*12345678*\n' \
            '1|        |\n'\
            '2|     k  |\n'\
            '3|        |\n'\
            '4|        |\n'\
            '5|        |\n'\
            '6|        |\n'\
            '7|   K    |\n'\
            '8|        |\n'\
            'W*--------*\n'

        self.assertEquals(
            str(board),
            expected_board
        )

if __name__ == '__main__':
    unittest.main()
