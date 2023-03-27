from board import init, display

WIDTH = 10
HEIGHT = 10


board= init(WIDTH,HEIGHT)

board[4][5] = 1
board[4][6] = 1
board[5][5] = 1
print(board)


display(board)