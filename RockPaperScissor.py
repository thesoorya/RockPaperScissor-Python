import random

while True:
    choices = ['rock', 'paper', 'scissors']

    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input('Rock, Paper, Scissors ? : ').lower()
    
    print('Player : ', player)
    print('Computer : ', computer)

    if player == computer:
        print('Tie')
    elif player == 'rock':
        if computer == 'paper':
            print('you lose')
        if computer == 'scissors':
            print('you win')
    elif player == 'paper':
        if computer == 'scissors':
            print('you lose')
        if computer == 'rock':
            print('you win')
    elif player == 'scissors':
        if computer == 'paper':
            print('you lose')
        if computer == 'rock':
            print('you win')
            
    play_again = input('want to play again? (yes/no) :')
    
    if play_again != 'yes':
        break;