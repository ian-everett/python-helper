# Game board current state
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def check_for_win(current_game):

    def check_row(row, direction):
        # Check if all items in the row are a valid
        # player 1 or 2 and the same player
        if row[0] and row.count(row[0]) == len(row):
            print('Winner player %d [%s]' % (row[0], direction))
            return True
        return False


    # Check for horizontal match
    for row in current_game:
        if check_row(row, '-'):
            break

    else:
        n_elements = len(current_game)

        # Check for verticle match
        for column in range(n_elements):
            row = [row[column] for row in current_game]
            if check_row(row, '|'):
                break

        else:
            # Check dialog top left to bottom right
            row = [current_game[i][i] for i in range(n_elements)]
            
            # Check dialog top right to bottom left
            if not check_row(row, '\\'):
                row = [current_game[(n_elements-1) - i][i] for i in range(n_elements)]
                check_row(row, '/')

def game_board(current_game, player=0, row=0, column=0, display_only=False):
    if not display_only:
        current_game[row][column] = player
    # Redraw current game board state
    print('   a  b  c')
    for count, row in enumerate(current_game):
        print(count, row)
    check_for_win(game)

# Start with a blank board
game_board(game, display_only=True)
game_board(game, player=1, row=0, column=0)
game_board(game, player=1, row=1, column=1)
game_board(game, player=1, row=2, column=2)

