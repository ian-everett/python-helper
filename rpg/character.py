'''
Character class
'''
import random

class Character:
    '''
    Character
    '''

    def __init__(self, name, health=0):
        self.name = name
        self.health = health
        self.attacks = []
        self.weakness = []


    def take_damage(self, attack):
        '''
        Charcter takes damage
        returns if the character is alive
        '''
        damage = attack['damage']

        # If this charcter has a weakness the
        # the damage taken is more
        if attack in self.weakness:
            damage *= 2
        if (self.health - damage) >= 0:
            self.health -= damage
        return self.is_alive()

    def is_alive(self):
        '''
        Check to see if charcater is alive
        '''
        return self.health > 0

    def random_attack(self):
        '''
        Random attack using the available attacks
        '''
        num = random.randint(0, len(self.attacks) - 1)
        return self.attacks[num]
