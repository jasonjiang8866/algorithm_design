SIZE = 9

board = ((5, 3, 4, 6, 7, 8, 9, 1, 2),
(6, 0, 2, 1, 9, 0, 3, 4, 0),
(1, 9, 8, 3, 4, 2, 0, 6, 7),
(8, 5, 9, 7, 6, 1, 4, 2, 3),
(4, 2, 0, 8, 5, 3, 7, 9, 1),
(7, 1, 3, 9, 2, 4, 8, 5, 6),
(9, 6, 1, 0, 3, 7, 2, 8, 4),
(2, 8, 7, 4, 1, 9, 6, 0, 5),
(3, 4, 5, 2, 8, 6, 1, 7, 9))

def easy_sudoku(x, y, n):
    # write your code below
    # either return "No violation" or return "Violation"
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[x-1][j]==n or board[i][y-1]==n:
                return 'Violation'
    return 'No violation'

print(easy_sudoku(2, 2, 7))
print(easy_sudoku(2, 6, 8))
print(easy_sudoku(3, 7, 5))
print(easy_sudoku(2, 9, 9))
print(easy_sudoku(2, 9, 2))
print(easy_sudoku(2, 9, 6))

'''
Each column contains digits from 1 to 9 only one time each AND
Each row contains digits from 1 to 9 only one time each.

'''
