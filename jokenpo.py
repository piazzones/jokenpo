import os
import random
import re
from time import sleep
from emoji import emojize

os.system('cls' if os.name=='nt' else 'clear')

play = 'Y'

while play == 'Y':

    #initialize the program with some color and rules 
    print(emojize('''\033[31m------JOKENPÔ------\033[m
Chose Your Yeapon:
[ R ] Rock 👊
[ P ] Paper 🖐️
[ S ] Scissors ✌️
[ L ] Lizard 🦎
[ K ] Spock 🖖''', use_aliases=True))
    print("Rules: ")
    print("Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.")

    # ask for input from user
    userChoice = input("Your choice: ")

    #check for match expressions input from user area correct, with "re.match"
    if not re.match("[SsRrPpLlKk]", userChoice):
        print("Please, chose a letter: ")
        print("[R]ock, [S]cissors, [P]aper, [L]izard, Spoc[K]")
        continue 

    # JO...KEN...PO... timer. Just for show off.
    print('\033[31mJO\033[m')
    sleep(.3)
    print('\033[31mKEN\033[m')
    sleep(.3)
    print('\033[31mPÔ!\033[m\n')
    
    #provide the program with the possible choices
    choices = ['R', 'P', 'S', 'L', 'K']

    #generate a random choice for the program and print it 
    programChoice = random.choice(choices)

    #print both results to compare    
    print("You chose: " + userChoice)
    print(f"I chose: {programChoice}\n")

    #results
    if programChoice == str.upper(userChoice):
        print("Tie!")
    elif programChoice == 'S' and userChoice.upper() == 'P': 
        print("Scissors cuts paper, I win!")
    elif programChoice == 'P' and userChoice.upper() == 'R':
        print("Paper cover rock, I win!") 
        continue
    elif programChoice == 'R' and userChoice.upper() == 'L':
        print("Rock crushes lizard, I win!")
        continue
    elif programChoice == 'L' and userChoice.upper() == 'K':
        print("Lizard poisons Spock, I win!")
        continue
    elif programChoice == 'K' and userChoice.upper() == 'S':
        print("Spock smashes scissors, I win!")
        continue
    elif programChoice == 'S' and userChoice.upper() == 'L':
        print("Scissors decapitates Lizard, I win!")
        continue
    elif programChoice == 'L' and userChoice.upper() == 'P':
        print("Lizard eats Paper, I win!")
        continue
    elif programChoice == 'P' and userChoice.upper() == 'K':
        print("Paper disproves Spock, I win!")
        continue
    elif programChoice == 'R' and userChoice.upper() == 'S': 
        print("Rock crushes scissors, I win!") 
        continue     
    else:
        print("You win!")
        play_again = str(input('\nDo you want to play Again?' '[Y/N] ')).upper().strip()
        if play_again == 'N':
            break
    
