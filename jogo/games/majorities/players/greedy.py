import math

from games.majorities.player import MajoritiesPlayer
from games.majorities.result import MajoritiesResult
from games.majorities.state import MajoritiesState
from games.state import State

class GreedyMajoritiesPlayer(MajoritiesPlayer):
  
    def __init__(self, name):
        super().__init__(name)
        
    def get_action(self, state: MajoritiesState, playerV):
        available_actions = state.available_actions()
        max_score = float('-inf')
        best_action = None
        
        for action in available_actions:
            score = state.check_winner(action, self)
            if score > max_score:
                max_score = score
                best_action = action
                
        state.update(self, state, best_action, playerV)
        state.clear()
        
        return int(state.check_winner(self))
