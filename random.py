from random import randint

from tictactoe.action import TictTacToeAction
from tictactoe.player import TicTacToePlayer
from tictactoe.state import TicTacToeState
from tictactoe.state import State


class RandomTicTaCToePlayer(TicTacToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TicTacToeState):
        return TicTacToeAction(randint(0, state.get_num_cols()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
