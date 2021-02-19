from tkinter import *
from random import*
import tkinter as tk

class MathQuiz:
    def __init__(self, parent):
        self.frame1 = LabelFrame(parent)
        self.frame1.grid(row=0, column = 0)
        
        self.TitleLabel = Label (self.frame1, bg = "light blue", fg = "black", width = 20, padx = 30, pady = 10, text = "Welcome to Maths Mania", font= ("Times", "14", "bold"))
        self.TitleLabel.grid(columnspan = 5)
        
        self.button1 = Button(self.frame1, text = "     Addition     ", font =("bold", "10"), bg = "white", pady= 10, anchor = W)
        self.button1.grid(row = 8, column = 2)
        
        self.button2 = Button(self.frame1, text = "  Subtraction   ", font =("bold", "10"), bg = "white", pady= 10, anchor = W)
        self.button2.grid(row = 9, column = 2)
    
        self.button3 = Button(self.frame1, text = " Multiplication  ", font =("bold", "10"), bg = "white", pady= 10, anchor = W)
        self.button3.grid(row = 10, column = 2)    
        
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()
    