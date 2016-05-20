'''
Created on Mar 30, 2015

@author: mayberryr
'''
# Guess My Number, GUI
# Recreation of the Guess My Number game using TKINTER GUI.

import random
from tkinter import *

class Application(Frame):
    """ GUI recreation of the GMN game. """
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """ Create widgets to play the game. """
        self.pw_lbl = Label(self, text = "Guess a number! (1-100):")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        
        self.submit_bttn = Button(self, text = "Submit!", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)
        
    def reveal(self):
        contents = self.pw_ent.get()
        guess = int(contents)
        if guess == the_number:
            message = "You got it right!"
        if guess > the_number:
            message = "Lower..."
        if guess < the_number:
            message = "Higher..."
        print(message)
        
# main
print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")
the_number = random.randint(1, 100)

root = Tk()
root.title('Guess My Number!')

app = Application(root)
app.mainloop()