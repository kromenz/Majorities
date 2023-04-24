from games.majorities.player import MajoritiesPlayer
from games.majorities.state import MajoritiesState
from games.game_simulator import GameSimulator


class MajoritiesSimulator(GameSimulator):

    def __init__(self, player1: MajoritiesPlayer, player2: MajoritiesPlayer, num_rows: int = 6, num_cols: int = 7):
        super(MajoritiesSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the Majorities grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return MajoritiesState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: MajoritiesState):
        # ignored for this simulator
        pass

    def end_game(self, state: MajoritiesState):
        # ignored for this simulator
        pass
