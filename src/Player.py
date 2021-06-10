class Player:
    """ class  """
    def __init__(self, symb, ):
        if symb != 'x' and symb != 'o':
            raise Exception("wrong symbol, try 'x' or 'o' ")
        self.symb = symb 
            

class KeyboardPlayer(Player):
    
class RandomPlayer(Player):
    
class MCPlayer(Player):
    