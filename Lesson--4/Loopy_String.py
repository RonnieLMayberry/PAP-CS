'''
Created on October 22, 2014

@author: mayberryr
'''
# Loopy String
# Demonstrates the for loop with a string.
# Ronnie Mayberry
# Wednesday, October 22, 2014

word = input("Enter a word: ")

print("\nHere's each letter in your word: ")
for letter in word:
    print(letter, end = "")

input("\n\nPress the enter key to exit.")
