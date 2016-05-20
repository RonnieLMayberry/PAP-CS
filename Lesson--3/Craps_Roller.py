'''
Created on September 30, 2014

@author: mayberryr
'''
# Craps Roller
# Demonstrates random number generation.
# Ronnie Mayberry
# Tuesday, September 30, 2014

import random

# generate random numbers 1-6
die1 = random.randint(1,6)
die2 = random.randrange(6)+1

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)


input("\n\nPress the enter key to exit.")
