import random


class Player:
    """ class  """
    def __init__(self, symb='o'):
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
            print("%s's turn" % str(game.players[game.turn % 2]))
        elif winner == 'draw':
            print("It's a stalemate!")
            game.status = 'game over'
        else:
            print("%s wins!" % winner)
            game.status = 'game over'
            

class KeyboardPlayer(Player):
    def play_next_move(self, game):
        if game.selected_token:
            (row, column) = input(f'Enter the case "(row, column)" in which we want to move the pawn:')
            move = game.is_valid_move(self.symb, game.selected_token, row, column)
            if move[0]: #si cest un valid move (a gauche : true)
                self.play(game, game.selected_token, row, column, move[1])
            elif row == game.selected_token[0] and column == game.selected_token[1]:
                #quand on reclique sur le mm pion, on deselectionne ce pion
                game.selected_token = None
                if game.jumping:
                    game.jumping = False
                    game.next_turn()
            else:
                print('invalid move')

        #quand il a cliqué sur le pion a deplacer
        else: 
            #si ca correspond au symbole du joueur a qui c'est le tour
            (row, column) = input(f'Enter the case "(row, column)" of the moving pawn:')
            if game.game_board[row][column].lower() == self.symb:
                #selected token devient le pion sur lequel on clique en premier
                game.selected_token = [row, column]


class RandomPlayer(Player):
    def get_possible_moves(self, game):
        #if self.symb --> +1 ou -1 en fct
        list_pos = []
        for r,c in self.pawns:
            pos_combi = [(r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1), (r+2, c+2), (r+2, c-2), (r-2, c+2), (r-2, c-2)]
            for combi in pos_combi:
                if 0<=combi[0]<=game.board_size-1 and 0<=combi[1]<=game.board_size-1:
                    if game.is_valid_move(self, (r,c), combi[0], combi[1])[0]:
                        print("valid move", r , c)
                        list_pos.append((r,c), combi)
        return list_pos
    
    def get_random_move(self, game):
        list_pos = self.get_possible_moves(game)
        print(list_pos)
        return random.choice(list_pos)
    
    def play_next_move(self, game):
        pion2pion = self.get_random_move(game)
        print(pion2pion)
        selected_token = pion2pion[0]
        print(selected_token)
        row = pion2pion[0][0]
        column = pion2pion[0][1]
        print(row, column)
        move = game.is_valid_move(self.symb, selected_token, row, column)
        self.play(game, game.selected_token, row, column, move[1])
        
    
class MCPlayer(Player):
    def calcul(self):
        return
    