'''
Created on Feb 23, 2015

@author: mayberryr
'''
# Alien Blaster
# Demonstrates object interaction.
# Ronnie Mayberry
# February 23, 2015

import time

def print_slow(str):
    for letter in str:
        print(letter, end="")
        time.sleep(.03)
        
class Player(object):
    """A player in a shooter game."""
    def blast(self, enemy):
        print_slow("The player blasts an enemy.\n")
        enemy.die()
        
class Alien(object):
    """An alien in a shooter game."""
    def die(self):
        print_slow("The alien gasps and say, 'Oh, this is it. This is the big one. \n" \
              "Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them...\n" \
              "Good-bye, cruel universe.")
        
# main
print_slow("\t\tDeath of an Alien.\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress the enter key to exit.")
