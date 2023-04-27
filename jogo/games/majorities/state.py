from typing import Optional

from games.majorities.action import MajoritiesAction
from games.majorities.result import MajoritiesResult
from games.state import State
import os

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

class bcolors:
    B = '\033[96m' #BLUE
    A = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class MajoritiesState(State):
    
    EMPTY_CELL = -1

    def __init__(self, num_rows: int = 6, num_cols: int = 7):
        super().__init__()

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


    def clear():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix (Linux, macOS)
            os.system('clear')


    def check_winner(self):

        Vencedorp1 = 0
        Vencedorp2 = 0

        if(PontDirecao1[0] == 3):
            Vencedorp1 += 1
        if(PontDirecao1[1] == 3):
            Vencedorp2 += 1

        if(PontDirecao2[0] == 3):
            Vencedorp1 += 1
        if(PontDirecao2[1] == 3):
            Vencedorp2 += 1

        if(PontDirecao3[0] == 3):
            Vencedorp1 += 1
        if(PontDirecao3[1] == 3):
            Vencedorp2 += 1

        if Vencedorp1 >= 2:
            return 1
        if Vencedorp2 >= 3:
            return 2
        
        pecastabuleiro = 0
        for i in tabuleiro:
            if(i == f'{bcolors.A}A{bcolors.RESET}' or i == f'{bcolors.B}B{bcolors.RESET}' or i == f'{bcolors.A}A{bcolors.RESET} ' or i == f'{bcolors.B}B{bcolors.RESET} '):
                pecastabuleiro += 1

        if pecastabuleiro == 15:
            Vencedorp1 = 0
            Vencedorp2 = 0
            if(PontDirecao1[0] > PontDirecao1[1]):
                Vencedorp1 += 1
            else:
                Vencedorp2 += 1

            if(PontDirecao2[0] > PontDirecao2[1]):
                Vencedorp1 += 1
            else:
                Vencedorp2 += 1

            if(PontDirecao3[0] > PontDirecao3[1]):
                Vencedorp1 += 1
            else:
                Vencedorp2 += 1

            if(Vencedorp1 > Vencedorp2):
                return 1
            else:
                return 2

        return 0

    def get_num_players(self):
        return 2
    
    def validate_action(self, action: MajoritiesAction, x) -> bool:
        if(x< 1 or x > 15):
            return True
        if(tabuleiro[x-1] == f'{bcolors.A}A{bcolors.RESET}' or tabuleiro[x-1] == f'{bcolors.B}B{bcolors.RESET}' or tabuleiro[x-1] == f'{bcolors.A}A{bcolors.RESET} ' or tabuleiro[x-1] == f'{bcolors.B}B{bcolors.RESET} '):
            return True

        return False

    def ContaPecas(self, tuplo):
        nA=0
        nB=0
        i=0
        while(i<3):
            if tabuleiro[tuplo[i]-1] == f'{bcolors.B}B{bcolors.RESET}' or tabuleiro[tuplo[i]-1] == f'{bcolors.B}B{bcolors.RESET} ':
                    nB += 1
            elif tabuleiro[tuplo[i]-1] == f'{bcolors.A}A{bcolors.RESET}' or tabuleiro[tuplo[i]-1] == f'{bcolors.A}A{bcolors.RESET} ':
                    nA += 1
            i +=  1

        if nA > nB and nA> 1:
            return 'A'
        if nA < nB and nB>1:
            return 'B'
        
        return 'X'
    
    def ContaDirecao(self, direcao, state):
        i=0
        dA=0
        dB=0

        while i<5:
            V = state.ContaPecas(self, direcao[0][i])
            if(V=='A'):
                dA += 1
                direcao[2][i] = f'{bcolors.A}A{bcolors.RESET}'
            elif(V=='B'):
                dB += 1
                direcao[2][i] = f'{bcolors.B}B{bcolors.RESET}'
            else:
                direcao[2][i] = ' '
            i += 1

        direcao[1][0]=dB
        direcao[1][1]=dA

    def update(self, state, x, playerV):
        if(playerV==True):
            if(int(tabuleiro[x-1])>=10):
                tabuleiro[x-1] = f'{bcolors.B}B{bcolors.RESET} '
            else:
                tabuleiro[x-1] = f'{bcolors.B}B{bcolors.RESET}'
        else:
            if(int(tabuleiro[x-1]) >= 10):
                tabuleiro[x-1] = f'{bcolors.A}A{bcolors.RESET} '
            else:
                tabuleiro[x-1] = f'{bcolors.A}A{bcolors.RESET}'
        
        state.ContaDirecao(self, Direcao1,state)
        state.ContaDirecao(self, Direcao2,state)
        state.ContaDirecao(self, Direcao3,state)

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


    def reset_board():
        tabuleiro[0:15]=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        PecasP= []
        PecasB= []

        LinhasDirecao1= [[1,3,5],[2,7,9],[4,6,12], [8,11,14],[10,13,15]]
        PontDirecao1[0:2]=[0,0]
        VencedorDirecao1[0:15]=[' ',' ',' ',' ',' ']
        Direcao1[0:3]=[LinhasDirecao1,PontDirecao1,VencedorDirecao1]

        LinhasDirecao2=[[1,2,4],[3,6,8],[5,7,10],[9,11,13],[12,14,15]]
        PontDirecao2[0:2]=[0,0]
        VencedorDirecao2[0:15]=[' ',' ',' ',' ',' ']
        Direcao2[0:3]=[LinhasDirecao2,PontDirecao2,VencedorDirecao2]

        LinhasDirecao3=[[4,8,10],[2,6,13],[1,11,15],[3,7,14],[5,9,12]]
        PontDirecao3[0:2]=[0,0]
        VencedorDirecao3[0:15]=[' ',' ',' ',' ',' ']
        Direcao3[0:3]=[LinhasDirecao3,PontDirecao3,VencedorDirecao3]

    def available_actions(self):
        actions = []
        for i in tabuleiro:
            if i not in [f'{bcolors.B}B{bcolors.RESET}', f'{bcolors.B}B{bcolors.RESET} ', f'{bcolors.A}A{bcolors.RESET}', f'{bcolors.A}A{bcolors.RESET} ']:
                actions.append(i) # Adiciona a posição não ocupada ao array
        return actions
    
    def bestplay(self,state, action, action2,playerV):
        if(playerV==True):
            if(int(tabuleiro[action-1])>=10):
                tabuleiro[action-1] = f'{bcolors.B}B{bcolors.RESET} '
            else:
                tabuleiro[action-1] = f'{bcolors.B}B{bcolors.RESET}'
        else:
            if(int(tabuleiro[action-1]) >= 10):
                tabuleiro[action-1] = f'{bcolors.A}A{bcolors.RESET} '
            else:
                tabuleiro[action-1] = f'{bcolors.A}A{bcolors.RESET}'
        
        if(playerV==True):
            if(int(tabuleiro[action2-1])>=10):
                tabuleiro[action2-1] = f'{bcolors.B}B{bcolors.RESET} '
            else:
                tabuleiro[action2-1] = f'{bcolors.B}B{bcolors.RESET}'
        else:
            if(int(tabuleiro[action2-1]) >= 10):
                tabuleiro[action2-1] = f'{bcolors.A}A{bcolors.RESET} '
            else:
                tabuleiro[action2-1] = f'{bcolors.A}A{bcolors.RESET}'

        state.ContaDirecao(self, Direcao1,state)
        state.ContaDirecao(self, Direcao2,state)
        state.ContaDirecao(self, Direcao3,state)

        score=0
        if(playerV==True):
            score=(PontDirecao1[0]-PontDirecao1[1])+(PontDirecao2[0]-PontDirecao2[1])+(PontDirecao3[0]-PontDirecao3[1])
        else:
            score=(PontDirecao1[1]-PontDirecao1[0])+(PontDirecao2[1]-PontDirecao2[0])+(PontDirecao3[1]-PontDirecao3[0])
        
        tabuleiro[action-1]=action
        tabuleiro[action2-1]=action2

        state.ContaDirecao(self, Direcao1,state)
        state.ContaDirecao(self, Direcao2,state)
        state.ContaDirecao(self, Direcao3,state)

        return score
    
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
