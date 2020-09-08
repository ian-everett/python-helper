'''
Monster: Zombie
'''
from character import Character
from attacks import ATTACKS

class Zombie(Character):
    '''
    Zombie
    '''
    def __init__(self):
        Character.__init__(self, 'Zombie', 50)
        # Attacks
        self.attacks.append(ATTACKS['Bite'])
        self.attacks.append(ATTACKS['Tear'])
        self.attacks.append(ATTACKS['Moan'])
        self.attacks.append(ATTACKS['Bludgeon'])

        # Weaknesses
        self.weakness.append(ATTACKS['Sword'])
        self.weakness.append(ATTACKS['Fire'])
