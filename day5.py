# Create a random password generator using upper case letters, lower case letters, numbers, and special characters

import random

password = []
cap_lets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
low_lets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spec_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "\\", "|", ":", ";", "\"", "\'"]

cap, lower, num, special = 0, 0, 0, 0

cap = input("\nWelcome to your random password generator\n\nEnter the amount of upper case letters that you will include in your password\n> ")
for i in range(int(cap)):
    password.extend(random.choice(cap_lets))

lower = input("Now enter the amount of lower case letters that you will include in your password\n> ")
for i in range(int(lower)):
    password.extend(random.choice(low_lets))

num = input("Now enter the amount of numbers that you will include in your password\n> ")
for i in range(int(num)):
    password.extend(random.choice(nums))

special = input("Now enter the amount of special characters that you will include in your password\n> ")
for i in range(int(special)):
    password.append(random.choice(spec_char))

random.shuffle(password)

print(f"Your completed password is:\n> {''.join(password)}")
