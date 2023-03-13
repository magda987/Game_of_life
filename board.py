def init(width, height):
    board = []

    for x in range(height):
        row = []
        for y in range(width):
            row.append(0)
        board.append(row)
    return board


def display(board):
    for row in board:
        print(row)
