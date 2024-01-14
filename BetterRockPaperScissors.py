import random

while True:

    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)

    player = ''

    while player not in choices:
        player = input('rock, paper, scissors? : ').lower()
        
        if player == computer:
            print('computer: ', computer)
            print('You: ', player)
            print("its a tie")
        elif player == 'rock':
            if computer == 'paper':
                print('computer: ', computer)
                print('You: ', player)
                print("You lost!")
            if computer == 'scissors':
                print('computer: ', computer)
                print('You: ', player)
                print("You won")

        elif player == 'paper':
            if computer == 'rock':
                print('computer : ', computer)
                print('You: ', player)
                print("You won!")
            if computer == 'scissors':
                print('computer: ', computer)
                print('You: ', player)
                print("You lost")
        
        elif player == 'scissors':
            if computer == 'rock':
                print('computer: ', computer)
                print('You: ', player)
                print("You lost!")
            if computer == 'paper':
                print('computer: ', computer)
                print('You: ', player)
                print("You won")

    PlayAgain = input('would you like to play again? yes or no: ').lower()
    if PlayAgain != 'yes':
        break


