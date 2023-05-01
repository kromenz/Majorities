import math
import random
from games.majorities.player import MajoritiesPlayer
from games.majorities.result import MajoritiesResult
from games.majorities.state import MajoritiesState
from games.state import State


class MonteCarloMajoritiesPlayer(MajoritiesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def montecarlo(state: MajoritiesState,new_state,Direcao1,Direcao2,Direcao3,playerV):
        win = 0
        lost = 0
        d1 = []
        d2 = []
        d3 = []

        
    
        for play in range(500):
            playerV=True
            end=0
            state_clone,d1,d2,d3 = state.clone(new_state,Direcao1,Direcao2,Direcao3)
            while end==0:
                playerV=False
                play = random.choice(state.get_possible_actions_cloned(state_clone))
                state.update_cloned( state, play, playerV, d1,d2,d3, state_clone)
                play = random.choice(state.get_possible_actions_cloned(state_clone))
                state.update_cloned( state, play, playerV, d1,d2,d3, state_clone)

                playerV=True
                if(state.check_winner_cloned(d1,d2,d3,state_clone)!=0):
                    break

                play = random.choice(state.get_possible_actions_cloned(state_clone))
                state.update_cloned( state, play, playerV, d1,d2,d3, state_clone)
                play = random.choice(state.get_possible_actions_cloned(state_clone))
                state.update_cloned( state, play, playerV, d1,d2,d3, state_clone)

                if(state.check_winner_cloned(d1,d2,d3,state_clone)!=0):
                    break
            
            if(state.check_winner_cloned(d1,d2,d3,state_clone)==2):
                    win += 1
            if(state.check_winner_cloned(d1,d2,d3,state_clone)==1):
                    lost += 1
            
        
        return (win * 100)/(win + lost)

            

    def get_action(self,state: MajoritiesState, playerV):
        max_score = -1
        best_action = []

        actions = state.get_possible_actions(self)
        if len(actions) == 2:
            dimensao=3
            state.update(state, actions[0], playerV,dimensao)
            state.update(state, actions[1],playerV,dimensao)

            state.board()
        
            return int(state.check_winner())

        for action in actions:
            for action2 in actions:
                if action != action2:
                    new_state,d1,d2,d3 = state.sim_play(action,action2,playerV,state)
                    playerValor=playerV
                    score = MonteCarloMajoritiesPlayer.montecarlo(state,new_state,d1,d2,d3,playerValor)
                    print(f'Pecas {action} e {action2} = {score}')
                    if score > max_score:
                        max_score = score
                        best_action.clear()
                        best_action.append([action,action2])
                    if score == max_score:
                        best_action.append([action,action2])
        
        dimensao=3
        jogada = random.choice(best_action)
        state.update(state, jogada[0], playerV,dimensao)
        state.update(state, jogada[1],playerV,dimensao)
        
        if(int(state.check_winner() != 0)):
            state.board(self,dimensao)
        
        return int(state.check_winner())


    def event_action( pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game( final_state: State):
        # ignore
        pass
