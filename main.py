## Dice Roller project I found online.

import random

def roll():
    print(random.randrange(1,6,1))
    print("\n")

print("\nWelcome to the Dice Roller!\n")

answer = True

roll()

while answer != False:

    resp = input("would you like to roll again?: ")

    if resp.lower()[0] == 'y':
        roll()
    elif resp.lower()[0] == 'n':
        answer = False
    else:
        print("\nSorry, I didn't understand that...")