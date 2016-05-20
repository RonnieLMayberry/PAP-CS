'''
Created on Feb 5, 2015

@author: mayberryr
'''
# Constructor Program
# Demonstrates constructors
# Ronnie Mayberry
# February 5, 2015

class Critter(object):
    """A virtual pet"""
    def __init__(self):
        print("A new critter has been born!")
    
    def talk(self):
        print("Hi. I'm an instance of class Critter.")
        
# main
crit1 = Critter()
crit2 = Critter()
crit3 = Critter()
crit4 = Critter()
crit5 = Critter()
crit6 = Critter()

crit1.talk()
crit2.talk()
crit3.talk()
crit4.talk()
crit5.talk()
crit6.talk()

input("\n\nPress the enter key to exit.")