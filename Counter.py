'''
Created on October 22, 2014

@author: mayberryr
'''
# Counter
# Demonstrates the range() function.
# Ronnie Mayberry
# Wednesday, October 22, 2014

print("Counting:")
for i in range(10):
    print(i, end= "")

print("\n\nCounting by fives:")
for i in range(0, 50, 5):
    print(i, end="")

print("\n\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end="")

a_string=input("\n\nPlease enter a phrase and I will turn it around: ")
for char in reversed(a_string):
    print(char, end="")

input("\n\nPress the enter key to exit.\n")
