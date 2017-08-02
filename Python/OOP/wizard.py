#How to use Super
from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()
        self.intelligence = 10
    def heal(self):
        self.health += 10

class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()
        self.stealth = 10
    def steal(self):
        self.stealth += 5

class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()
        self.strength = 10
    def sacrifice(self):
        self.health -= 5
        
