from random import randint

from games.majorities.action import MajoritiesAction
from games.majorities.player import MajoritiesPlayer
from games.majorities.state import MajoritiesState
from games.state import State


class RandomMajoritiesPlayer(MajoritiesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: MajoritiesState, playerV):
        jogada = randint(1, 15)
        z=state.validate_action(self,MajoritiesAction,jogada)
        if z == True:
            while  z == True:
                jogada = randint(1, 15)
                z=state.validate_action(self,MajoritiesAction,jogada)

        state.update(self,state,jogada,playerV)
        if(int(state.check_winner(self) != 0)):
            state.board()
        return int(state.check_winner(self))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
