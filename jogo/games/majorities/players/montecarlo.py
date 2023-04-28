from random import choice

from games.majorities.action import MajoritiesAction
from games.majorities.player import MajoritiesPlayer
from games.majorities.state import MajoritiesState
from games.state import State
from games.majorities.result import MajoritiesResult


class MonteCarloMajoritiesPlayer(MajoritiesPlayer):

    def __init__(self, name):
        super().__init__(name)

    def montecarlo(self, state: MajoritiesState):
        win = 0
        lost = 0
        draw = 0

        for play in range(25):
            state_clone = state.clone()
            while not state_clone.is_finished:
                action = choice(state_clone.get_possible_actions())
                state_clone.play(action)
            if state_clone.get_result(self.get_current_pos()) == MajoritiesResult.WIN:
                win += 1
            if state_clone.get_result(self.get_current_pos()) == MajoritiesResult.LOOSE:
                lost += 1
            if state_clone.get_result(self.get_current_pos()) == MajoritiesResult.DRAW:
                draw += 1
        
        return (win + draw*0.25)/win + lost + draw

            

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
