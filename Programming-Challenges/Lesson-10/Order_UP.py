'''
Created on Mar 30, 2015

@author: mayberryr
'''
# Order UP!
# GUI program representing a restaurant menu with the total bill.

from tkinter import *
import random

class Application(Frame):
    """ GUI application that creates a story based on user input. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """ Create widgets to display a menu and print the prices. """
        # create instruction label
        Label(self, text = "Enter your selection.").grid(row = 0,
                                                        column = 0,
                                                        columnspan = 2,
                                                        sticky = W)
        
        # create a label and text entry for the server
        Label(self, text = "Server's Name: ").grid(row = 1, column = 0, sticky = W)
        self.name_ent = Entry(self)
        self.name_ent.grid(row = 1, column = 1, sticky = W)
        
        # create a label for adjectives check buttons
        Label(self, text = "Food Choice(s):").grid(row = 4, column = 0, sticky = W)
        
        # create steak check button
        self.steak = BooleanVar()
        Checkbutton(self, text = "Steak - $15.00", variable = self.steak).grid(row = 4,
                                                                         column = 1,
                                                                         sticky = W)
        
        # create potato check button
        self.potato = BooleanVar()
        Checkbutton(self, text = "Mashed Potatoes - $2.50", variable = self.potato).grid(row = 4,
                                                                           column = 2,
                                                                           sticky = W)
        
        # create chicken check button
        self.chicken = BooleanVar()
        Checkbutton(self, text = "Chicken Stew - $10.00", variable = self.chicken).grid(row = 4,
                                                                           column = 3,
                                                                           sticky = W)
        
        # create mac check button
        self.mac = BooleanVar()
        Checkbutton(self, text = "Mac and Cheese - $5.00", variable = self.mac).grid(row = 4,
                                                                         column = 4,
                                                                         sticky = W)
            
        # create a submit button
        Button(self,
               text = "Click for receipt",
               command = self.receipt
               ).grid(row = 6, column = 0, sticky = W)
               
        self.receipt_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.receipt_txt.grid(row = 7, column = 0, columnspan = 4)
        
    def receipt(self):
        cost = 0
        """ Fill text box with receipt information based on input. """
        # get values from the GUI
        person = self.name_ent.get()
        adjectives = ""
        if self.steak.get():
            cost += 15.00
            adjectives += "- Steak -"
        if self.potato.get():
            cost += 2.50
            adjectives += "- Mashed Potatoes -"
        if self.chicken.get():
            cost += 10.00
            adjectives += "- Chicken Stew -"
        if self.mac.get():
            cost += 5.00
            adjectives += "- Mac and Cheese -"
        
        cost = str(cost)
        
        # create the receipt
        receipt = "Server's Name: "
        receipt += person
        receipt += "\nYou ordered: "
        receipt += adjectives
        receipt += "\nWhich means your total bill is: $"
        receipt += cost
        receipt += "\nThank you for coming!" 
        
        # display the receipt
        self.receipt_txt.delete(0.0, END)
        self.receipt_txt.insert(0.0, receipt)
        
# main
root = Tk()
root.title("Order UP!")
app = Application(root)
root.mainloop()
