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

l1=[' ',' ',10,19,27,34,41,'  ','  ']
l2=[' ',6,15,23,32,'  ',46,'  ']
l3=[' ',4,11,20,28,35,42,50,'  ']
l4=[2,7,16,24,'  ',39,47,53]
l5=[1,' ',12,'  ',29,36,43,51,55]
l6=[3,8,17,25,'  ',40,48,54]
l7=[' ',5,13,21,30,37,44,52,'  ']
l8=[' ',9,18,26,33,'  ',49,'  ']
l9=[' ',' ',14,22,31,38,45,'  ','  ']

l1ind=[' ',' ',10,19,27,34,41,'  ','  ']
l2ind=[' ',6,15,23,32,'  ',46,'  ']
l3ind=[' ',4,11,20,28,35,42,50,'  ']
l4ind=[2,7,16,24,'  ',39,47,53]
l5ind=[1,' ',12,'  ',29,36,43,51,55]
l6ind=[3,8,17,25,'  ',40,48,54]
l7ind=[' ',5,13,21,30,37,44,52,'  ']
l8ind=[' ',9,18,26,33,'  ',49,'  ']
l9ind=[' ',' ',14,22,31,38,45,'  ','  ']

LinhasDirecao15= [[1,3,5,9,14],
                  [2,8,13,18,22],
                  [4,7,12,17,21,26,31], 
                  [6,11,16,25,30,33,38],
                  [10,15,20,24,29,37,45],
                  [19,23,28,36,40,44,49],
                  [27,32,35,39,43,48,52],
                  [34,42,47,51,54],
                  [41,46,50,53,55]]
PontDirecao15=[0,0]
VencedorDirecao15=[' ',' ',' ',' ',' ',' ',' ']
Direcao15=[LinhasDirecao15,PontDirecao15,VencedorDirecao15]

LinhasDirecao25=[[1,2,4,6,10],
                 [3,7,11,15,19],
                 [5,8,12,16,20,23,27],
                 [9,13,17,24,28,32,34],
                 [14,18,21,25,29,35,41],
                 [22,26,30,36,39,42,46],
                 [31,33,37,40,43,47,50],
                 [38,44,48,51,53],
                 [45,49,52,54,55]
                 ]
PontDirecao25=[0,0]
VencedorDirecao25=[' ',' ',' ',' ',' ',' ',' ']
Direcao25=[LinhasDirecao25,PontDirecao25,VencedorDirecao25]

LinhasDirecao35=[[10,19,27,34,41],
                 [6,15,23,32,46],
                 [4,11,20,28,35,42,50],
                 [2,7,16,24,39,47,53],
                 [1,12,29,36,43,51,55],
                 [3,8,17,25,40,48,54],
                 [5,13,21,30,37,44,52],
                 [9,18,26,33,49],
                 [14,22,31,38,45]
                 ]
