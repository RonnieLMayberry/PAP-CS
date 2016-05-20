'''
Created on October 16, 2014

@author: mayberryr
'''
#Guess My Number Improved
#Computer selects a random number, the user has 5 tries to guess the right one.
#Ronnie Mayberry
#Thursday, October 16, 2014

import random

print("Welcome to the new and improved 'Guess My Number' game.")
print("This time you have a limited number of guesses, so guess wisely.\n")

the_number = random.randrange(100) + 1

guess = int(input("Take a guess: "))
tries = 1

while guess != the_number:
    if tries > 5:
        print("Too bad. You tried one too many times.")
        print("The number was", the_number, ".")
        break
    elif guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")

    guess = int(input("Guess again:"))
    tries += 1

if tries < 6:
    print("You guessed it! The number was", the_number, ".")
    print("And it only took you", tries, "tries!\n")
