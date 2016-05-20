'''
Created on Mar 27, 2015

@author: mayberryr
'''
# Mad Lib 2
# Customized Mad Lib

from tkinter import *

class Application(Frame):
    """ GUI application that creates a story based on user input. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # create instruction label
        Label(self, text = "Enter information for a new story").grid(row = 0,
                                                                     column = 0,
                                                                     columnspan = 2,
                                                                     sticky = W)
        
        # create a label and text entry for the name of a person
        Label(self, text = "Name: ").grid(row = 1, column = 0, sticky = W)
        self.name_ent = Entry(self)
        self.name_ent.grid(row = 1, column = 1, sticky = W)
        
        # create label and text entry for a type of fish
        Label(self, text = "Fish Type: ").grid(row = 2, column = 0, sticky = W)
        self.fish_ent = Entry(self)
        self.fish_ent.grid(row = 2, column = 1, sticky = W)
        
        # create a label and text entry for a verb
        Label(self, text = "Verb: ").grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)
        
        # create a label for adjectives check buttons
        Label(self, text = "Adjective(s):").grid(row = 4, column = 0, sticky = W)
        
        # create proud check button
        self.is_proud = BooleanVar()
        Checkbutton(self, text = "proud", variable = self.is_proud).grid(row = 4,
                                                                         column = 1,
                                                                         sticky = W)
        
        # create overwhelming check button
        self.is_overwhelming = BooleanVar()
        Checkbutton(self, text = "overwhelming", variable = self.is_overwhelming).grid(row = 4,
                                                                           column = 2,
                                                                           sticky = W)
        
        # create strong check button
        self.is_strong = BooleanVar()
        Checkbutton(self, text = "strong", variable = self.is_strong).grid(row = 4,
                                                                           column = 3,
                                                                           sticky = W)
        
        # create a label for body parts radio buttons
        Label(self, text = "Body Part:").grid(row = 5,
                                              column = 0,
                                              sticky = W)
        
        # create variable for single, body part
        self.body_part = StringVar()
        self.body_part.set(None)
        
        # create body part radio buttons
        body_parts = ["neck", "hair", "back"]
        column = 1
        for part in body_parts:
            Radiobutton(self, 
                        text = part, 
                        variable = self.body_part, 
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1
            
        # create a submit button
        Button(self,
               text = "Click for story",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)
               
        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)
        
    def tell_story(self):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        person = self.name_ent.get()
        noun = self.fish_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_proud.get():
            adjectives += "proud, "
        if self.is_overwhelming.get():
            adjectives += "overwhelming, "
        if self.is_strong.get():
            adjectives += "strong, "
        body_part = self.body_part.get()
        
        # create the story
        story = "One beautiful day in Galveston, "
        story += person
        story += " decided to go fishing for some "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person + ". "
        story += "A peculiar, "
        story += adjectives
        story += "happy feeling overwhelmed the fisherman. "
        story += "He had finally caught the "
        story += noun.title()
        story += "! Beads of sweat started pouring down from "
        story += person + "'s "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person + ". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += "."
        
        # display the story
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)
        
# main
root = Tk()
root.title("Mad Lib 2.0")
app = Application(root)
root.mainloop()