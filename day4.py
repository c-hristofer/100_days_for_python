# Create a game of rock, paper, scissors using a list and nested statements

import random
def randomize():
    return random.choice([0, 1, 2])

def repeat():
    if (input("\nWould you like to play Rock, Paper, Scissors?\nEnter Y or N:\n> ").lower() == "y"):
        return "y"
    else:
        exit()


play = "y"
while play == "y":
    computer = randomize()
    print(computer)
    user = float(input("\nEnter 0 for Rock, 1 for Paper, or 2 for Scissors:\n>"))

    if user == computer:
        print(f"\nYou both selected  {str(computer)}!\nLooks like it's a draw.")
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print(f"\nYou chose {str(user)[0]} and the computer chose {str(computer)}.\nYou won!")
    else:
        print(f"\nYou entered {str(user)[0]} and the computer chose {computer}!\nYou lose!")
    play = repeat()
