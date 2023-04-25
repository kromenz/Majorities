from typing import Optional

from games.majorities.action import MajoritiesAction
from games.majorities.result import MajoritiesResult
from games.state import State

tabuleiro=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
PecasP= []
PecasB= []

LinhasDirecao1= [[1,3,5],[2,7,9],[4,6,12], [8,11,14],[10,13,15]]
PontDirecao1=[0,0]
VencedorDirecao1=[' ',' ',' ',' ',' ']
Direcao1=[LinhasDirecao1,PontDirecao1,VencedorDirecao1]

LinhasDirecao2=[[1,2,4],[3,6,8],[5,7,10],[9,11,13],[12,14,15]]
PontDirecao2=[0,0]
VencedorDirecao2=[' ',' ',' ',' ',' ']
Direcao2=[LinhasDirecao2,PontDirecao2,VencedorDirecao2]

LinhasDirecao3=[[4,8,10],[2,6,13],[1,11,15],[3,7,14],[5,9,12]]
PontDirecao3=[0,0]
VencedorDirecao3=[' ',' ',' ',' ',' ']
Direcao3=[LinhasDirecao3,PontDirecao3,VencedorDirecao3]


class MajoritiesState(State):
    EMPTY_CELL = -1

    def __init__(self, num_rows: int = 6, num_cols: int = 7):
        super().__init__()

        if num_rows < 4:
            raise Exception("the number of rows must be 4 or over")
        if num_cols < 4:
            raise Exception("the number of cols must be 4 or over")

        """
        the dimensions of the board
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        """
        the grid
        """
        self.__grid = [[MajoritiesState.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        # check for 4 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player:
                    return True

        # check for 4 up and down
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: MajoritiesAction, x) -> bool:
        if(x<= 1 or x >= 15):
            return True
        if(tabuleiro[x-1] == 'A' or tabuleiro[x-1] == 'B'):
            return True

        return False

    def update(self, action: MajoritiesAction, x, playerV):
        if(playerV==True):
            if(int(tabuleiro[x-1])>=10):
                tabuleiro[x-1] = f'B '
            else:
                tabuleiro[x-1] = f'B'
        else:
            if(tabuleiro[x-1] >= 10):
                tabuleiro[x-1] = f'A '
            else:
                tabuleiro[x-1] = f'A'
        '''
        action.get_col()

        # drop the checker
        for row in range(self.__num_rows - 1, -1, -1):
            if self.__grid[row][col] < 0:
                self.__grid[row][col] = self.__acting_player
                break

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1
        '''

    def board():
        print(f"                  _____                   |", end="     \n")
        print(f"                 /     \\                  |", end="     \n")
        print(f"           _____/   {tabuleiro[0]}   \\_____            |", end="     \n")
        print(f"          /     \       /     \\           |", end="     \n")
        print(f"    _____/   {tabuleiro[1]}   \_____/   {tabuleiro[2]}   \\_____     |", end="     \n")
        print(f"   /     \       /     \       /     \\    |", end="     \n")
        print(f"  /   {tabuleiro[3]}   \_____/       \_____/   {tabuleiro[4]}   \\   |", end="     \n")
        print(f"  \       /     \       /     \       /   |", end="     \n")
        print(f"   \_____/   {tabuleiro[5]}   \     /   {tabuleiro[6]}   \_____/    |", end="     \n")
        print(f"   /     \       /     \       /     \\    |", end=f"            {Direcao1[1][0]} - {Direcao1[1][1]}           |           {Direcao2[1][0]} - {Direcao2[1][1]}           |           {Direcao3[1][0]} - {Direcao3[1][1]}     \n")
        print(f"  /   {tabuleiro[7]}   \_____/       \_____/   {tabuleiro[8]}   \\   |", end=f"             ___            |            ___            |            ___                 \n")
        print(f"  \       /                   \       /   |", end=f"         ___/ {Direcao1[2][0]} \___        |        ___/ {Direcao2[2][0]} \___        |        ___/ {Direcao3[2][2]} \___             \n")
        print(f"   \_____/        _____        \_____/    |", end=f"     ___/ {Direcao1[2][1]} \___/ {Direcao1[2][0]} \___    |    ___/ {Direcao2[2][0]} \___/ {Direcao2[2][1]} \___    |    ___/ {Direcao3[2][1]} \___/ {Direcao3[2][3]} \___         \n")
        print(f"   /     \       /     \       /     \\    |", end=f"    / {Direcao1[2][2]} \___/ {Direcao1[2][1]} \___/ {Direcao1[2][0]} \   |   / {Direcao2[2][0]} \___/ {Direcao2[2][1]} \___/ {Direcao2[2][2]} \   |   / {Direcao3[2][0]} \___/ {Direcao3[2][2]} \___/ {Direcao3[2][4]} \        \n")
        print(f"  /  {tabuleiro[9]}   \_____/  {tabuleiro[10]}   \_____/  {tabuleiro[11]}   \\   |", end=f"    \___/ {Direcao1[2][2]} \___/ {Direcao1[2][1]} \___/   |   \___/ {Direcao2[2][1]} \___/ {Direcao2[2][2]} \___/   |   \___/ {Direcao3[2][1]} \___/ {Direcao3[2][3]} \___/        \n")
        print(f"  \       /     \       /     \       /   |", end=f"    / {Direcao1[2][3]} \___/ {Direcao1[2][2]} \___/ {Direcao1[2][1]} \   |   / {Direcao2[2][1]} \___/ {Direcao2[2][2]} \___/ {Direcao2[2][3]} \   |   / {Direcao3[2][0]} \___/ {Direcao3[2][2]} \___/ {Direcao3[2][4]} \        \n")
        print(f"   \_____/  {tabuleiro[12]}   \_____/  {tabuleiro[13]}   \_____/    |", end=f"    \___/ {Direcao1[2][3]} \___/ {Direcao1[2][2]} \___/   |   \___/ {Direcao2[2][2]} \___/ {Direcao2[2][3]} \___/   |   \___/ {Direcao3[2][1]} \___/ {Direcao3[2][3]} \___/        \n")
        print(f"         \       /     \       /          |", end=f"    / {Direcao1[2][4]} \___/ {Direcao1[2][3]} \___/ {Direcao1[2][2]} \   |   / {Direcao2[2][2]} \___/ {Direcao2[2][3]} \___/ {Direcao2[2][4]} \   |   / {Direcao3[2][0]} \___/ {Direcao3[2][2]} \___/ {Direcao3[2][4]} \        \n")
        print(f"          \_____/  {tabuleiro[14]}   \_____/           |", end=f"    \___/ {Direcao1[2][4]} \___/ {Direcao1[2][3]} \___/   |   \___/ {Direcao2[2][3]} \___/ {Direcao2[2][4]} \___/   |   \___/ {Direcao3[2][1]} \___/ {Direcao3[2][3]} \___/        \n")
        print(f"                \       /                 |", end=f"        \___/ {Direcao1[2][4]} \___/       |       \___/ {Direcao2[2][4]} \___/       |       \___/ {Direcao3[2][2]} \___/            \n")
        print(f"                 \_____/                  |", end=f"            \___/           |           \___/           |           \___/                \n")


        
    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = MajoritiesState(self.__num_rows, self.__num_cols)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[MajoritiesResult]:
        if self.__has_winner:
            return MajoritiesResult.LOOSE if pos == self.__acting_player else MajoritiesResult.WIN
        if self.__is_full():
            return MajoritiesResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    def get_possible_actions(self):
        return list(filter(
            lambda action: self.validate_action(action),
            map(
                lambda pos: MajoritiesAction(pos),
                range(0, self.get_num_cols()))
        ))

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