PontDirecao35=[0,0]
VencedorDirecao35=[' ',' ',' ',' ',' ',' ',' ']
Direcao35=[LinhasDirecao35,PontDirecao35,VencedorDirecao35]


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


    def check_winner():

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
            if(i == f'A' or i == f'B'):
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
    
    def validate_action(self, action: MajoritiesAction, x,dimensao) -> bool:
        if(dimensao==3):
            if(x< 1 or x > 15):
                return True
            if(tabuleiro[x-1] == f'A' or tabuleiro[x-1] == f'B'):
                return True
            
            return False
        
        if(dimensao==5):
            if(x< 1 or x > 55):
                return True
            for i in l1:
                if i==x:
                    return False
                    

            for i in l2:
                if i==x:
                    return False

            for i in l3:
                if i==x:
                    return False
                    

            for i in l4:
                if i == x:
                    return False
                
            for i in l5:
                if i == x:
                    return False
                    

            for i in l6:
                if i == x:
                    return False
                
            for i in l7:
                if i == x:
                    return False
                    

            for i in l8:
                if i == x:
                    return False
            
            for i in l9:
                if i==x:
                    return False
                       
            return True

    def ContaPecas5():
        pass

    def ContaDirecao5():
        pass

    def ContaPecas(tuplo):
        nA=0
        nB=0
        i=0
        while(i < 3):
            if tabuleiro[tuplo[i]-1] == f'B':
                    nB += 1
            elif tabuleiro[tuplo[i]-1] == f'A':
                    nA += 1
            i +=  1

        if nA > nB and nA> 1:
            return 'A'
        if nA < nB and nB>1:
            return 'B'
        
        return 'X'
    
    def ContaDirecao(direcao, state):
        i=0
        dA=0
        dB=0


        while i<5:
            V = state.ContaPecas(direcao[0][i])
            if(V=='A'):
                dA += 1
                direcao[2][i] = f'A'
            elif(V=='B'):
                dB += 1
                direcao[2][i] = f'B'
            else:
                direcao[2][i] = ' '
            i += 1

        direcao[1][0]=dB
        direcao[1][1]=dA
    
    def put_piece5(state, x, playerV, dimensao,linha):
        for i in range(len(linha)):
                if linha[i] != ' ' and  linha[i] != '  ':
                    if linha[i]==x:
                        if(playerV==True):
                            linha[i] = f'B'
                        else:
                            linha[i] = f'A'

    def put_piece(state, x, playerV, dimensao):

        if(dimensao==3):
            if(playerV==True):
                tabuleiro[x-1] = f'B'
            else:
                tabuleiro[x-1] = f'A'
                
        if(dimensao==5):
            state.put_piece5(state, x, playerV, dimensao,l1)
            state.put_piece5(state, x, playerV, dimensao,l2)
            state.put_piece5(state, x, playerV, dimensao,l3)
            state.put_piece5(state, x, playerV, dimensao,l4)
            state.put_piece5(state, x, playerV, dimensao,l5)
            state.put_piece5(state, x, playerV, dimensao,l6)
            state.put_piece5(state, x, playerV, dimensao,l7)
            state.put_piece5(state, x, playerV, dimensao,l8)
            state.put_piece5(state, x, playerV, dimensao,l9)
            
    def update(state, x, playerV,dimensao):

        state.put_piece(state, x, playerV, dimensao)
        state.ContaDirecao(Direcao1,state)
        state.ContaDirecao(Direcao2,state)
        state.ContaDirecao(Direcao3,state)

    def print_cell(cell, tabuleiro):
        players = {
            'A': '\033[96mA\033[0m',
            'B': '\033[91mB\033[0m',
        }

        for p,v in players.items():
            if tabuleiro[cell] == p:
                return v if cell < 9 else v + ' '  
            
        return tabuleiro[cell]
            
    def board(self, dimensao):
        if(dimensao==3):
            print(f"                  _____                   |", end="     \n")
            print(f"                 /     \\                  |", end="     \n")
            print(f"           _____/   {MajoritiesState.print_cell(0,tabuleiro)}   \\_____            |", end="     \n")
            print(f"          /     \       /     \\           |", end="     \n")
            print(f"    _____/   {MajoritiesState.print_cell(1,tabuleiro)}   \_____/   {MajoritiesState.print_cell(2,tabuleiro)}   \\_____     |", end="     \n")
            print(f"   /     \       /     \       /     \\    |", end="     \n")
            print(f"  /   {MajoritiesState.print_cell(3,tabuleiro)}   \_____/       \_____/   {MajoritiesState.print_cell(4,tabuleiro)}   \\   |", end="     \n")
            print(f"  \       /     \       /     \       /   |", end="     \n")
            print(f"   \_____/   {MajoritiesState.print_cell(5,tabuleiro)}   \     /   {MajoritiesState.print_cell(6,tabuleiro)}   \_____/    |", end="     \n")
            print(f"   /     \       /     \       /     \\    |", end=f"            {Direcao1[1][0]} - {Direcao1[1][1]}           |           {Direcao2[1][0]} - {Direcao2[1][1]}           |           {Direcao3[1][0]} - {Direcao3[1][1]}     \n")
            print(f"  /   {MajoritiesState.print_cell(7,tabuleiro)}   \_____/       \_____/   {MajoritiesState.print_cell(8,tabuleiro)}   \\   |", end=f"             ___            |            ___            |            ___                 \n")
            print(f"  \       /                   \       /   |", end=f"         ___/ {MajoritiesState.print_cell(0, Direcao1[2])} \___        |        ___/ {MajoritiesState.print_cell(0, Direcao2[2])} \___        |        ___/ {MajoritiesState.print_cell(2, Direcao3[2])} \___             \n")
            print(f"   \_____/        _____        \_____/    |", end=f"     ___/ {MajoritiesState.print_cell(1, Direcao1[2])} \___/ {MajoritiesState.print_cell(0, Direcao1[2])} \___    |    ___/ {MajoritiesState.print_cell(0, Direcao2[2])} \___/ {MajoritiesState.print_cell(1, Direcao2[2])} \___    |    ___/ {MajoritiesState.print_cell(1, Direcao3[2])} \___/ {MajoritiesState.print_cell(3, Direcao3[2])} \___         \n")
            print(f"   /     \       /     \       /     \\    |", end=f"    / {MajoritiesState.print_cell(2, Direcao1[2])} \___/ {MajoritiesState.print_cell(1, Direcao1[2])} \___/ {MajoritiesState.print_cell(0, Direcao1[2])} \   |   / {MajoritiesState.print_cell(0, Direcao2[2])} \___/ {MajoritiesState.print_cell(1, Direcao2[2])} \___/ {MajoritiesState.print_cell(2, Direcao2[2])} \   |   / {MajoritiesState.print_cell(0, Direcao3[2])} \___/ {MajoritiesState.print_cell(2, Direcao3[2])} \___/ {MajoritiesState.print_cell(4, Direcao3[2])} \        \n")
            print(f"  /  {MajoritiesState.print_cell(9,tabuleiro)}   \_____/  {MajoritiesState.print_cell(10,tabuleiro)}   \_____/  {MajoritiesState.print_cell(11,tabuleiro)}   \\   |", end=f"    \___/ {MajoritiesState.print_cell(2, Direcao1[2])} \___/ {MajoritiesState.print_cell(1, Direcao1[2])} \___/   |   \___/ {MajoritiesState.print_cell(1, Direcao2[2])} \___/ {MajoritiesState.print_cell(2, Direcao2[2])} \___/   |   \___/ {MajoritiesState.print_cell(1, Direcao3[2])} \___/ {MajoritiesState.print_cell(3, Direcao3[2])} \___/        \n")
            print(f"  \       /     \       /     \       /   |", end=f"    / {MajoritiesState.print_cell(3, Direcao1[2])} \___/ {MajoritiesState.print_cell(2, Direcao1[2])} \___/ {MajoritiesState.print_cell(1, Direcao1[2])} \   |   / {MajoritiesState.print_cell(1, Direcao2[2])} \___/ {MajoritiesState.print_cell(2, Direcao2[2])} \___/ {MajoritiesState.print_cell(3, Direcao2[2])} \   |   / {MajoritiesState.print_cell(0, Direcao3[2])} \___/ {MajoritiesState.print_cell(2, Direcao3[2])} \___/ {MajoritiesState.print_cell(4, Direcao3[2])} \        \n")
            print(f"   \_____/  {MajoritiesState.print_cell(12,tabuleiro)}   \_____/  {MajoritiesState.print_cell(13,tabuleiro)}   \_____/    |", end=f"    \___/ {MajoritiesState.print_cell(3, Direcao1[2])} \___/ {MajoritiesState.print_cell(2, Direcao1[2])} \___/   |   \___/ {MajoritiesState.print_cell(2, Direcao2[2])} \___/ {MajoritiesState.print_cell(3, Direcao2[2])} \___/   |   \___/ {MajoritiesState.print_cell(1, Direcao3[2])} \___/ {MajoritiesState.print_cell(3, Direcao3[2])} \___/        \n")
            print(f"         \       /     \       /          |", end=f"    / {MajoritiesState.print_cell(4, Direcao1[2])} \___/ {MajoritiesState.print_cell(3, Direcao1[2])} \___/ {MajoritiesState.print_cell(2, Direcao1[2])} \   |   / {MajoritiesState.print_cell(2, Direcao2[2])} \___/ {MajoritiesState.print_cell(3, Direcao2[2])} \___/ {MajoritiesState.print_cell(4, Direcao2[2])} \   |   / {MajoritiesState.print_cell(0, Direcao3[2])} \___/ {MajoritiesState.print_cell(2, Direcao3[2])} \___/ {MajoritiesState.print_cell(4, Direcao3[2])} \        \n")
            print(f"          \_____/  {MajoritiesState.print_cell(14,tabuleiro)}   \_____/           |", end=f"    \___/ {MajoritiesState.print_cell(4, Direcao1[2])} \___/ {MajoritiesState.print_cell(3, Direcao1[2])} \___/   |   \___/ {MajoritiesState.print_cell(3, Direcao2[2])} \___/ {MajoritiesState.print_cell(4, Direcao2[2])} \___/   |   \___/ {MajoritiesState.print_cell(1, Direcao3[2])} \___/ {MajoritiesState.print_cell(3, Direcao3[2])} \___/        \n")
            print(f"                \       /                 |", end=f"        \___/ {MajoritiesState.print_cell(4, Direcao1[2])} \___/       |       \___/ {MajoritiesState.print_cell(4, Direcao2[2])} \___/       |       \___/ {MajoritiesState.print_cell(2, Direcao3[2])} \___/            \n")
            print(f"                 \_____/                  |", end=f"            \___/           |           \___/           |           \___/                \n")

        if(dimensao==5):
            for i in range(9):
                if(i>=2):
                    print(f'{MajoritiesState.print_cell(i,l1)}      {MajoritiesState.print_cell(i,l3)}      {MajoritiesState.print_cell(i,l5)}      {MajoritiesState.print_cell(i,l7)}      {MajoritiesState.print_cell(i,l9)}')
                    if(i<8):
                        print(f'    {MajoritiesState.print_cell(i,l2)}      {MajoritiesState.print_cell(i,l4)}      {MajoritiesState.print_cell(i,l6)}      {MajoritiesState.print_cell(i,l8)}')
                else:
                    print(f'{MajoritiesState.print_cell(i,l1)}       {MajoritiesState.print_cell(i,l3)}       {MajoritiesState.print_cell(i,l5)}       {MajoritiesState.print_cell(i,l7)}       {MajoritiesState.print_cell(i,l9)}')
                    print(f'    {MajoritiesState.print_cell(i,l2)}       {MajoritiesState.print_cell(i,l4)}       {MajoritiesState.print_cell(i,l6)}       {MajoritiesState.print_cell(i,l8)}')
                
            
            print(f'{PontDirecao15[0]} - {PontDirecao15[1]}')
            print(f'{PontDirecao25[0]} - {PontDirecao25[1]}')
            print(f'{PontDirecao35[0]} - {PontDirecao35[1]}')



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

    def get_possible_actions(self):
        actions = []
        for i in tabuleiro:
            if i not in ['B','A']:
                actions.append(i) # Adiciona a posição não ocupada ao array
        return actions
    
    def bestplay(self,state, action, action2,playerV):
        if(playerV==True):
            tabuleiro[action-1] = f'B'
        else:
            tabuleiro[action-1] = f'A'

        if(playerV==True):
            tabuleiro[action2-1] = f'B'
        else:
            tabuleiro[action2-1] = f'A'

        state.ContaDirecao(Direcao1,state)
        state.ContaDirecao(Direcao2,state)
        state.ContaDirecao(Direcao3,state)

        score=0
        if(playerV==True):
            score=(PontDirecao1[0]-PontDirecao1[1])+(PontDirecao2[0]-PontDirecao2[1])+(PontDirecao3[0]-PontDirecao3[1])
        else:
            score=(PontDirecao1[1]-PontDirecao1[0])+(PontDirecao2[1]-PontDirecao2[0])+(PontDirecao3[1]-PontDirecao3[0])
        
        tabuleiro[action-1]=action
        tabuleiro[action2-1]=action2

        state.ContaDirecao(Direcao1,state)
        state.ContaDirecao(Direcao2,state)
        state.ContaDirecao(Direcao3,state)

        return score
    
    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(tabuleiro,Direcao1,Direcao2,Direcao3):
        cloned_state = tabuleiro.copy()
       
        d1=Direcao1.copy()
        d2=Direcao2.copy()
        d3=Direcao3.copy()
        
        return cloned_state,d1,d2,d3
    
    def board_cloned(tabuleiro,Direcao1,Direcao2,Direcao3):
            print(f"                  _____                   |", end="     \n")
            print(f"                 /     \\                  |", end="     \n")
            print(f"           _____/   {MajoritiesState.print_cell(0,tabuleiro)}   \\_____            |", end="     \n")
            print(f"          /     \       /     \\           |", end="     \n")
            print(f"    _____/   {MajoritiesState.print_cell(1,tabuleiro)}   \_____/   {MajoritiesState.print_cell(2,tabuleiro)}   \\_____     |", end="     \n")
            print(f"   /     \       /     \       /     \\    |", end="     \n")
            print(f"  /   {MajoritiesState.print_cell(3,tabuleiro)}   \_____/       \_____/   {MajoritiesState.print_cell(4,tabuleiro)}   \\   |", end="     \n")
            print(f"  \       /     \       /     \       /   |", end="     \n")
            print(f"   \_____/   {MajoritiesState.print_cell(5,tabuleiro)}   \     /   {MajoritiesState.print_cell(6,tabuleiro)}   \_____/    |", end="     \n")
            print(f"   /     \       /     \       /     \\    |", end=f"            {Direcao1[1][0]} - {Direcao1[1][1]}           |           {Direcao2[1][0]} - {Direcao2[1][1]}           |           {Direcao3[1][0]} - {Direcao3[1][1]}     \n")
            print(f"  /   {MajoritiesState.print_cell(7,tabuleiro)}   \_____/       \_____/   {MajoritiesState.print_cell(8,tabuleiro)}   \\   |", end=f"             ___            |            ___            |            ___                 \n")
            print(f"  \       /                   \       /   |", end=f"         ___/ {MajoritiesState.print_cell(0, Direcao1[2])} \___        |        ___/ {MajoritiesState.print_cell(0, Direcao2[2])} \___        |        ___/ {MajoritiesState.print_cell(2, Direcao3[2])} \___             \n")
            print(f"   \_____/        _____        \_____/    |", end=f"     ___/ {MajoritiesState.print_cell(1, Direcao1[2])} \___/ {MajoritiesState.print_cell(0, Direcao1[2])} \___    |    ___/ {MajoritiesState.print_cell(0, Direcao2[2])} \___/ {MajoritiesState.print_cell(1, Direcao2[2])} \___    |    ___/ {MajoritiesState.print_cell(1, Direcao3[2])} \___/ {MajoritiesState.print_cell(3, Direcao3[2])} \___         \n")
            print(f"   /     \       /     \       /     \\    |", end=f"    / {MajoritiesState.print_cell(2, Direcao1[2])} \___/ {MajoritiesState.print_cell(1, Direcao1[2])} \___/ {MajoritiesState.print_cell(0, Direcao1[2])} \   |   / {MajoritiesState.print_cell(0, Direcao2[2])} \___/ {MajoritiesState.print_cell(1, Direcao2[2])} \___/ {MajoritiesState.print_cell(2, Direcao2[2])} \   |   / {MajoritiesState.print_cell(0, Direcao3[2])} \___/ {MajoritiesState.print_cell(2, Direcao3[2])} \___/ {MajoritiesState.print_cell(4, Direcao3[2])} \        \n")
            print(f"  /  {MajoritiesState.print_cell(9,tabuleiro)}   \_____/  {MajoritiesState.print_cell(10,tabuleiro)}   \_____/  {MajoritiesState.print_cell(11,tabuleiro)}   \\   |", end=f"    \___/ {MajoritiesState.print_cell(2, Direcao1[2])} \___/ {MajoritiesState.print_cell(1, Direcao1[2])} \___/   |   \___/ {MajoritiesState.print_cell(1, Direcao2[2])} \___/ {MajoritiesState.print_cell(2, Direcao2[2])} \___/   |   \___/ {MajoritiesState.print_cell(1, Direcao3[2])} \___/ {MajoritiesState.print_cell(3, Direcao3[2])} \___/        \n")
            print(f"  \       /     \       /     \       /   |", end=f"    / {MajoritiesState.print_cell(3, Direcao1[2])} \___/ {MajoritiesState.print_cell(2, Direcao1[2])} \___/ {MajoritiesState.print_cell(1, Direcao1[2])} \   |   / {MajoritiesState.print_cell(1, Direcao2[2])} \___/ {MajoritiesState.print_cell(2, Direcao2[2])} \___/ {MajoritiesState.print_cell(3, Direcao2[2])} \   |   / {MajoritiesState.print_cell(0, Direcao3[2])} \___/ {MajoritiesState.print_cell(2, Direcao3[2])} \___/ {MajoritiesState.print_cell(4, Direcao3[2])} \        \n")
            print(f"   \_____/  {MajoritiesState.print_cell(12,tabuleiro)}   \_____/  {MajoritiesState.print_cell(13,tabuleiro)}   \_____/    |", end=f"    \___/ {MajoritiesState.print_cell(3, Direcao1[2])} \___/ {MajoritiesState.print_cell(2, Direcao1[2])} \___/   |   \___/ {MajoritiesState.print_cell(2, Direcao2[2])} \___/ {MajoritiesState.print_cell(3, Direcao2[2])} \___/   |   \___/ {MajoritiesState.print_cell(1, Direcao3[2])} \___/ {MajoritiesState.print_cell(3, Direcao3[2])} \___/        \n")
            print(f"         \       /     \       /          |", end=f"    / {MajoritiesState.print_cell(4, Direcao1[2])} \___/ {MajoritiesState.print_cell(3, Direcao1[2])} \___/ {MajoritiesState.print_cell(2, Direcao1[2])} \   |   / {MajoritiesState.print_cell(2, Direcao2[2])} \___/ {MajoritiesState.print_cell(3, Direcao2[2])} \___/ {MajoritiesState.print_cell(4, Direcao2[2])} \   |   / {MajoritiesState.print_cell(0, Direcao3[2])} \___/ {MajoritiesState.print_cell(2, Direcao3[2])} \___/ {MajoritiesState.print_cell(4, Direcao3[2])} \        \n")
            print(f"          \_____/  {MajoritiesState.print_cell(14,tabuleiro)}   \_____/           |", end=f"    \___/ {MajoritiesState.print_cell(4, Direcao1[2])} \___/ {MajoritiesState.print_cell(3, Direcao1[2])} \___/   |   \___/ {MajoritiesState.print_cell(3, Direcao2[2])} \___/ {MajoritiesState.print_cell(4, Direcao2[2])} \___/   |   \___/ {MajoritiesState.print_cell(1, Direcao3[2])} \___/ {MajoritiesState.print_cell(3, Direcao3[2])} \___/        \n")
            print(f"                \       /                 |", end=f"        \___/ {MajoritiesState.print_cell(4, Direcao1[2])} \___/       |       \___/ {MajoritiesState.print_cell(4, Direcao2[2])} \___/       |       \___/ {MajoritiesState.print_cell(2, Direcao3[2])} \___/            \n")
            print(f"                 \_____/                  |", end=f"            \___/           |           \___/           |           \___/                \n")

    
    def check_winner_cloned(d1,d2,d3,cloned_state):

        Vencedorp1 = 0
        Vencedorp2 = 0

        if(d1[1][0] == 3):
            Vencedorp1 += 1
        if(d1[1][1] == 3):
            Vencedorp2 += 1

        if(d2[1][0] == 3):
            Vencedorp1 += 1
        if(d2[1][1] == 3):
            Vencedorp2 += 1

        if(d3[1][0] == 3):
            Vencedorp1 += 1
        if(d3[1][1] == 3):
            Vencedorp2 += 1

        if Vencedorp1 >= 2:
            return 1
        if Vencedorp2 >= 3:
            return 2
        
        pecastabuleiro = 0
        for i in cloned_state:
            if(i == f'A' or i == f'B'):
                pecastabuleiro += 1

        if pecastabuleiro == 15:
            Vencedorp1 = 0
            Vencedorp2 = 0
            if(d1[1][0] > d1[1][1]):
                Vencedorp1 += 1
            else:
                Vencedorp2 += 1

            if(d2[1][0] > d2[1][1]):
                Vencedorp1 += 1
            else:
                Vencedorp2 += 1

            if(d3[1][0] > d3[1][1]):
                Vencedorp1 += 1
            else:
                Vencedorp2 += 1

            if(Vencedorp1 > Vencedorp2):
                return 1
            else:
                return 2

        return 0
    
    def get_possible_actions_cloned(cloned_state):
        
        actions = []

        for i in cloned_state:
            if i not in ['B','A']:
                actions.append(i) # Adiciona a posição não ocupada ao array
        return actions

    def put_piece_cloned(x, playerV,cloned_state):
        if(playerV==True):
            cloned_state[x-1] = f'B'
        else:
            cloned_state[x-1] = f'A'



    def ContaPecas_cloned(tuplo,cloned_state):
        nA=0
        nB=0
        i=0
        while(i < 3):
            if cloned_state[tuplo[i]-1] == f'B':
                    nB += 1
            elif cloned_state[tuplo[i]-1] == f'A':
                    nA += 1
            i +=  1

        if nA > nB and nA> 1:
            return 'A'
        if nA < nB and nB>1:
            return 'B'
        
        return 'X'
    
    def ContaDirecao_cloned(direcao, state, cloned_state):
        i=0
        dA=0
        dB=0


        while i<5:
            V = state.ContaPecas_cloned(direcao[0][i],cloned_state)
            if(V=='A'):
                dA += 1
                direcao[2][i] = f'A'
            elif(V=='B'):
                dB += 1
                direcao[2][i] = f'B'
            else:
                direcao[2][i] = ' '
            i += 1

        direcao[1][0]=dB
        direcao[1][1]=dA

    def update_cloned(state, x, playerV, d1,d2,d3, cloned_state):


        state.put_piece_cloned(x, playerV,cloned_state)
        state.ContaDirecao_cloned(d1,state,cloned_state)
        state.ContaDirecao_cloned(d2,state,cloned_state)
        state.ContaDirecao_cloned(d3,state,cloned_state)

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


    def sim_play(action,action2,playerV,state):
        new_state = tabuleiro.copy()
        d1=Direcao1.copy()
        d2=Direcao2.copy()
        d3=Direcao3.copy()
        state.update_cloned(state, action, playerV, d1,d2,d3, new_state)
        state.update_cloned(state, action2, playerV, d1,d2,d3, new_state)
        return new_state,d1,d2,d3
