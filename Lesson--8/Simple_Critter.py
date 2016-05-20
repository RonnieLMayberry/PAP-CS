'''
Created on Feb 5, 2015

@author: mayberryr
'''
# Simple Critter
# Demonstrates a basic class and object.
# Ronnie Mayberry
# February 5, 2015

class Critter(object):
    """A virtual pet"""
    
    def talk(self):
        print("Hi. I'm an instance of class Critter.")
        
# main
crit = Critter()
crit.talk()

input("\n\nPress the enter key to exit.")