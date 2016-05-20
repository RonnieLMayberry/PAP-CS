'''
Created on October 27, 2014

@author: mayberryr
'''
# Message Analyzer - Edited
# Demonstrates the len() function and the in operator, as well as how many 'e's are in the message.
# Ronnie Mayberry
# Monday, October 27, 2014

message = input("Enter a message: ")

print("\nThe length of your message is:", len(message))

print("\nThe most common letter in the English language, 'e',")

numb = 0

if 'e' in message:

    print("is in your message.")

    for e in message:
    
        if e !='e' or e !='a' or e !='i' or e !='o' or e !='u':
        
            numb +=1

    print("\nThere are", numb, "consonants in your message.")

else:
    
    print("is not in your message.")
