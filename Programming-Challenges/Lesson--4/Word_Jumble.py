'''
Created on October 29, 2014

@author: mayberryr
'''
# Word Jumble - Improved
# Improves on the Word Jumble game so that each word is paired with a hint,
# which can be requested by the player if they get stuck, although -
# the game will reward the player if they solve the jumble without using hints.
# Ronnie Mayberry
# Wednesday, October 29, 2014

import random

# Creates a sequence of words to choose from.
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# Picks one word randomly from the sequence.
word = random.choice(WORDS)

# Creates a variable to use later to see if the guess is correct.
correct = word

# Creates a jumbled version of the word.
jumble = ""

# Creates a variable for the hint/reward system.
count = 0

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# Starts the game.
print(
    """
                    Welcome to the Word Jumble!

             Unscramble the letters to make a word.
           (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")

    yn = input("Would you like to see a hint? Y/N ")
    if yn == "Y" and correct == "python":
        print("The program this game is written in.")
        count += 1
    elif yn == "Y" and correct == "jumble":
        print("What is being done to these words.")
        count += 1
    elif yn == "Y" and correct == "easy":
        print("The opposite of difficult.")
        count += 1
    elif yn == "Y" and correct == "difficult":
        print("The opposite of easy.")
        count += 1
    elif yn == "Y" and correct == "answer":
        print("A synonym for 'correct choice'")
        count += 1
    elif yn == "Y" and correct == "xylophone":
        print("An instrument beginning with the letter x.")
        count += 1
    elif yn == "N":
        continue

if guess == correct:
    print("That's it! You guessed it!\n")
    if count == 0:
        print("And you did it without any hints! Awesome!")
    else:
        print('Great job using those hints!')

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
