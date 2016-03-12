import unittest

from chess import (
    Board,
    BoardFactory,
    CellEmptyException,
    CellNotEmptyException,
    InvalidArgumentException,
    InvalidTurnException,
    MoveException,
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
        with self.assertRaises(MoveException):
            # double move white pawn
            board.move(4, 3, 2, 3)
        board.move(4, 3, 3, 3)
        with self.assertRaises(MoveException):
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


if __name__ == '__main__':
    unittest.main()
