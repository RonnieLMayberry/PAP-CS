'''
Created on October 29, 2014

@author: mayberryr
'''
# Name Initial-er
# Allows the user to input their first, middle, and last names -
# and tells them their initials.
# Ronnie Mayberry
# Wednesday, October 29, 2014

name = input('Type your first, middle, and last name: ')
name_list = name.split()

for part in name_list:
    print(part[0].upper() + ". ", end="")
print()

input("\n\nPress the enter key to exit.")
