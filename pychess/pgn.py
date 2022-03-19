
class PGN_Game:
    def __init__(self, pgn_game_content):
        self.content = pgn_game_content


class PGN:
    def __init__(self, pgn_content):
        self.games = []
        event_index = pgn_content.find('[Event')
        while event_index > -1:
            game_content_start = event_index
            event_index = pgn_content.find('[Event', event_index + 1)
            game_content_end = event_index - 1
            self.games.append(
                PGN_Game(pgn_content[game_content_start:game_content_end])
            )
