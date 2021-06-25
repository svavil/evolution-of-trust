class Bot():
    def __init__(self):
        self.history = []
    
    def move(self):
        raise NotImplementedError
        
    def append_history(self, move):
        self.history.append(move)

class AlwaysCooperate(Bot):
    def __init__(self):
        super().__init__()
    
    def move(self):
        return "C"

class AlwaysBetray(Bot):
    def __init__(self):
        super().__init__()
    
    def move(self):
        return "N"

class Copycat(Bot):
    def __init__(self):
        super().__init__()
    
    def move(self):
        if len(self.history) < 1:
            return "C"
        return self.history[-1]
    
from random import choice
class Random(Bot):
    def __init__(self):
        super().__init__()
    
    def move(self):
        return choice("CN")
