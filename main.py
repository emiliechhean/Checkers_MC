import math
import random
from src.game import Game
from src.player import Player, RandomPlayer, MCPlayer, KeyboardPlayer
from src.utils import *



### SOURCE :  ###
def main(params):
    
    # start game:
    if params['PLAYER1']=='Keyboard':
        player1 = KeyboardPlayer(symb = 'x')
    elif params['PLAYER1']=='Random':
        player1 = RandomPlayer(symb = 'x')
    if params['PLAYER2']=='Keyboard':
        player2 = KeyboardPlayer(symb = 'o')
    elif params['PLAYER2']=='Random':
        player2 = RandomPlayer(symb = 'o')
    if player1.symb == player2.symb:
        raise exception("Please chose an other symbol for the second player")
    
    game = Game(player1, player2, board_size = params["BOARD_SIZE"])
    print(game)

    # Loop
    done = False

    # game loop:
    while not done:
        # --- Main event loop
        
        if game.status == 'game over':
            done = True
        game.evaluate_click()


###


if __name__ == "__main__":
    params = parse_yaml("parameters.yaml")

    main(params)
    
