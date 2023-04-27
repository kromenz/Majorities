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
        available_actions = state.available_actions(self)
        print(available_actions)
        max_score = 0
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
        
        
        jogada=random.choice(best_action)
        state.update(self, state, jogada[0], playerV)
        state.update(self,state, jogada[1],playerV)

        state.clear()
        if(int(state.check_winner(self) != 0)):
            state.board()
        
        return int(state.check_winner(self))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass