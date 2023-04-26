from games.majorities.players.minimax import MinimaxMajoritiesPlayer
from games.majorities.players.random import RandomMajoritiesPlayer
from games.majorities.players.humano import HumanoMajoritiesPlayer
from games.majorities.simulator import MajoritiesSimulator
from games.majorities.state import MajoritiesState
from games.game_simulator import GameSimulator
import time
import os

ops = [0,1,2,3,4,5]

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()

# Limpar o terminal
def clear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix (Linux, macOS)
        os.system('clear')

def sair():
    clear()
    print("\n---------------------------------------------------")
    print("\tObrigado por ter jogado o Majorities!\t")
    print("---------------------------------------------------")
    time.sleep(5)  #delay
    clear()
    exit()  #kill programm
    

def regras():
    print("\n-------------------------------------------------------------------------------------------------")
    print("\t\t\t\tRegras do Majorities!\t\t")
    print("-------------------------------------------------------------------------------------------------")
    print("|\tO jogo Majorities é jogado por dois jogadores, cada um com um conjunto de peças.\t|")
    print("|\tO objetivo é conseguir:\t\t\t\t\t\t\t\t\t|")
    print("|\t1. Controlar a maioria dos espaços numa linha para ganhar a linha.\t\t\t|")
    print("|\t2. Controlar the maioria das linhas paralelas para ganhar a direção.\t\t\t|")
    print("|\t3. Controlar a maioria das três direções para ganhar o jogo.\t\t\t\t|")
    print("-------------------------------------------------------------------------------------------------")
    print("\t\t\t\tIntruções do Majorities!\t\t")
    print("-------------------------------------------------------------------------------------------------")
    print("|\t1. Para jogar basta selecionar uma opção no menu.\t\t\t\t\t|")
    print("|\t2. De seguida, selecionar uma posição onde quer colocar a sua peça.\t\t\t|")
    print("|\t3.O jogo termina quando não há mais espaços livres no tabuleiro ou quando\t\t|")
    print("|\tum dos jogadores ganhar a maior parte das direções.\t\t\t\t\t|")
    print("-------------------------------------------------------------------------------------------------\n")
    
    
    # Espera por input
    while True:
        try:
            op = int(input("\n\tSelecione '0' e 'ENTER', para voltar atrás: "))
            if op == 0:
                break
            else:
                print("Opção inválida. Digite '0' para voltar ao menu principal.")
        except ValueError:
            print("Opção inválida. Digite '0' para voltar ao menu principal.")

    clear()


def menu():
    op = -1
    while op not in ops:
        print("\n-----------------------------------------")
        print("|\tBem vindo ao Majorities!\t|")
        print("-----------------------------------------")
        print("|\t1. Jogar contra Humano \t\t|")
        print("\n")
        print("|\t2. Jogar contra Minimax \t|")
        print("\n")
        print("|\t3. Jogar Minimax contra Random \t|")
        print("\n")
        print("|\t4. Jogar Humano contra Random \t|")
        print("\n")
        print("|\t5. Regras do jogo \t\t|")
        print("\n")
        print("|\t0. Sair \t\t\t|")
        print("-----------------------------------------")
        op = int(input("\n\tOpção: ")) 
        if op not in ops:
             print("\n\tInsira um valor entre 0 e 4...")

    return op

def main():
    
    while True:
        op = menu()

        num_iterations = 1000
        clear()
        if(op == 1):
            end = 0
            playerV = True
            sim_name = "\n\tMajorities - Humano vs Humano"
            p1 = input("\n\tIntroduza o nome do Player 1: ")
            p2 = input("\n\tIntroduza o nome do Player 2: ")
            clear()
            print("\n------------------------------------------------------------------")
            print(f"\t\tMajorities - {p1.center(10)} VS {p2.center(10)}")
            print("------------------------------------------------------------------")

            end = HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV)
            clear()
            playerV = False
            while end == 0 :
                print("\n------------------------------------------------------------------")
                print(f"\t\tMajorities - {p1.center(10)} VS {p2.center(10)}")
                print("------------------------------------------------------------------\n")
                end = int(HumanoMajoritiesPlayer(p2).get_action(MajoritiesState,playerV))
                clear()
                print("\n------------------------------------------------------------------")
                print(f"\t\tMajorities - {p1.center(10)} VS {p2.center(10)}")
                print("------------------------------------------------------------------\n")
                end = int(HumanoMajoritiesPlayer(p2).get_action(MajoritiesState,playerV))
                clear()
                if(end != 0):
                    break
                playerV = True
                print("\n------------------------------------------------------------------")
                print(f"\t\tMajorities - {p1.center(10)} VS {p2.center(10)}")
                print("------------------------------------------------------------------\n")
                
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                clear()
                print("\n------------------------------------------------------------------")
                print(f"\t\tMajorities - {p1.center(10)} VS {p2.center(10)}")
                print("------------------------------------------------------------------\n")
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                clear()
                if(end != 0):
                    break
                playerV = False
                
            if end == 1:
                print("\n-----------------------------------------")
                print(f"\tVencedor - {p1.center(10)}\t\t")
                print("-----------------------------------------\n")
                
            else:
                print("\n-----------------------------------------")
                print(f"\tVencedor - {p2.center(10)}\t\t")
                print("-----------------------------------------")
                
            jogar_novamente = input("\nDeseja jogar novamente? (S/N) ")

            if jogar_novamente.lower() == "s":
                continue  # começa o loop novamente
            if jogar_novamente.lower() == "n":
                print("\n\tObrigado por ter jogado, volte sempre!")
                break  # interrompe o loop e sai do programa
            
            '''
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
            '''
            
        elif(op == 2):
            print("\n\t Humano vs Minimax")
                
        elif(op == 3):
            print("\n\t Minimax vs Rando")

        elif(op == 4):
            end = 0
            playerV = True
            p1 = input("\n\tIntroduza o nome do Player 1: ")
            print("\n------------------------------------------------------------------")
            print(f"\t\tMajorities - {p1.center(10)} VS Random")
            print("------------------------------------------------------------------")

            end = HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV)
            playerV = False
            while end == 0 :
                end = int(RandomMajoritiesPlayer("Random").get_action(MajoritiesState,playerV))
                end = int(RandomMajoritiesPlayer("Random").get_action(MajoritiesState,playerV))
                if(end!=0):
                    break
                playerV = True
                print("\n------------------------------------------------------------------")
                print(f"\tMajorities - {p1.center(10)} VS Random")
                print("------------------------------------------------------------------\n")
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                print("\n------------------------------------------------------------------")
                print(f"\tMajorities - {p1.center(10)} VS Random")
                print("------------------------------------------------------------------\n")
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                if(end != 0):
                    break
                playerV = False
                
            if end == 1:
                print("\n-----------------------------------------")
                print(f"\tVencedor - {p1.center(10)}\t\t")
                print("-----------------------------------------\n")
                
            else:
                print("\n-----------------------------------------")
                print(f"\tVencedor - Random")
                print("-----------------------------------------")  

            jogar_novamente = input("\nDeseja jogar novamente? (S/N) ")

            if jogar_novamente.lower() == "s":
                continue  # começa o loop novamente
            if jogar_novamente.lower() == "n":
                print("\n\tObrigado por ter jogado, volte sempre!")
                break  # interrompe o loop e sai do programa
        elif(op == 5):
            regras()
            
            
        elif(op == 0):
            sair()
    
    
    mj_simulations = [
        {
            "name": sim_name,
            "player1": HumanoMajoritiesPlayer(p1),
            "player2": HumanoMajoritiesPlayer(p2)
        },
    ]

    for sim in mj_simulations:
        run_simulation(sim["name"], MajoritiesSimulator(sim["player1"], sim["player2"]), 1)
    

if __name__ == "__main__":
    main()
