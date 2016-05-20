'''
Created on October 24, 2014

@author: mayberryr
'''
# Random Access
# Demonstrates string indexing.
# Ronnie Mayberry
# Friday, October 24, 2014

import random
word = "index"
print("The word is: ", word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

input("\n\nPress the enter key to exit.")
