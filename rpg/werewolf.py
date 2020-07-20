'''
Monster: Vampire
'''
from character import Character
from attacks import ATTACKS

class Werewolf(Character):
    '''
    Werewolf
    '''
    def __init__(self):
        Character.__init__(self, 'Werewolf', 150)
        # Attacks
        self.attacks.append(ATTACKS['Bite'])
        self.attacks.append(ATTACKS['Tear'])

        # Weaknesses
        self.weakness.append(ATTACKS['Fire'])
