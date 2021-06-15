import random
import pygame


class Player:
    """ class  """
    def __init__(self, symb):
        if symb != 'x' and symb != 'o':
            raise Exception("wrong symbol, try 'x' or 'o' ")
        self.symb = symb
        self.pawns = []
        self.checkers = []
        #init pos combi ici
    
    def __str__(self):
        return self.symb
    
    def init_moves(self, game):
        for r in range(len(game.game_board)):
            for c in range(len(game.game_board[r])):
                if game.game_board[r][c]==self.symb:
                    self.pawns.append((r,c))
            

class KeyboardPlayer(Player):
    def play(self, game, token_location, to_row, to_col, jump):
        """
        Move selected token to a particular square, then check to see if the game is over.
        """
        from_row = token_location[0]
        from_col = token_location[1]
        token_char = game.game_board[from_row][from_col]
        game.game_board[to_row][to_col] = token_char
        game.game_board[from_row][from_col] = '-'
        if (self.symb == 'x' and to_row == 7) or (self.symb == 'o' and to_row == 0):
            game.game_board[to_row][to_col] = token_char.upper()
        if jump:
            game.game_board[jump[0]][jump[1]] = '-'
            game.selected_token = [to_row, to_col]
            game.jumping = True
        else:
            game.selected_token = None
            game.next_turn()
        winner = game.check_winner()
        if winner is None:
            pygame.display.set_caption("%s's turn" % str(game.players[game.turn % 2]))
        elif winner == 'draw':
            pygame.display.set_caption("It's a stalemate! Click to start again")
            game.status = 'game over'
        else:
            pygame.display.set_caption("%s wins! Click to start again" % winner)
            game.status = 'game over'


class RandomPlayer(Player):
    def get_possible_moves(self, game):
        #if self.symb --> +1 ou -1 en fct
        list_pos = []
        for r,c in self.pawns:
            pos_combi = [(r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1), (r+2, c+2), (r+2, c-2), (r-2, c+2), (r-2, c-2)]
            for combi in pos_combi:
                if game.is_valid_move(self, (r,c), combi[0], combi[1])[0]:
                    list_pos.append((r,c), combi)
        return list_pos
    
    def get_random_combi(self, game):
        list_pos = get_possible_moves(game)
        return random.choice(list_pos)
        
    
class MCPlayer(Player):
    def calcul(self):
        return
    