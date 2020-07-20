'''
Player Class
'''
from attacks import ATTACKS
from character import Character

class Player(Character):
    '''
    Player
    '''

    def __init__(self, name):
        Character.__init__(self, name, 100)

        # Player starts with these attacks
        self.attacks.append(ATTACKS['Sword'])
        self.attacks.append(ATTACKS['Fire'])
        self.attacks.append(ATTACKS['Stake'])

        # Only the player has strength and magick
        self.strength = 100
        self.magick = 100

    def give_damage(self, attack):
        '''
        Update the players strength and magick
        '''
        strength = attack['strength']
        magick = attack['magick']
        if self.strength - strength >= 0:
            self.strength -= strength
        if self.magick - magick >= 0:
            self.magick -= magick

    def list_attacks(self):
        '''
        List the attacks the player has available
        '''
        return self.attacks
