import random
import os
#simple tic tac toe game

def clearconsole():
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

print('Welcome to Tic Tac Toe! Press 1 to play against another player, or 2 to play against the computer.')
while True:
    gamemode = input('Enter your choice: ')
    if gamemode == '1' or gamemode == '2':
        break
    else:
        print('Invalid choice, try again.')


clearconsole()

if gamemode == '1':
    print('To play, enter the letter and number of the space you want to play in. (ex. a1, b2, c3)')
    print_board()


    # 2 player main game loop
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


if gamemode == '2':
    print('To play, enter the letter and number of the space you want to play in. (ex. a1, b2, c3). The computer will play as O.')

    print_board()

    # 1 player main game loop
    while True:
        #player 1 turn
        while True:
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
            print('You win!')
            break

        #computer turn
        if not check_win(board):
            # check for winning move
            for i in range(9):
                if check_clear(board, i):
                    board[i] = 'O'
                    if check_win(board):
                        break
                    else:
                        board[i] = ' '
            else:
                # check for blocking move
                for i in range(9):
                    if check_clear(board, i):
                        board[i] = 'X'
                        if check_win(board):
                            board[i] = 'O'
                            break
                        else:
                            board[i] = ' '
                else:
                    # play random move
                    while True:
                        i = random.randint(0, 8)
                        if check_clear(board, i):
                            board[i] = 'O'
                            break

        clearconsole()
        print_board()
        if check_tie(board):
            print('Tie game!')
            break
        if check_win(board):
            print('The computer wins!')
            break

            
