import time


tabuleiro=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
PecasA= []
PecasB= []

def sair():
    print("-----------------------------------------")
    print("|\tObrigado por jogar o Majorities |\n|\tVolte Sempre!\t\t\t|")
    print("-----------------------------------------")
    time.sleep(1)
    exit()
    
def menu():
    print("-----------------------------------------")
    print("|\tBem vindo ao Majorities!\t|")
    print("-----------------------------------------")
    print("|\t1. Jogar contra Humano \t\t|")
    print("\n")
    print("|\t2. Jogar contra Minimax \t|")
    print("\n")
    print("|\t3. Jogar Minimax contra Random \t|")
    print("\n")
    print("|\t4. Sair \t\t\t|")
    print("-----------------------------------------")
    op = int(input("\n\tOpção: ")) 
    return op

def board(player):
        print(f"                  _____")
        print(f"                 /     \\")
        print(f"           _____/   {tabuleiro[0]}   \\_____")
        print(f"          /     \       /     \\")
        print(f"    _____/   {tabuleiro[1]}   \_____/   {tabuleiro[2]}   \\_____")
        print(f"   /     \       / XXX \       /     \\")
        print(f"  /   {tabuleiro[3]}   \_____/ XXXXX \_____/   {tabuleiro[4]}   \\")
        print(f"  \       /     \ XXXXX /     \       /")
        print(f"   \_____/   {tabuleiro[5]}   \_____/   {tabuleiro[6]}   \_____/")
        print(f"   /     \       / XXX \       /     \\")
        print(f"  /   {tabuleiro[7]}   \_____/ XXXXX \_____/   {tabuleiro[8]}   \\")
        print(f"  \       / XXX \ XXXXX / XXX \       /")
        print(f"   \_____/ XXXXX \_____/ XXXXX \_____/")
        print(f"   /     \ XXXXX /     \ XXXXX /     \\")
        print(f"  /  {tabuleiro[9]}   \_____/  {tabuleiro[10]}   \_____/  {tabuleiro[11]}   \\")
        print(f"  \       /     \       /     \       /")
        print(f"   \_____/  {tabuleiro[12]}   \_____/  {tabuleiro[13]}   \_____/")
        print(f"         \       /     \       /")
        print(f"          \_____/  {tabuleiro[14]}   \_____/")
        print(f"                \       /")
        print(f"                 \_____/")
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

    
    
    
def main():
    
    op = menu()
    
    if(op == 1):
        end=0
        player = True
        while( end==0):
            print("\n\t Humano vs Humano")
            board(player)
            if(player==True):
                player=False
            else:
                player=True
            board(player)

    elif(op == 2):
        print("\n\t Humano vs Minimax")
        
    elif(op == 3):
        print("\n\t Minimax vs Rando") 
        
    elif(op == 4):
        sair()
    else:
        print("\n\tEscolha uma das opções acima....")
        
        
    
            
    
    

main()
    