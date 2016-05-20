'''
Created on Feb 17, 2015

@author: mayberryr
'''
# Critter Caretaker
# A virtual pet to care for.
# Ronnie Mayberry
# February 17, 2015

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
        
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness <5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
        
    def eat(self, food = 4):
        amt = int(input("How much food would you like to give(1-4)? "))
        if amt <= 0:
            print("That's nothing! Try again.")
        elif amt > 5:
            print("That's too much! Try again.")
        elif amt == 1:
            print("Brruppp. Thank you.")
            self.hunger -= food
            
            if self.hunger < 0:
                self.hunger - 1
        elif amt == 2:
            print("Brruppp. Thank you.")
            self.hunger -= food
            
            if self.hunger < 0:
                self.hunger - 2
        elif amt == 3:
            print("Brruppp. Thank you.")
            self.hunger -= food
            
            if self.hunger < 0:
                self.hunger - 3
        elif amt == 4:
            print("Brruppp. Thank you.")
            self.hunger -= food
            
            if self.hunger < 0:
                self.hunger - 4
        elif amt == 5:
            print("Brruppp. Thank you.")
            self.hunger -= food
            
            if self.hunger < 0:
                self.hunger - 5
                
            self.__pass_time()
        
    def play(self, fun = 0):
        tm = int(input("How long would you like to play(1-4)? "))
        if tm < 0:
            print("That's no time! Try again.")
        elif tm > 5:
            print("That's too long! Try again.")
        elif tm == 1:
            print("Wheee!")
            fun += 1
            self.boredom -= fun
        
            if self.boredom < 0:
                self.boredom = 0
        elif tm == 2:
            print("Wheee!")
            fun += 2
            self.boredom -= fun
        
            if self.boredom < 0:
                self.boredom = 0
        elif tm == 3:
            print("Wheee!")
            fun += 3
            self.boredom -= fun
        
            if self.boredom < 0:
                self.boredom = 0
        elif tm == 4:
            print("Wheee!")
            fun += 4
            self.boredom -= fun
        
            if self.boredom < 0:
                self.boredom = 0
        elif tm == 5:
            print("Wheee!")
            fun += 5
            self.boredom -= fun
        
            if self.boredom < 0:
                self.boredom = 0
            
        self.__pass_time()
        
def main():
    crit_name = input("What do you want to name your critter: ")
    crit = Critter(crit_name)
    
    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker
        
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
        
        choice = input("Choice: ")
        print()
        
        # exit
        if choice == "0":
            print("Good-bye.")
            
        # listen to your critter
        elif choice == "1":
            crit.talk()
            
        # feed your critter
        elif choice == "2":
            crit.eat()
        
        # play with your critter
        elif choice == "3":
            crit.play()
            
        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")
            
main()
print("\n\nPress the enter key to exit")