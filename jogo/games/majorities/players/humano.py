import math

from games.majorities.player import MajoritiesPlayer
from games.majorities.result import MajoritiesResult
from games.majorities.state import MajoritiesState
from games.majorities.action import MajoritiesAction
from games.state import State

class HumanoMajoritiesPlayer(MajoritiesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: MajoritiesState, playerV,dimensao):
        z = False

        state.board(self, dimensao)
        jogada = int(input("\nEscolha onde quer jogar:"))
        z=state.validate_action(self,MajoritiesAction,jogada,dimensao)
        if z == True:
            while  z == True:
                jogada = int(input("\nLugar Ocupado/Nao Valido\n\nEscolha outro lugar:"))
                z=state.validate_action(self,MajoritiesAction,jogada,dimensao)
        
        state.update(state,jogada,playerV,dimensao)
        state.clear()
        if(int(state.check_winner() != 0)):
            state.board(self, dimensao)

        return int(state.check_winner())    
    
    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
