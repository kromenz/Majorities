import math
import random
from games.majorities.player import MajoritiesPlayer
from games.majorities.result import MajoritiesResult
from games.majorities.state import MajoritiesState
from games.state import State


class MonteCarloMajoritiesPlayer(MajoritiesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def montecarlo(self, state: MajoritiesState):
        win = 0
        lost = 0
        d1 = []
        d2 = []
        d3 = []

        for play in range(10):
            playerV=True
            end=0
            state_clone,d1,d2,d3 = state.clone(self,d1,d2,d3)
            play = random.choice(state.get_possible_actions_cloned(self,state_clone))
            state.update_cloned(self, state, play, playerV, d1,d2,d3, state_clone)
            while end==0:
                playerV=False
                play = random.choice(state.get_possible_actions_cloned(self,state_clone))
                state.update_cloned(self, state, play, playerV, d1,d2,d3, state_clone)
                play = random.choice(state.get_possible_actions_cloned(self,state_clone))
                state.update_cloned(self, state, play, playerV, d1,d2,d3, state_clone)

                playerV=True
                if(state.check_winner_cloned(self,d1,d2,d3,state_clone)!=0):
                    state.board_cloned(self,state_clone,d1,d2,d3)
                    break

                play = random.choice(state.get_possible_actions_cloned(self,state_clone))
                state.update_cloned(self, state, play, playerV, d1,d2,d3, state_clone)
                play = random.choice(state.get_possible_actions_cloned(self,state_clone))
                state.update_cloned(self, state, play, playerV, d1,d2,d3, state_clone)

                
                if(state.check_winner_cloned(self,d1,d2,d3,state_clone)!=0):
                    state.board_cloned(self,state_clone,d1,d2,d3)
                    break
            
            if(state.check_winner_cloned(self,d1,d2,d3,state_clone)==1):
                    win += 1
            if(state.check_winner_cloned(self,d1,d2,d3,state_clone)==2):
                    lost += 1
            
        print('Resultados das simulacoes')
        print(win)
        print(lost)
        return (win * 100)/(win + lost)

            

    def get_action(self, state: MajoritiesState, playerV):
        selected_action = None
        max_score = -1

        actions = state.get_possible_actions()

        for action in actions:
            new_state = state.sim_play(action)
            score = self.montecarlo(new_state)
            if(score > max_score):
                max_score = score
                selected_action = action
        
        return selected_action


    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
