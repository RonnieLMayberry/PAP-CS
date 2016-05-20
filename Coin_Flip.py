'''
Created on October 16, 2014

@author: mayberryr
'''
# Coin Flip
# The computer flips a coin 100 times and tells you how many times the coin was heads/tails.
# Ronnie Mayberry
# Thursday, October 16, 2014
import random

headsCount = 0
tailsCount = 0
count = 0

while count < 100:
    coin = random.randrange(2)
    coin
    if coin == 0:
        headsCount += 1
    else:
        tailsCount += 1
    count += 1

print("The number of heads was ", headsCount)
print("The number of tails was ", tailsCount)

input("\n\nPress the enter key to exit.")
