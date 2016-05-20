'''
Created on Feb 18, 2015

@author: mayberryr
'''
# Television
# Simulates a television by creating it as an object.
# Ronnie Mayberry
# February 18, 2015

class TV(object):
    """A television"""
    def __init__(self, inp, channel = 0, volume = 0):
        self.channel = channel
        self.volume = volume
    
    @property
    def vol(self, volume = 0):
        volu = int(input("What volume would you like(1-5)? "))
        if volu > 5:
            print("That's not a valid volume. (1-5)")
            
        elif volu < 1:
            print("That's not a valid volume. (1-5)")
            
        elif volu == 1:
            print("Volume is at level 1.")
            volume = 1
            
        elif volu == 2:
            print("Volume is at level 1.")
            volume = 2
            
        elif volu == 3:
            print("Volume is at level 1.")
            volume = 3
            
        elif volu == 4:
            print("Volume is at level 1.")
            volume = 4
            
        elif volu == 5:
            print("Volume is at level 1.")
            volume = 5
    
    @property        
    def chann(self, channel = 0):
        chan = int(input("Which channel would you like to be on(1-5)? "))
        if chan > 5:
            print("That's not a valid channel. (1-5)")
            
        elif chan < 1:
            print("That's not a valid channel. (1-5)")
            
        elif chan == 1:
            print("Channel 1.")
            channel = 1
            
        elif chan == 2:
            print("Channel 2.")
            channel = 2
            
        elif chan == 3:
            print("Channel 3.")
            channel = 3
            
        elif chan == 4:
            print("Channel 4.")
            channel = 4
            
        elif chan == 5:
            print("Channel 5.")
            channel = 5

def main():
    tv_name = input("What is your name?: ")
    tv = TV(tv_name)
    
    choice = None
    while choice != "0":
        print \
        ("""
        Television Simulator
        
        0 - Quit
        1 - Change the volume.
        2 - Change the channel.
        """)
        
        choice = input("Choice: ")
        print()
        
        # exit
        if choice == "0":
            print("Good-bye.")
            
        # change the volume
        elif choice == "1":
            tv.vol()
            
        # change the channel
        elif choice == "2":
            tv.chann()
            
        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")
            
main()
print("\n\nPress the enter key to exit")