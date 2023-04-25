class MajoritiesAction:

    """
    a connect 4 action is simple - it only takes the value of the column to play
    """

    __pos: int

    def __init__(self, pos: int):
        self.__pos = pos

    def get_pos(self):
        return self.__pos
