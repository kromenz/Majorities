from games.majorities.players.minimax import MinimaxMajoritiesPlayer
from games.majorities.players.random import RandomMajoritiesPlayer
from games.majorities.players.humano import HumanoMajoritiesPlayer
from games.majorities.simulator import MajoritiesSimulator
from games.majorities.state import MajoritiesState
from games.game_simulator import GameSimulator

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()

            


def menu():
    op = -1
    while op not in [0,1,2,3,4]:
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
        print("|\t0. Sair \t\t\t|")
        print("-----------------------------------------")
        op = int(input("\n\tOpção: ")) 
        if op not in [0,1,2,3,4]:
             print("\n\tInsira um valor entre 0 e 4...")

    return op

def main():
    
    while True:
        op = menu()

        num_iterations = 1000

        if(op == 1):
            end = 0
            playerV = True
            sim_name = "\n\tMajorities - Humano vs Humano"
            p1 = input("\n\tIntroduza o nome do Player 1: ")
            p2 = input("\n\tIntroduza o nome do Player 2: ")
            print("\n------------------------------------------------------------------")
            print(f"\t\tMajorities - {p1.center(10)} VS {p2.center(10)}")
            print("------------------------------------------------------------------")

            end = HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV)
            playerV = False
            while end == 0 :
                print("\n------------------------------------------------------------------")
                print(f"\tMajorities - {p1.center(10)} VS {p2.center(10)}")
                print("------------------------------------------------------------------\n")
                end = int(HumanoMajoritiesPlayer(p2).get_action(MajoritiesState,playerV))
                print("\n------------------------------------------------------------------")
                print(f"\tMajorities - {p1.center(10)} VS {p2.center(10)}")
                print("------------------------------------------------------------------\n")
                end = int(HumanoMajoritiesPlayer(p2).get_action(MajoritiesState,playerV))
                if(end!=0):
                    break
                playerV = True
                print("\n------------------------------------------------------------------")
                print(f"\tMajorities - {p1.center(10)} VS {p2.center(10)}")
                print("------------------------------------------------------------------\n")
                
                end = int(HumanoMajoritiesPlayer(p1).get_action(MajoritiesState,playerV))
                print("\n------------------------------------------------------------------")
                print(f"\tMajorities - {p1.center(10)} VS {p2.center(10)}")
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
