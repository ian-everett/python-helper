'''
Reveals a word and the person can stop and guess it
'''
import random
import time

# alphabet
ALPHABET = ('abcdefghijklmnopqrstuvwxyz')

def get_random_word(words):
    '''
    returns a random word from a list of words or blank ''
    if no words in list of words
    '''
    length = len(words)
    if length > 1:
        index = random.randint(0, length - 1)
        return words[index].rstrip('\n')

    return ''

def print_current_state(word, current):
    '''
    print_current_state
    '''
    print("Guess Word: ", end='')
    for letter in word:
        if letter.lower() in current:
            print(letter, end='')
        else:
            print('%c' % '-', end='')
    print('')

    # Show all letters that have been picked thus far
    if current != set():
        # Display in alphabetical order
        for item in sorted(current):
            print("%c " % item, end='')
        print('')
        print('')

        # Check to see if we have matched all letters


def main():
    '''
    main()
    '''

    # Open given file for reading, list of words should
    # be a word each line with a \n at the end
    with open('./states.txt', 'r') as file:
        words = file.readlines()

        # Return a random word from that list of words
        word = get_random_word(words)

        # Preset alphabet set, we will slowly remove each
        # letter as we randlonly select it.
        # Chosen starts blank as it holds the letters drawn
        alphabet = set(ALPHABET)
        chosen = set()

        # We have maxium 26 letters so get each of them randomly
        for n_goes in range(len(ALPHABET)):

            # Get next letter and remove it from list so we can't choose it again
            letter = random.choice(tuple(alphabet))
            alphabet.remove(letter)

            # Add the next letter to the chosen set
            chosen.add(letter)
            print_current_state(word, chosen)

            time.sleep(2.0)



if __name__ == "__main__":
    main()
