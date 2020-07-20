'''
Monster: Vampire
'''
from character import Character
from attacks import ATTACKS

class Vampire(Character):
    '''
    Vampire
    '''
    def __init__(self):
        Character.__init__(self, 'Vampire', 50)
        # Attacks
        self.attacks.append(ATTACKS['Bite'])

        # Weaknesses
        self.weakness.append(ATTACKS['Stake'])
        self.weakness.append(ATTACKS['Fire'])
