'''
RPG test
'''
from player import Player
from zombie import Zombie

def prompt_next_action(player, monster_name):
    '''
    Player has encountered a monster, ask if they want to attack it
    '''
    print("What would you like to attack the %s with" % monster_name)
    attacks = player.list_attacks()
    for i, attack in enumerate(attacks, start=1):
        print('%d:%s  ' % (i, attack['name']), end='')
    print()
    text = input("Enter the number of the attack or 0 to run away ")
    choice = int(text)
    if choice == 0:
        return None

    return attacks[choice - 1]


def attack_monster(player, monster, attack):
    '''
    Attack the monster
    '''
    # Player attacks which takes effort and magick
    print('%s attacks %s with a %s attack' % (player.name, monster.name, attack['name']))
    player.give_damage(attack)
    monster.take_damage(attack)

    # If monster is still alive it fights back
    if monster.is_alive():
        attack = monster.random_attack()
        if attack:
            print('%s attacks with %s' %(monster.name, attack['name']))
            player.take_damage(attack)
    else:
        print('%s has heroically slain the %s' % (player.name, monster.name))


def main():
    '''
    main entry point
    '''
    player = Player('Barry')
    monster = Zombie()
    print('%s approachs a %s' % (player.name, monster.name))

    while monster.is_alive() and player.is_alive():
        # See if player wants to attack the monster
        attack = prompt_next_action(player, monster.name)
        if attack:
            # Player chooses to attack the monster
            attack_monster(player, monster, attack)
        else:
            print('%s runs away like a little girl' % player.name)
            break

        #print('Player health %d' % player.health)
        #print('Player strength %d' % player.strength)
        #print('Player magick %d' % player.magick)
        #print('Monster health %d' % monster.health)
    print('Game over')

if __name__ == "__main__":
    main()
