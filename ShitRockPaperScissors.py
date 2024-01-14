
import random

choice = {
    1 : 'rock',
    2 : 'paper',
    3 : 'scissors',
}

PlayerPts = 0
CompPts = 0




print('----    WELCOME TO SHIT ROCK PAPER SCISSORS    ----')

rounds = int(input('How many rounds would you like to go? : '))

for i in range(rounds):
    CompGuess = choice.get(random.randint(1,3))
    RPS = input('rock, Paper, Scissors? : ')
    RPS = RPS.lower()
    if RPS == 'rock' and CompGuess == 'paper':
        print('Computer says paper')
        print('Computer wins!')
        CompPts = CompPts+1
    elif RPS == 'rock' and CompGuess == 'rock':
        print('Computer says rock')
        print('its a tie!')
        CompPts = CompPts+1 
        PlayerPts =  PlayerPts+1
    elif RPS == 'rock' and CompGuess == 'scissors':
        print('Computer says scissors')
        print('You win!')
        PlayerPts+=1
    elif RPS == 'paper' and CompGuess == 'rock':
        print('Computer says rock')
        print('You win!')
        PlayerPts+=1
    elif RPS == 'paper' and CompGuess == 'paper':
        print('Computer says paper')
        print('its a tie!')
        PlayerPts+=1
        CompPts+=1
    elif RPS == 'paper' and CompGuess == 'scissors':
        print('Computer says scissors')
        print('Computer wins!')
        CompPts+=1
    elif RPS == 'scissors' and CompGuess == 'rock':
        print('Computer says rock')
        print('Computer wins!')
        CompPts+=1
    elif RPS == 'scissors' and CompGuess == 'paper':
        print('Computer says paper')
        print('You win!')
        PlayerPts+=1
    elif RPS == 'scissors' and CompGuess == 'scissors':
        print('Computer says scissors')
        print('its a tie!')
        CompPts+=1
        PlayerPts+=1

print("you got " + str(PlayerPts))
print('Computer got ' + str(CompPts))
if PlayerPts > CompPts:
    print("You won!")
elif CompPts > PlayerPts:
    print('Computer won')
else:
    print("its a tie")


