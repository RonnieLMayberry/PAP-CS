'''
Created on October 7, 2014

@author: mayberryr
'''
# Maitre D'
# Demonstrates treating a value as a condition.
# Ronnie Mayberry
# Tuesday, October 7, 2014

print("Welcome to the Chataeu D'Food")
print("It seems we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre D'? "))

if money:
    print("Ah, I am reminded of a table. Right this way.")
else:
    print("Please, sit. It may be a while.")

input("\n\nPress the enter key to exit.")
