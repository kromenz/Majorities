import math

from games.majorities.player import MajoritiesPlayer
from games.majorities.result import MajoritiesResult
from games.majorities.state import MajoritiesState
from games.state import State

class HumanoMajoritiesPlayer(MajoritiesPlayer):

    def __init__(self, name):
        super().__init__(name)

        