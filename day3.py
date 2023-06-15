# Create a game called Treasure Island using control flow and logical operators to prompt the user and receive inputs. Nested if statements

def repeat():
    again = input("\nWould you like to play? Enter Y or N:\n>").lower()
    if again == "y":
        return again
    else:
        quit()
def level1():
    return input("\nWelcome to Treasure Island.\nYour mission is to find the tresaure.\nWill you travel left or right to search for it?\nType \"left\" or \"right\"\n> ").lower()

def level2():
    return input ("\nNice, you made it to the next level!\nYour map shows that you need to get to Treasure Island, you can wait to board a ship or swim across the sea, pick one\nType \"swim\" or \"wait\"\n> ").lower()

def level3():
    return input ("\nNow that you've made it to Treasure Island, you can dig or search the cave.\nType \"dig\" or \"cave\"\n> ").lower()

play = repeat()
while play == "y":
    if level1() == "left":
        if level2() == "wait":
            if level3() == "dig":
                print("\nYou found the treasure!! You Win!")
                repeat()
            else:
                print("\nYou went searching in the cave and got lost!")
                repeat()
        else:
            print("you ended up taking a swim and got eaten by a shark!")
            repeat()
    else:
        print("\nYou ended up getting lost and couldn't find the treasure!")
        repeat()
