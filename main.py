import pygame
import math
import random
from src.game import Game
from src.player import Player, RandomPlayer, MCPlayer, KeyboardPlayer
from src.utils import *

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)
TRANS    = (   1,   2,   3)

# CONSTANTS:
WIDTH = 700
HEIGHT = 700
MARK_SIZE = 50

### SOURCE :  ###
def main(params):
    
    # start pygame:
    pygame.init()
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)

    # start game:
    game = Game(board_size = params["BOARD_SIZE"])

    player = KeyboardPlayer(symb = 'x')
    print(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # game loop:
    while not done:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                entry = str(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                game.evaluate_click(pygame.mouse.get_pos())

        # --- Drawing code should go here

        # First, clear the screen to black. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)

        # draw the game board and marks:
        game.draw()

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

###


if __name__ == "__main__":
    params = parse_yaml("parameters.yaml")
    main(params)
    
