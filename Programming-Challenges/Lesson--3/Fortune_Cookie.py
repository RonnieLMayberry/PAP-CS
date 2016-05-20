'''
Created on October 10, 2014

@author: mayberryr
'''
# Fortune Cookie
# The computer picks a random fortune and displays it to the user.
# Ronnie Mayberry
# Friday, October 10, 2014

import random

print("\tWelcome to 'Fortune Cookie Simulator'!")
print("\nI can see your fortune...")
input("\nPress enter to see it.")

count = 0

while count < 5:
    
        fortune = random.randint(1,10)
    
        if fortune == 1:
            print("A dream you have will come true.")
        
        elif fortune == 2:
            print("Never give up. You're not a failure if you don't give up.")
        
        elif fortune == 3:
            print("You will become great if you believe in yourself.")
        
        elif fortune == 4:
            print("You already know the answer to the questions lingering inside your head.")
        
        elif fortune == 5:
            print("It is now, and in this world, that we must live.")
        
        elif fortune == 6:
            print("You must try, or hate yourself for not trying.")
        
        elif fortune == 7:
            print("You can make your own happiness.")
        
        elif fortune == 8:
            print("The greatest risk is not taking one.")
        
        elif fortune == 9:
            print("Our deeds determine us, as much as we determine our deeds.")
        
        elif fortune == 10:
            print("Meeting adversity well is the source of your strength.")
        count += 1

more = input("Would you like more fortunes?")

while input == "Yes":
            fortune = random.randint(1,10)

while input == "No":

        input("Press the enter key to exit.")
