import os
import random
import re

os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
    print("\n")
    print("If you don't know the rules, input 'Rules'")    
    
    # ask for input from user
    userChoice = input("Choose your weapon: [R]ock, [P]aper, [S]cissors, [L]izard, Spoc[K]: ")
    
    #check for match expressions input from user, with "re.match"
    if not re.match("[SsRrPpLlKk]", userChoice):
        print("Please, chose a letter: ")
        print("[R]ock, [S]cissors, [P]aper, [L]izard, Spoc[K]")
        continue 

    if re.match("[Rules, rules]", userChoice):
        print("Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.")
        break 

    #Echo the users choice, just to check if is correct
    print("You chose " + userChoice)

    #provide the program with the possible choices
    choices = ['R', 'P', 'S', 'L', 'K']

    #generate a random choice for the program and print it 
    programChoice = random.choice(choices)
    print("I chose: " + programChoice)

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
    break
