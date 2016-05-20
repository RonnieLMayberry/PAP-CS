'''
Created on October 24, 2014

@author: mayberryr
'''
# Hero's Inventory
# Demonstrates tuple creation.
# Ronnie Mayberry
# Friday, October 24, 2014

inventory = ()

if not inventory:
    print("You are empty-handed.")

input("\nPress the enter key to continue.")

inventory = ("sword",
                    "armor",
                    "shield",
                    "healing potion")

print("\nThe tuple inventory is:")
print(inventory)

print("\nYour items:")
for item in inventory:
    print(item)

input("\n\nPress the enter key to exit.")
