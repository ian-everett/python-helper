'''
numpy libary test
'''
import numpy as np

def redraw(board):
    '''
    redraw game board
    '''
    for row in board:
        print(row)

def main():
    '''
    main()
    '''
    current_board = np.zeros((3, 3))    # Create an 3 x 3 array of all zeros

    # fill some data
    current_board[0][0] = 1
    current_board[1][0] = 1
    current_board[2][0] = 1

    # get first column of data
    col = current_board[:, 0]
    print('col %s' % col)
    # check all numbers are equal
    print('Are all numbers in col set to 1? % r' % np.all(col == 1))

    # get first row of data
    row = current_board[0, :]
    print('row %s' % row)
    print('Are all numbers in row set to 1? % r' % np.all(row == 1))

    redraw(current_board)

    b = np.array([[100, 23, 10, 10], [102, 26, 20, 10]])
    print(b.shape)

    print('avg = %s' % np.average(b, 0))
    print('max = %s' % np.max(b, 0))
    print('min = %s' % np.min(b, 0))

if __name__ == "__main__":
    main()
