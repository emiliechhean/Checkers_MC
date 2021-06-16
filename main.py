import math
import random
from src.game import Game
from src.player import Player, RandomPlayer, MCPlayer, KeyboardPlayer
from src.utils import *



### SOURCE :  ###
def main(params):
    
    # start game:
    player1 = KeyboardPlayer(symb = 'o')
    player2 = RandomPlayer(symb = 'x')
    if player1.symb == player2.symb:
        raise exception("Please chose an other symbol for the second player")
    
    game = Game(player1, player2, board_size = params["BOARD_SIZE"])

    # Loop
    done = False

    # game loop:
    while not done:
        # --- Main event loop
        if game.status == 'game over':
            done = True
        print(game)
        if type(game.players[game.turn % 2]) == type(KeyboardPlayer()):
            game.evaluate_click()
        elif type(game.players[game.turn % 2]) == type(RandomPlayer()):
            game.evaluate_click()


###


if __name__ == "__main__":
    params = parse_yaml("parameters.yaml")

    main(params)
    
