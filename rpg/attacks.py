'''
Define the attacks
'''
ATTACKS = {}
# Monster attack only gives damage
ATTACKS['Bite'] = {'name': 'Bite', 'damage': 12, 'strength': 0, 'magick': 0}
ATTACKS['Bludgeon'] = {'name': 'Bludgeon', 'damage': 10, 'strength': 0, 'magick': 0}
ATTACKS['Tear'] = {'name': 'Tear', 'damage': 5, 'strength': 0, 'magick': 0}
ATTACKS['Moan'] = {'name': 'Moan', 'damage': 0, 'strength': 0, 'magick': 0}

# Player attacks give damage but take strength and magick
ATTACKS['Fire'] = {'name': 'Fire', 'damage': 5, 'strength': 0, 'magick': 20}
ATTACKS['Sword'] = {'name': 'Sword', 'damage': 5, 'strength': 30, 'magick': 0}
ATTACKS['Stake'] = {'name': 'Stake', 'damage': 5, 'strength': 30, 'magick': 0}
