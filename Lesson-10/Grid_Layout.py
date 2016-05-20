'''
Created on Mar 27, 2015

@author: mayberryr
'''
# Grid Layout
# Demonstrates a grid layout

from tkinter import *

class Application(Frame):
    """ A GUI application with nine buttons. """
    
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """ Create nine buttons that do nothing. """
        # create first button
        self.bttnl = Button(self, text = "row = 2\ncolumn = 0")
        self.bttnl.grid(row = 0, column = 0)
        
        # create second button
        self.bttn2 = Button(self, text = "row = 2\ncolumn = 0")
        self.bttn2.grid(row = 0, column = 1)
        
        # create third button
        self.bttn3 = Button(self, text = "row = 2\ncolumn = 0")
        self.bttn3.grid(row = 0, column = 2)

        # create fourth button
        self.bttn4 = Button(self, text = "row = 2\ncolumn = 0")
        self.bttn4.grid(row = 1, column = 0)
        
        # create fifth button
        self.bttn5 = Button(self, text = "row = 2\ncolumn = 0")
        self.bttn5.grid(row = 1, column = 1)
        
        # create sixth button
        self.bttn6 = Button(self, text = "row = 2\ncolumn = 0")
        self.bttn6.grid(row = 1, column = 2)

        # create seventh button
        self.bttn6 = Button(self, text = "row = 2\ncolumn = 0")
        self.bttn6.grid(row = 2, column = 0)

        # create eigth button
        self.bttn7 = Button(self, text = "row = 2\ncolumn = 0")
        self.bttn7.grid(row = 2, column = 1)

        # create ninth button
        self.bttnl = Button(self, text = "row = 2\ncolumn = 0")
        self.bttnl.grid(row = 2, column = 2)
    
# main
root = Tk()
root.title("Grid Layout")
app = Application(root)
root.mainloop()
