import unittest

from .pgn import PGN


class PortableGameNotationTests(unittest.TestCase):

    def setUp(self):
        self.pgn_content = (
            '''
            [Event "Great Britain"]
            [Site "Great Britain"]
            [Date "1844.??.??"]
            [Round "?"]
            [White "Seligo"]
            [Black "Anderssen, Adolf"]
            [Result "1-0"]
            [WhiteElo ""]
            [BlackElo ""]
            [ECO "C26"]

            1.e4 e5 2.Bc4 Nf6 3.Nc3 Bc5 4.h3 O-O 5.a3 c6 6.Nf3 d5 7.exd5 cxd5 8.Ba2 Nc6
            9.O-O e4 10.Nh2 Qd6 11.d3 Qg3 12.Ne2 Qg6 13.Kh1 Nh5 14.d4 Bd6 15.f4 Be6 16.Qe1 f5
            17.b3 Rf6 18.c4 Qf7 19.Be3 Rg6 20.Qh4 Qf8 21.Qxh5 Be7 22.Nc3 Rg4 23.hxg4 g6
            24.Qh3 fxg4 25.Qg3 h5 26.cxd5 h4 27.Qe1 Bf5 28.dxc6  1-0

            '''
        )

    def test_parse_pgn(self):
        full_pgn_content = (
            '''
            [Event "Great Britain"]
            [Site "Great Britain"]
            [Date "1844.??.??"]
            [Round "?"]
            [White "Seligo"]
            [Black "Anderssen, Adolf"]
            [Result "1-0"]
            [WhiteElo ""]
            [BlackElo ""]
            [ECO "C26"]

            1.e4 e5 2.Bc4 Nf6 3.Nc3 Bc5 4.h3 O-O 5.a3 c6 6.Nf3 d5 7.exd5 cxd5 8.Ba2 Nc6
            9.O-O e4 10.Nh2 Qd6 11.d3 Qg3 12.Ne2 Qg6 13.Kh1 Nh5 14.d4 Bd6 15.f4 Be6 16.Qe1 f5
            17.b3 Rf6 18.c4 Qf7 19.Be3 Rg6 20.Qh4 Qf8 21.Qxh5 Be7 22.Nc3 Rg4 23.hxg4 g6
            24.Qh3 fxg4 25.Qg3 h5 26.cxd5 h4 27.Qe1 Bf5 28.dxc6  1-0

            [Event "Breslau m"]
            [Site "Breslau"]
            [Date "1846.??.??"]
            [Round "?"]
            [White "Von Heydebrand und der L, Tassilo"]
            [Black "Anderssen, Adolf"]
            [Result "1-0"]
            [WhiteElo ""]
            [BlackElo ""]
            [ECO "C39"]

            1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 h5 6.Bc4 Rh7 7.d4 Qf6 8.Nc3 Ne7
            9.O-O Bh6 10.g3 d6 11.Nxf7 Rxf7 12.Bxf7+ Qxf7 13.Bxf4 Bxf4 14.Rxf4 Qg7 15.Qd3 Be6
            16.d5 Bg8 17.Qb5+ Nd7 18.Qxb7 Qd4+ 19.Kg2 Rb8 20.Qxc7 Rxb2 21.Rf2 Nc5 22.Raf1 Nd7
            23.Re2 Ne5 24.a4 Bh7 25.Rd1 Qc4 26.Qxc4 Nxc4 27.Nb5 Ng6 28.Nxa7 Ra2 29.Rb1 Rxa4
            30.Rb8+ Kf7 31.Rb7+ Kg8 32.Kf2 Nge5 33.Nc6 Ra3 34.Rb8+ Kg7 35.Rb7+ Kh6 36.Nxe5 dxe5
            37.Rb4 Nd6 38.Rb6 Rf3+ 39.Ke1 Rf6 40.c4 Kg7 41.c5 Nxe4 42.c6 Rf7 43.Rb4 Nd6
            44.Rxe5 Bf5 45.Ke2 Kf6 46.Re3 Re7 47.Rxe7 Kxe7 48.Ke3  1-0
            '''
        )

        pgn_parsed = PGN(full_pgn_content)
        self.assertEqual(len(pgn_parsed.games), 2)
        self.assertIn(
            '[Event "Great Britain"]',
            pgn_parsed.games[0].content,
        )
        self.assertIn(
            '28.dxc6  1-0',
            pgn_parsed.games[0].content,
        )
        self.assertIn(
            '[Event "Breslau m"]',
            pgn_parsed.games[1].content,
        )
        self.assertIn(
            'Kxe7 48.Ke3  1-0',
            pgn_parsed.games[1].content,
        )


if __name__ == '__main__':
    unittest.main()
