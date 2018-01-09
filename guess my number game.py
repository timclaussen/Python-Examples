# Guess my number game, random number generation

import random

# Dice roller

# generate random numbers 1 - 6
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1

total = die1 + die2
print("I rolled a ", die1, "and a", die2, "making the total:", total)

print("Now it's time for you to guess! I'll roll again.\n")

die1 = random.randint(1,6)
die2 = random.randrange(6) + 1

total = die1 + die2
choice = "y"
while choice == "y":
    guess_num = int(float(input("Guess the total of the two dice roll: ")))

    if guess_num == total: # correct guess
        print("You guessed right! The total was ", total, "\n")
        choice = "n" # break while loop
    elif guess_num > total:
        print("You guessed higher than the total!")
        choice = input("Try again (same total)? [y/n]")
    else: # guess < total
        print("You guessed lower than the total!")
        choice = input("Try again (same total)? [y/n]")
