#FIRST WE GONNA IMPORT RANDOM, TIME & SYS
import random, time, sys

print('''Rock, Paper, Scissor

- Rock beats scissors.
- Paper beats 
- Scissors beats paper

''')

#variables to keep track of the number of wins, loses and ties
wins = 0
loses = 0
ties = 0


#STARTING A MAIN WHILE LOOP
while True:
    #INNER while loop thats keeps asking the player to enter R,P,S or Q
    while True:
        print('{} Wins, {} Losses, {} Ties'.format(wins, loses, ties))

        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input('> ').upper()

        if playerMove == 'Q':
            print('Thanks for playing!');
            sys.exit()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R, P, S or Q')

    #DISPLAYING WHAT THE PLAYER CHOOSES
    if playerMove == 'R':
        print('ROCK versus...')
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER versus...')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS versus...')
        playerMove = 'SCISSORS'

    # Count to three with dramatic pauses:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'ROCK'
    elif randomNumber == 2:
        computerMove = 'PAPER'
    elif randomNumber == 3:
        computerMove = 'SCISSORS'
    print(computerMove)
    time.sleep(0.5)