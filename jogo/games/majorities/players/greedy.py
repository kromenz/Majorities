import math
import random
from games.majorities.player import MajoritiesPlayer
from games.majorities.result import MajoritiesResult
from games.majorities.state import MajoritiesState
from games.state import State

class GreedyMajoritiesPlayer(MajoritiesPlayer):
  
    def __init__(self, name):
        super().__init__(name)
        
    def get_action(self, state: MajoritiesState, playerV):
        available_actions = state.get_possible_actions(self)
        max_score = -1
        best_action = []
        
        for action in available_actions:
            for action2 in available_actions:
                if action != action2:    
                    score = state.bestplay(self, state, action, action2, playerV)
                    if score > max_score:
                        max_score = score
                        best_action.clear()
                        best_action.append([action,action2])
                    if score == max_score:
                        best_action.append([action,action2])
        
        dimensao = 3
        jogada = random.choice(best_action)
        state.update(state, jogada[0], playerV,dimensao)
        state.update(state, jogada[1],playerV,dimensao)

        state.clear()
        if(int(state.check_winner() != 0)):
            state.board(self,dimensao)
        
        return int(state.check_winner())

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass