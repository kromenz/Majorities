from games.majorities.players.minimax import MinimaxMajoritiesPlayer
from games.majorities.players.greedy import GreedyMajoritiesPlayer
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
        
def texto(p1, p2):
    print("\n------------------------------------------------------------------")
    print(f"\t\tMajorities - {p1.center(10)} VS {p2.center(10)}")
    print("------------------------------------------------------------------")

def texto_w(p):
    print("\n-----------------------------------------")
    print(f"\tVencedor - {p.center(10)}\t\t")
    print("-----------------------------------------\n")
    
def joga_nova():
    
    jogar = ""
    while jogar.lower() not in ["s", "n"]:
        jogar = input("\n\tDeseja jogar novamente? (S/N) ")

        if jogar.lower() == "s":
            MajoritiesState.reset_board()
            clear()
            continue  # começa o loop novamente
        if jogar.lower() == "n":
            sair()
            break  # interrompe o loop e sai do programa
        else:
            print("\n\tIntroduza uma das opções: 'S' ou 'N'")

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
    
    input()
    clear()

def menu():
    op = -1
    while op not in ops:
        print("\n-----------------------------------------")
        print("|\tBem vindo ao Majorities!\t|")
        print("-----------------------------------------")
        print("|\t1. Jogar contra Humano \t\t|")
        print("\n")
        print("|\t2. Jogar contra Greedy \t\t|")
        print("\n")
        print("|\t3. Jogar contra Random \t\t|")
        print("\n")
        print("|\t4. Jogar entre computas \t|")
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
            sim_name = "Majorities - Humano vs Humano"
            p1 = input("\n\tIntroduza o nome do Player 1: ")
            p2 = input("\n\tIntroduza o nome do Player 2: ")
            clear()
            texto(p1, p2)
            end = HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV)
            playerV = False
            while end == 0 :
                texto(p1, p2)
                end = int(HumanoMajoritiesPlayer(p2).get_action(MajoritiesState,playerV))
                texto(p1, p2)
                end = int(HumanoMajoritiesPlayer(p2).get_action(MajoritiesState,playerV))
                if(end != 0):
                    break
                playerV = True
                texto(p1, p2)
                
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                texto(p1, p2)
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                if(end != 0):
                    break
                playerV = False
                
            if end == 1:
                texto_w(p1)
            else:
                texto_w(p2)
            joga_nova()
            
        elif(op == 2):
            end = 0
            playerV = True
            p1 = input("\n\tIntroduza o nome do Player 1: ")
            p2 = "Greedy"
            texto(p1, p2)
            end = HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV)
            playerV = False
            while end == 0 :
                end = int(GreedyMajoritiesPlayer("Greedy").get_action(MajoritiesState,playerV))
                if(end!=0):
                    break
                playerV = True
                texto(p1, p2)
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                texto(p1, p2)
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                if(end != 0):
                    break
                playerV = False
            if end == 1:
                texto_w(p1)
            else:
                texto_w(p2)
            joga_nova()
        
        elif(op == 3):
            end = 0
            playerV = True
            p1 = input("\n\tIntroduza o nome do Player 1: ")
            p2 = "Random"
            texto(p1, p2)
            end = HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV)
            playerV = False
            while end == 0 :
                end = int(RandomMajoritiesPlayer("Random").get_action(MajoritiesState,playerV))
                end = int(RandomMajoritiesPlayer("Random").get_action(MajoritiesState,playerV))
                if(end!=0):
                    break
                playerV = True
                texto(p1, p2)
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                texto(p1, p2)
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                if(end != 0):
                    break
                playerV = False
                
            if end == 1:
                texto_w(p1)
            else:
                texto_w(p2)
            joga_nova()
        
        elif(op == 4):
            pass

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
