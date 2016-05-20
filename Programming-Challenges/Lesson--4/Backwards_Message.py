'''
Created on October 28, 2014

@author: mayberryr
'''
# Backwards Message
# Allows the user to input a message, and then prints it backwards.
# Ronnie Mayberry
# Tuesday, October 28, 2014

string = input("\n\nEnter a phrase, and I will turn it around: ")
for char in reversed(string):
    print(char, end="")
