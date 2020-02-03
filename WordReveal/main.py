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


def print_current_guess(word, current):
    '''
    Outputs the current word guess
    '''
    print("Guess Word: ", end='')
    for letter in word:
        if letter.lower() in current:
            print(letter, end='')
        elif letter == ' ':
            print(' ', end='')
        else:
            print('%c' % '-', end='')
    print('')


def show_drawn_letters(current):
    '''
    Ouputs the currently drawn letters
    '''
    # Display all the letters which have been
    # drawn in alphabetical order
    for item in sorted(current):
        print("%c " % item, end='')


def get_current_state(word, current):
    '''
    Outputs the current game state and returns
    wether the word has been gussed with True or
    False if not yet.
    '''
    print_current_guess(word, current)
    print('')

    # Show all letters that have been picked thus far
    if current != set():
        show_drawn_letters(current)
        print('')

        # Check to see if we have matched all letters if
        # so we we return True to stop cureent game.
        if set(word.lower()).issubset(current):
            return True

    return False


def main():
    '''
    main entry point
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

            # Show current state of game and if we have a match quit loop
            if get_current_state(word, chosen):
                print('Got a match took %d goes.' % (n_goes + 1))
                break

            time.sleep(2.0)



if __name__ == "__main__":
    main()
