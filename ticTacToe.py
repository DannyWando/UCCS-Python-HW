"""
Homework 3, Exercise 4
Daniel Wandeler

This program is a tic-tac-toe game. It stores the game state in a data structure and allows
two players to input their moves.
"""

def printBoard(board):
    print('Tic-Tac-Toe Game!')
    for y in range(3):
        for x in range(3):
            print(end=board[x][y])
        print()


def playerTurn(board, stringToken):
    placed = False
    while not placed:
        printBoard(board)
        row = int(input('Please pick a row for your move. 1, 2, or 3:')) % 4 - 1
        column = int(input('Please pick a column for your move. 1, 2, or 3:')) % 4 - 1
        if board[column][row] == '_':
            board[column][row] = stringToken
            placed = True
        else:
            print("That space is TAKEN. Try taking a FREE space.")


if __name__ == '__main__':
    gameBoard = [['_', '_', '_'],
                 ['_', '_', '_'],
                 ['_', '_', '_']]
    player1 = 'X'
    player2 = 'O'
    for x in range(9):
        if x % 2 == 0:
            playerTurn(gameBoard, player1)
        else:
            playerTurn(gameBoard, player2)
    printBoard(gameBoard)
    