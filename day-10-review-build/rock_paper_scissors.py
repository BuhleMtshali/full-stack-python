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