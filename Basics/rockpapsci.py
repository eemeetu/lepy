import random
print ('to stop anytime enter: ass')
score = 0
games = 0
while True:
# Here starts code to take input from user
    games += 1
    player = input('Choose and enter - Rock, Paper or Scissors: ')
    if player == 'ass':
        print ('Game over, see you later!')
        break
    if player == 'Rock':
        pls = 0
    elif player == 'Paper':
        pls = 1
    elif player == 'Scissors':
        pls = 2
    # Next 2 lines are to avoid bugs with invalid input
    else:
        pls = 5
    # Here starts computations, some parts of code could be simpler, so it is beta for now
    comp = random.randint(0, 2)
    if comp == 0:
        print ('Computer decided to throw ROCK!!!')
    elif comp == 1:
        print ('Computer decided to throw PAPER!!!')
    elif comp == 2:
        print ('Computer gonna cut ya with SCISSORS!!!')
    if (comp == 1 and pls == 0) or (comp == 0 and pls == 2) or (comp == 2 and pls == 1):
        print ('You lost to AI this time, your score is: ', score, 'out of', games, 'games.')
    # I felt too lazy to distinguish typos and comletely invalid input :)
    elif pls == 5:
        print ('But you have a typo, so do it again and type accurately.')
        games -=1
    elif pls == comp:
        print ('Meh, do it again, your score is: ', score, 'out of', games, 'games.')
    else:
        score += 1
        print ('You managed to win, your score is: ', score, 'out of', games, 'games.')
   
