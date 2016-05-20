'''
Created on Mar 25, 2015

@author: mayberryr
'''
# Click Counter
# Demonstrates binding an event with an event handler.

from tkinter import *

class Application(Frame):
    """ GUI application which counts button clicks. """
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()
        
    def create_widget(self):
        """ Create button which displays the number of clicks. """
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()
        
    def update_count(self):
        """ Increase click count and display new total. """
        self.bttn_clicks += 2 ** 10000000000000
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)
        
# main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()
