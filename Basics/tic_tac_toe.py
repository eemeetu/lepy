import random as ai
import numpy as np

def show_board(board):
    print (' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n-----------' +
           '\n ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n-----------'
           + '\n ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n')

def rock_paper_s():
    choice = None
    while choice == None:
        player = input('Choose and enter - Rock (type: 1), Paper (2) or Scissors(3): ')
        if player == '1':
            pls = 0
        elif player == '2':
            pls = 1
        elif player == '3':
            pls = 2
        else:
            pls = 5
        comp = ai.randint(0, 2)
        if comp == 0:
            print ('Computer decided to throw ROCK!!!')
        elif comp == 1:
            print ('Computer decided to throw PAPER!!!')
        elif comp == 2:
            print ('Computer gonna cut ya with SCISSORS!!!')
        if (comp == 1 and pls == 0) or (comp == 0 and pls == 2) or (comp == 2 and pls == 1):
            print ('You lost to AI this time, you play as "O"')
            choice = 0
            return 0
        elif pls == 5:
            print ('But you have a typo, so do it again and type accurately.')
        elif pls == comp:
            print ('Meh, do it again.')
        else:
            print ('You managed to win, you play as "X"')
            choice = 1
            return 1

def signer():
    choice = rock_paper_s()
    ai_s = ''
    player_s = ''
    if choice == 1:
        ai_s = 'O'
        player_s = 'X'
    elif choice == 0:
        ai_s = 'X'
        player_s = 'O'
    return ai_s, player_s

def do_move(board, move, sign):
    board[int(move)-1] = sign

def free_space(board, move):
    return board[int(move)-1]==' '

def player_turn(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not free_space(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)
        
def check_winner(bo, le):
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or
        (bo[3] == le and bo[4] == le and bo[5] == le) or
        (bo[0] == le and bo[1] == le and bo[2] == le) or
        (bo[6] == le and bo[3] == le and bo[0] == le) or
        (bo[7] == le and bo[4] == le and bo[1] == le) or
        (bo[8] == le and bo[5] == le and bo[2] == le) or
        (bo[6] == le and bo[4] == le and bo[2] == le) or
        (bo[8] == le and bo[4] == le and bo[0] == le))
       
def play_again():
    print('Do you want to play again? (yes to start a new game or any other input to stop)')
    return input().lower().startswith('y')

def random_move_list(board, moves):
    possible = []
    for move in moves:
        if free_space(board, move):
            possible.append(move)
    if len(possible) != 0:
        return ai.choice(possible)
    else:
        return None
    
def board_copy(board):
    copied = []
    for i in board:
        copied.append(i)
    return copied

def goes_first(ais, plays):
    if ai_sign == 'X':
        return 'ai'
    else:
        return 'player'
    
def ai_turn(board, ais, plays):
    for i in range(1, 10):
        copy = board_copy(board)
        if free_space(copy, i):
            do_move(copy, i, ais)
            if check_winner(copy, ais):
                return i
    for i in range(1, 10):
         copy = board_copy(board)
         if free_space(copy, i):
             do_move(copy, i, plays)
             if check_winner(copy, plays):
                 return i
    if free_space(board, 5):
        return 5
    
    ai_move = random_move_list(board, [1, 3, 7, 9])
    if ai_move != None:
        return ai_move

    return random_move_list(board, [2, 4, 6, 8])

def full_board(board):
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True

print('Preparus ur Anus!')
while True:
    Board = [' ']*9
    print ('Now we will get your letters through rock-paper-scissors!')
    ai_sign, player_sign = signer()
    print ('"X" goes first!')
    turn = goes_first(ai_sign, player_sign)
    playing = True
    while playing:
        if turn == 'player':
            show_board(Board)
            move = player_turn(Board)
            do_move(Board, move, player_sign)
            if check_winner(Board, player_sign):
                show_board(Board)
                print ('Congratulations! You win.')
                playing = False
            else:
                if full_board(Board):
                    show_board(Board)
                    print ('The Board is full. Game over.')
                    playing = False
            turn = 'ai'
        else:
            move = ai_turn(Board, ai_sign, player_sign)
            do_move(Board, int(move), ai_sign)
            if check_winner(Board, ai_sign):
                show_board(Board)
                print ('Ai has beaten you.')
                playing = False
            else:
                if full_board(Board):
                    show_board(Board)
                    print ('The Board is full. Game over.')
                    playing = False
                else:
                    turn = 'player'
    if not play_again():
        break
    
    

        
        
