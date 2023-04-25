from games.majorities.players.minimax import MinimaxMajoritiesPlayer
from games.majorities.players.random import RandomMajoritiesPlayer
from games.majorities.simulator import MajoritiesSimulator
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

def main():
    
    op = menu()

    num_iterations = 1000

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
    
    
    mj_simulations = [
        # uncomment to play as human
        #{
        #    "name": "Majorities - Human VS Random",
        #    "player1": HumanMajoritiesPlayer("Human"),
        #    "player2": RandomMajoritiesPlayer("Random")
        #},
        {
            "name": "Majorities - Random VS Random",
            "player1": RandomMajoritiesPlayer("Random 1"),
            "player2": RandomMajoritiesPlayer("Random 2")
        },
        #{
        #    "name": "Majorities - Greedy VS Random",
        #    "player1": GreedyMajoritiesPlayer("Greedy"),
        #    "player2": RandomMajoritiesPlayer("Random")
        #},
        #{
        #    "name": "Minimax VS Random",
        #    "player1": MinimaxMajoritiesPlayer("Minimax"),
        #    "player2": RandomMajoritiesPlayer("Random")
        #}
        #{
        #    "name": "Minimax VS Greedy",
        #    "player1": MinimaxMajoritiesPlayer("Minimax"),
        #    "player2": GreedyMajoritiesPlayer("Greedy")
        #}
    ]

    
    
    for sim in mj_simulations:
        run_simulation(sim["name"], MajoritiesSimulator(sim["player1"], sim["player2"]), 1)

if __name__ == "__main__":
    main()
