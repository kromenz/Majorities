import time

tabuleiro=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
PecasP= []
PecasB= []

LinhasDirecao1= [[1,3,5],[2,7,9],[4,6,12], [8,11,14],[10,13,15]]
PontDirecao1=[0,0]
Direcao1=[LinhasDirecao1,PontDirecao1]

LinhasDirecao2=[[1,2,4],[3,6,8],[5,7,10],[9,11,13],[12,14,15]]
PontDirecao2=[0,0]
Direcao2=[LinhasDirecao2,PontDirecao2]

LinhasDirecao3=[[4,8,10],[2,6,13],[1,11,15],[3,7,14],[5,9,12]]
PontDirecao3=[0,0]
Direcao3=[LinhasDirecao3,PontDirecao3]


def sair():
    print("-----------------------------------------")
    print("|\tObrigado por jogar o Majorities |\n|\tVolte Sempre!\t\t\t|")
    print("-----------------------------------------")
    time.sleep(1)
    exit()
    
def menu():

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

def board(player):
        print(f"                  _____                   |")
        print(f"                 /     \\                  |")
        print(f"           _____/   {tabuleiro[0]}   \\_____            |")
        print(f"          /     \       /     \\           |")
        print(f"    _____/   {tabuleiro[1]}   \_____/   {tabuleiro[2]}   \\_____     |")
        print(f"   /     \       / XXX \       /     \\    |")
        print(f"  /   {tabuleiro[3]}   \_____/ XXXXX \_____/   {tabuleiro[4]}   \\   |")
        print(f"  \       /     \ XXXXX /     \       /   |")
        print(f"   \_____/   {tabuleiro[5]}   \_____/   {tabuleiro[6]}   \_____/    |")
        print(f"   /     \       / XXX \       /     \\    |")
        print(f"  /   {tabuleiro[7]}   \_____/ XXXXX \_____/   {tabuleiro[8]}   \\   |")
        print(f"  \       / XXX \ XXXXX / XXX \       /   |")
        print(f"   \_____/ XXXXX \_____/ XXXXX \_____/    |")
        print(f"   /     \ XXXXX /     \ XXXXX /     \\    |")
        print(f"  /  {tabuleiro[9]}   \_____/  {tabuleiro[10]}   \_____/  {tabuleiro[11]}   \\   |")
        print(f"  \       /     \       /     \       /   |")
        print(f"   \_____/  {tabuleiro[12]}   \_____/  {tabuleiro[13]}   \_____/    |")
        print(f"         \       /     \       /          |")
        print(f"          \_____/  {tabuleiro[14]}   \_____/           |")
        print(f"                \       /                 |")
        print(f"                 \_____/                  |")
        print(f'{Direcao1[1][0]} - {Direcao1[1][1]}')
        print(f'{Direcao2[1][0]} - {Direcao2[1][1]}')
        print(f'{Direcao3[1][0]} - {Direcao3[1][1]}')
        jogada = int(input("Escolha onde quer jogar:"))

        while(tabuleiro[jogada-1]=='P' or tabuleiro[jogada-1] == 'B'):
            jogada = int(input("Local ocupado. Escolha outro lugar:"))

        if(player==True):
            if(tabuleiro[jogada-1]>=10):
                tabuleiro[jogada-1]='B '
            else:
                tabuleiro[jogada-1]='B'
        else:
            if(tabuleiro[jogada-1]>=10):
                tabuleiro[jogada-1]='P '
            else:
                tabuleiro[jogada-1]='P'

def ContaPecas(tuplo):
    nP=0
    nB=0
    i=0
    while(i<3):
        if tabuleiro[tuplo[i]-1]=="B" or tabuleiro[tuplo[i]-1]=="B ":
                nB += 1
        elif tabuleiro[tuplo[i]-1]=="P" or tabuleiro[tuplo[i]-1]=="P ":
                nP += 1
        i +=  1

    if nP > nB and nP> 1:
         return 'P'
    if nP < nB and nB>1:
         return 'B'
    
    return 'X'

def ContaDirecao(direcao):
    i=0
    dP=0
    dB=0

    while i<5:
        V=ContaPecas(direcao[0][i])
        if(V=='P'):
              dP += 1
        elif(V=='B'):
              dB += 1
        i += 1

    direcao[1][0]=dB
    direcao[1][1]=dP
        
        

    
def main():
    op = menu()

    if(op == 1):
        end=0
        player = True
        p1 = input("\n\tIntroduza o nome do Player 1: ")
        p2 = input("\n\tIntroduza o nome do Player 2: ")
        while( end == 0):
            print("\n\t\t" + p1 + " vs " + p2)
            board(player)
            if(player==True):
                player=False
            else:
                player=True
            ContaDirecao(Direcao1)
            ContaDirecao(Direcao2)
            ContaDirecao(Direcao3)
            board(player)

    elif(op == 2):
        print("\n\t Humano vs Minimax")
            
    elif(op == 3):
        print("\n\t Minimax vs Rando") 
        
    elif(op == 0):
        sair()  
    
            
        
    
main()
    