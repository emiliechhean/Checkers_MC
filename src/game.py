import random
import pygame
from src.utils import *

### SOURCE : ###

class Game:
    """class to keep track of the status of the game."""
    def __init__(self, player1, player2, board_size):
        """
        Start a new game with an empty board and random player going first.
        """
        self.status = 'playing'
        self.turn = random.randrange(2)
        self.players = [player1, player2]
        self.selected_token = None
        self.jumping = False
        pygame.display.set_caption("%s's turn" % str(self.players[self.turn % 2]))
        
        if board_size not in [8, 10]:
            raise Exception("wrong board size, try 8 or 10.")
        self.board_size = board_size
        
        if board_size == 8:
            self.game_board = [['x','-','x','-','x','-','x','-'],
                               ['-','x','-','x','-','x','-','x'],
                               ['x','-','x','-','x','-','x','-'],
                               ['-','-','-','-','-','-','-','-'],
                               ['-','-','-','-','-','-','-','-'],
                               ['-','o','-','o','-','o','-','o'],
                               ['o','-','o','-','o','-','o','-'],
                               ['-','o','-','o','-','o','-','o']]
        if board_size == 10:
            self.game_board = [['x','-','x','-','x','-','x','-','x','-'],
                               ['-','x','-','x','-','x','-','x','-','x'],
                               ['x','-','x','-','x','-','x','-','x','-'],
                               ['-','x','-','x','-','x','-','x','-','x'],
                               ['-','-','-','-','-','-','-','-','-','-'],
                               ['-','-','-','-','-','-','-','-','-','-'],
                               ['o','-','o','-','o','-','o','-','o','-'],
                               ['-','o','-','o','-','o','-','o','-','o'],
                               ['o','-','o','-','o','-','o','-','o','-'],
                               ['-','o','-','o','-','o','-','o','-','o']]
        player1.init_moves(self)
        player2.init_moves(self)

    def evaluate_click(self, mouse_pos, params):
        """
        Select a token if none is selected.
        Move token to a square if it is a valid move.
        Start a new game if the game is over.
        """
        player = self.players[self.turn % 2]
        player_symb = str(self.players[self.turn % 2])
        if self.status == 'playing':
            row, column = get_clicked_row(mouse_pos, params), get_clicked_column(mouse_pos, params)
            if self.selected_token:
                move = self.is_valid_move(player_symb, self.selected_token, row, column)
                if move[0]:
                    player.play(self, self.selected_token, row, column, move[1])
                elif row == self.selected_token[0] and column == self.selected_token[1]:
                    self.selected_token = None
                    if self.jumping:
                        self.jumping = False
                        self.next_turn()
                else:
                    print('invalid move')
            else:
                if self.game_board[row][column].lower() == player_symb:
                    self.selected_token = [row, column]
        elif self.status == 'game over':
            self.__init__()

    def is_valid_move(self, player, token_location, to_row, to_col):
        """
        Check if clicked location is a valid square for player to move to.
        """
        from_row = token_location[0]
        from_col = token_location[1]
        token_char = self.game_board[from_row][from_col]
        if self.game_board[to_row][to_col] != '-':
            return False, None
        if (((token_char.isupper() and abs(from_row - to_row) == 1) or (player == 'x' and to_row - from_row == 1) or
             (player == 'o' and from_row - to_row == 1)) and abs(from_col - to_col) == 1) and not self.jumping:
            return True, None
        if (((token_char.isupper() and abs(from_row - to_row) == 2) or (player == 'x' and to_row - from_row == 2) or
             (player == 'o' and from_row - to_row == 2)) and abs(from_col - to_col) == 2):
            jump_row = int((to_row - from_row) / 2 + from_row)
            jump_col = int((to_col - from_col) / 2 + from_col)
            if self.game_board[jump_row][jump_col].lower() not in [player, '-']:
                return True, [jump_row, jump_col]
        return False, None

    

    def next_turn(self):
        self.turn += 1
        pygame.display.set_caption("%s's turn" % self.players[self.turn % 2])

    def check_winner(self):
        """
        check to see if someone won, or if it is a draw.
        """
        x = sum([row.count('x') + row.count('X') for row in self.game_board])
        if x == 0:
            return 'o'
        o = sum([row.count('o') + row.count('O') for row in self.game_board])
        if o == 0:
            return 'x'
        if x == 1 and o == 1:
            return 'draw'
        return None

    def draw(self, screen, params):
        """
        Draw the game board and the X's and O's.
        """
        for i in range(9):
            pygame.draw.line(screen, params['WHITE'], [i * params['WIDTH'] / 8, 0], [i * params['WIDTH'] / 8, params['HEIGHT'] ], 5)
            pygame.draw.line(screen, params['WHITE'], [0, i * params['HEIGHT'] / 8], [params['WIDTH'], i * params['HEIGHT'] / 8], 5)
        font = pygame.font.SysFont('Calibri', params['MARK_SIZE'], False, False)
        for r in range(len(self.game_board)):
            for c in range(len(self.game_board[r])):
                mark = self.game_board[r][c]
                if str(self.players[self.turn % 2]) == mark.lower():
                    color = params['YELLOW']
                else:
                    color = params['WHITE']
                if self.selected_token:
                    if self.selected_token[0] == r and self.selected_token[1] == c:
                        color = params['RED']
                if mark != '-':
                    mark_text = font.render(self.game_board[r][c], True, color)
                    x = params['WIDTH'] / 8 * c + params['WIDTH'] / 16
                    y = params['HEIGHT'] / 8 * r + params['HEIGHT'] / 16
                    screen.blit(mark_text, [x - mark_text.get_width() / 2, y - mark_text.get_height() / 2])

###