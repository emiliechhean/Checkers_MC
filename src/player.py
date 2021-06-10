class Player:
    """ class  """
    def __init__(self, symb):
        if symb != 'x' and symb != 'o':
            raise Exception("wrong symbol, try 'x' or 'o' ")
        self.symb = symb 
            

class KeyboardPlayer(Player):
    def calcul(self):
        return
    
class RandomPlayer(Player):
    def calcul(self):
        return
    
class MCPlayer(Player):
    def calcul(self):
        return
    