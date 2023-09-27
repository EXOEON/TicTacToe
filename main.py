#simple tic tac toe game

def clearconsole():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


#9x9 board
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_board():
    print('  1   2   3 ')
    print('a ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(' ---|---|----')
    print('b ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(' ---|---|----')
    print('c ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_clear(board, move):
    if board[move] == ' ':
        return True
    else:
        return False

def check_win(board):
    if board[0] == board[1] == board[2] != ' ':
        return True
    elif board[3] == board[4] == board[5] != ' ':
        return True
    elif board[6] == board[7] == board[8] != ' ':
        return True
    elif board[0] == board[3] == board[6] != ' ':
        return True
    elif board[1] == board[4] == board[7] != ' ':
        return True
    elif board[2] == board[5] == board[8] != ' ':
        return True
    elif board[0] == board[4] == board[8] != ' ':
        return True
    elif board[2] == board[4] == board[6] != ' ':
        return True
    else:
        return False

def check_tie(board):
    for i in board:
        if i == ' ':
            return False
    return True

clearconsole()

print('Welcome to Tic Tac Toe!')
print('To play, enter the letter and number of the space you want to play in. (ex. a1, b2, c3)')
print_board()


#main game loop
while True:
    while True:
        #player 1 turn
        current_turn = input('Player 1, enter your move: ')
        if current_turn == 'a1':
            if check_clear(board, 0):
                board[0] = 'X'
                break
        elif current_turn == 'a2':
            if check_clear(board, 1):
                board[1] = 'X'
                break
        elif current_turn == 'a3':
            if check_clear(board, 2):
                board[2] = 'X'
                break
        elif current_turn == 'b1':
            if check_clear(board, 3):
                board[3] = 'X'
                break
        elif current_turn == 'b2':
            if check_clear(board, 4):
                board[4] = 'X'
                break
        elif current_turn == 'b3':
            if check_clear(board, 5):
                board[5] = 'X'
                break
        elif current_turn == 'c1':
            if check_clear(board, 6):
                board[6] = 'X'
                break
        elif current_turn == 'c2':
            if check_clear(board, 7):
                board[7] = 'X'
                break
        elif current_turn == 'c3':
            if check_clear(board, 8):
                board[8] = 'X'
                break
        else:
            print('Invalid move, try again.')
    clearconsole()
    print_board()
    if check_tie(board):
        print('Tie game!')
        break
    if check_win(board):
        print('Player 1 wins!')
        break
    
    while True:
        #player 2 turn
        current_turn = input('Player 2, enter your move: ')
        if current_turn == 'a1':
            if check_clear(board, 0):
                board[0] = 'O'
                break
        elif current_turn == 'a2':
            if check_clear(board, 1):
                board[1] = 'O'
                break
        elif current_turn == 'a3':
            if check_clear(board, 2):
                board[2] = 'O'
                break
        elif current_turn == 'b1':
            if check_clear(board, 3):
                board[3] = 'O'
                break
        elif current_turn == 'b2':
            if check_clear(board, 4):
                board[4] = 'O'
                break
        elif current_turn == 'b3':
            if check_clear(board, 5):
                board[5] = 'O'
                break
        elif current_turn == 'c1':
            if check_clear(board, 6):
                board[6] = 'O'
                break
        elif current_turn == 'c2':
            if check_clear(board, 7):
                board[7] = 'O'
                break
        elif current_turn == 'c3':
            if check_clear(board, 8):
                board[8] = 'O'
                break
        else:
            print('Invalid move, try again.')
    clearconsole()
    print_board()
    if check_tie(board):
        print('Tie game!')
        break
    if check_win(board):
        print('Player 2 wins!')
        break
            
            
