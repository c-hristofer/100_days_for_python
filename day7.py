# Create a game of hangman

import random

def replay():
    again = input("\nWould you like to play a game of hangman?\nEnter Y to play again\n> ").lower()

    if again == "y":
        return "y"
    else:
        print("Thanks for playing!\n")
        exit()


def hangman(strikes):
    if strikes == 0:
        print("\n\n|---|\n|\n|\n|\n|______")
    elif strikes == 1:
        print("\n\n|---|\n|   O\n|\n|\n|______")
    elif strikes == 2:
        print("\n\n|---|\n|   O\n|   |\n|\n|______")
    elif strikes == 3:
        print("\n\n|---|\n|   O\n|   |/\n|\n|______")
    elif strikes == 4:
        print("\n\n|---|\n|   O\n|  \\|/\n|\n|______")
    elif strikes == 5:
        print("\n\n|---|\n|   O\n|  \\|/\n|  /\n|______")
    else:
        print("\n\n|---|\n|   O\n|  \\|/\n|  / \\\n|______\nYou Lose!")
        return 6
    return ""


# Set up variables
possible_words = ["languid", "shaky", "chilly", "complete", "error", "discover", "prevent", "flesh", "protect", "damage", "open", "house", "ahead", "shape", "wax", "oranges", "grass", "scream", "lighten", "tax", "sassy", "rain", "tin", "venomous", "baseball", "twig", "momentous", "tested", "nice", "electric", "teeth", "overconfident", "bee", "blood", "abusive", "relation", "command", "blushing", "pipe", "animated", "oval", "legal", "incompetent", "overwrought", "space", "thundering", "steel", "hallowed", "aboard", "leather"]
correct_guess = []
incorrect_guess = []
location = []

play = 'y'

# loop while player wants to play game
while play == 'y':
    correct_guess.clear()
    print("\nWelcome to Hangman")
    incorrect_guess.clear()

    # Start game by generating word to guess
    word = random.choice(possible_words)

    # Set up underscores
    for i in range(len(word)):
        correct_guess.append("_")

    # Start game loop to update variables and outputs each time
    while ''.join(correct_guess) != ''.join(word):

        # Display/update outputs
        print(f"Correct Guesses: {''.join(correct_guess)}")
        print(f"Incorrect Guesses: {''.join(incorrect_guess)}")

        # Get user's guess
        guess = input("Guess a letter\n> ")

        # If the guessed letter is in the word, loop to replace _ with that letter
        for i in range(len(word)):
            if guess in word[i]:
                location.append(i)

        if len(location) == 0:
            incorrect_guess.append(guess)
        else:
            for i in range(len(location)):
                correct_guess[location[i]] = guess
        location.clear()

        if ''.join(correct_guess) == ''.join(word):
            print("Congrats, you won!")
        elif hangman((len(incorrect_guess))) == 6:
            word = correct_guess
            
    play = replay()
