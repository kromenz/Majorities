import time

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

tabuleiro5=[l1,l2,l3,l4,l5,l6,l7,l8,l9]

class bcolors:
    B = '\033[96m' #BLUE
    A = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


def sair():
    print("-----------------------------------------")
    print("|\tObrigado por jogar o Majorities |\n|\tVolte Sempre!\t\t\t|")
    print("-----------------------------------------")
    time.sleep(1)
    exit()
    
def menu():

    linhatab=True
    for i in range(9):
            if(i>=2):
                print(f'{l1[i]}      {l3[i]}      {l5[i]}      {l7[i]}      {l9[i]}')
                print(f'    {l2[i]}      {l4[i]}      {l6[i]}      {l8[i]}')
            else:
                print(f'{l1[i]}       {l3[i]}       {l5[i]}       {l7[i]}       {l9[i]}')
                print(f'    {l2[i]}       {l4[i]}       {l6[i]}       {l8[i]}')

    

    op = -1
    while op not in [0,1,2,3]:
        print("-----------------------------------------")
        print("|\tBem vindo ao Majorities!\t|")
        print("-----------------------------------------")
        print("|\t1. Jogar contra Humano \t\t|")
        print("\n")
        print("|\t2. Jogar contra Minimax \t|")
        print("\n")
        print("|\t3. Jogar Minimax contra Random \t|")
        print("\n")
        print("|\t0. Sair \t\t\t|")
        print("-----------------------------------------")
        op = int(input("\n\tOpção: ")) 
        if op not in [0,1,2,3]:
             print("\n\tInsira um valor entre 0 e 3...")

    return op

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

def ContraHumano(player):
        
        board()
 
        jogada = int(input("\nEscolha onde quer jogar:"))

        while(tabuleiro[jogada-1] == 'A' or tabuleiro[jogada-1] == 'B'):
            jogada = int(input("Local ocupado. Escolha outro lugar:"))

        if(player==True):
            if(tabuleiro[jogada-1]>=10):
                tabuleiro[jogada-1] = f'{bcolors.B}B{bcolors.RESET} '
            else:
                tabuleiro[jogada-1] = f'{bcolors.B}B{bcolors.RESET}'
        else:
            if(tabuleiro[jogada-1] >= 10):
                tabuleiro[jogada-1] = f'{bcolors.A}A{bcolors.RESET} '
            else:
                tabuleiro[jogada-1] = f'{bcolors.A}A{bcolors.RESET}'

def ContaPecas(tuplo):
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

def ContaDirecao(direcao):
    i=0
    dA=0
    dB=0

    while i<5:
        V=ContaPecas(direcao[0][i])
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
          
def main():
    op = menu()

    if(op == 1):
        end=0
        player = True
        p1 = input("\n\tIntroduza o nome do Player 1: ")
        p2 = input("\n\tIntroduza o nome do Player 2: ")
        while( end == 0):
            print("\n\t\t" + p1 + " vs " + p2)
            ContraHumano(player)
            if(player==True):
                player=False
            else:
                player=True
            ContaDirecao(Direcao1)
            ContaDirecao(Direcao2)
            ContaDirecao(Direcao3)
            ContraHumano(player)

    elif(op == 2):
        print("\n\t Humano vs Minimax")
            
    elif(op == 3):
        print("\n\t Minimax vs Rando") 
        
    elif(op == 0):
        sair()  
    
main()
    