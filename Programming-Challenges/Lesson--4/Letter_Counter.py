'''
Created on October 29, 2014

@author: mayberryr
'''
# Letter Counter
# Allows the user to enter a message and the letter that they want to find in the message.
# Ronnie Mayberry
# Wednesday, October 29, 2014

message = input("Enter a message: ")
letter = input("Enter a letter: ")
print("\nThe length of your message is:", len(message))

count = message.count(letter)

if count > 0:
    print("The letter '", letter, "' appears in your message ", count, "times.")
elif count == 0:
    print("The letter '", letter, "' does not appear in your message.")

input("\n\nPress the enter key to exit.")