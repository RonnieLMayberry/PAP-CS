'''
Created on October 22, 2014

@author: mayberryr
'''
# Dice Roll
# Rolls a dice randomly.
# Ronnie Mayberry
# October 22, 2014

import random

min=1
max=8

yes="y"
no="n"

dice1=random.randint(min,max)
dice2=random.randint(min,max)

user_input = input("Press Y to roll the Dice, N to exit ")

while user_input != no:
    if user_input == yes:
        dice1=random.randint(min,max)
        dice2=random.randint(min,max)
        print()
        print ("Dice have been rolled")
        print()
        print ("Your first Dice has a value of", dice1)
        print()
        print ("Your second Dice has a value of", dice2)
        print()
        print ("Value of both Dice = ", dice1 + dice2)
        print()
        user_input = input ("Roll the Dice again ? ")
    elif user_input == no:
        exit
