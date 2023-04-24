#from games.majorities.players.greedy import GreedyMajoritiesPlayer
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


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 1000

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
