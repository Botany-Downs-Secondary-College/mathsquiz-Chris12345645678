from tkinter import *
from random import*
import tkinter as tk

class MathQuiz:
    score = 0
    total = 0    
    def __init__(self, parent):
        self.frame0 = LabelFrame(parent, height = 300)
        self.frame0.grid(row=0, column = 0)
        
        self.TitleLabel = Label(self.frame0, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "Sign In To Your Account", font= ("Times", "25", "bold"))#All the title attributes
        self.TitleLabel.grid(columnspan = 5)#Setting the column span for the page
        
        self.User = Label(self.frame0, text = "Username", padx = 20, font =("bold", "14"), pady= 10)#text that says usename above the entry box for the username to be entered
        self.User.grid(row = 1, column = 2)            #defining where it is positioned
        
        self.UserBox = Entry(self.frame0, width = 20, font =("12"))#Where the user puts in their username
        self.UserBox.grid(row = 2, column = 2) #defining where it is positioned
        
        self.Pass = Label(self.frame0, text = "Password", padx = 20, font =("bold", "14"), pady= 10)
        self.Pass.grid(row = 3, column = 2)                  #defining where it is positioned        
        
        self.PassBox = Entry(self.frame0, show = "*", width = 20, font =("12")) #The entry box for the password, which displays '*' so no one can see what is being typed.
        self.PassBox.grid(row = 4, column = 2)  #defining where it is positioned    
        
        self.SignIn = Button(self.frame0, text = "Sign In", padx = 20, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.Show_frame1)   #Creating the sign in button, that sends it to the check pass function
        self.SignIn.grid(row = 6, column = 2)  #defining where it is positioned
        
        self.Create = Label(self.frame0, text = "If you don't already have an account", padx = 20, font =("bold", "11"), pady= 10)  #Lets the user know they can create an account if they dont have one already. - text
        self.Create.grid(row = 7, column = 2)    #defining where it is positioned           
                       
        self.CreateAccount = Button(self.frame0, text = "Create Account", font =("bold", "11"), bg = "white", pady= 10, anchor = W)  #Button that takes them to a screen where they can craete a new account
        self.CreateAccount.grid(row = 8, column = 2)  #defining where it is positioned
        
        
        
        
        
        self.frame1 = LabelFrame(parent, bg = "light blue", height = 300)
       # self.frame1.grid(row=0, column = 0)
        
        self.TitleLabel = Label (self.frame1, bg = "light blue", fg = "black", width = 20, padx = 30, pady = 10, text = "Welcome to Maths Mania", font= ("Times", "14", "bold"))
        self.TitleLabel.grid(columnspan = 5)
        
        self.button1 = Button(self.frame1, text = "     Addition     ", font =("bold", "10"), bg = "white", pady= 10, anchor = W, command = self.Show_frame2)
        self.button1.grid(row = 8, column = 2)
        
        self.button2 = Button(self.frame1, text = "  Subtraction   ", font =("bold", "10"), bg = "white", pady= 10, anchor = W)
        self.button2.grid(row = 9, column = 2)
    
        self.button3 = Button(self.frame1, text = " Multiplication  ", font =("bold", "10"), bg = "white", pady= 10, anchor = W)
        self.button3.grid(row = 10, column = 2)    
        
        
        self.frame2 = LabelFrame(parent, bg = "light blue", height = 300)
        #self.frame2.grid(row=0, column = 0)
        
        self.problem_label = Label(self.frame2, text = "", width = 18, height = 3)
        self.problem_label.grid(row = 0, column = 0, sticky = W)
        
        self.answer_entry = Entry(self.frame2, width = 7, font = "10")
        self.answer_entry.grid(row = 0, column = 1, sticky = W)
        
        self.check_btn = Button(self.frame2, text = "Check Answer", bg = "white", relief = RIDGE, command = self.check_answer)
        self.check_btn.grid(row = 1, column = 1)        
        
        self.feedback = Label(self.frame2, text = "", height = 3, bg = "lightblue")
        self.feedback.grid(row = 2, column = 0)
        
        self.home_btn = Button(self.frame2, text = "Home", bg = "white", command = self.Show_frame1, relief = RIDGE)
        self.home_btn.grid(row = 1, column = 0)   
        self.next_problem()
        
        
        self.frame5 = LabelFrame(parent, height = "600", width = "300",  bg = "lightblue")
        #frame5.grid(row=0, column = 0)
    
        self.label = Label(self.frame5, text = "You answered {} question(s) correct out of 20".format(self.score),font = 20, padx = 10, fg = "black",bg = "lightblue", width = 35, height = 9)
        self. label.grid(row = 0, column = 0, sticky = W)
    
        self.home_btn = Button(self.frame5, text = "Home",font=20, bg = "white", command = self.Show_frame5, relief = RIDGE)
        self.home_btn.grid(row = 1, column = 0)
    
        self.end_btn = Button(self.frame5, text = "End",font=20, bg = "white", relief = RIDGE)
        self.end_btn.grid(row = 2, column = 0)        
        
    def next_problem(self):
            x = randrange(10)
            y = randrange(10)
            problem_text = str(x) + " + " +str(y) + " ="
            self.problem_label.configure(text = problem_text, bg = "lightblue", font = "10")
            self.answer_entry.focus()  
            self.answer = x + y  
   
    def check_answer(self): 
        try:
            self.user_answer = int(self.answer_entry.get())
            if self.user_answer == self.answer:
                self.feedback.configure(text = "Correct!", fg = "green", bg = "lightblue")
                self.answer_entry.delete(0, END)
                self.score = self.score + 1
                self.total = self.total + 1            
                self.next_problem()
            else:
                self.feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue") 
                self.answer_entry.delete(0, END)
                self.total = self.total + 1            
                self.next_problem()
        except ValueError:
            self.feedback.configure(text = "That is not a number", fg = "black", bg = "lightblue")
            self.answer_entry.delete(0, END)
            self.answer_entry.focus()
        if self.total == 20:
            self.Show_frame5()
            
    def Show_frame2(self):
        self.frame1.grid_remove()
        self.frame2.grid(row = 0, column = 0)
      
    def Show_frame1(self):
        self.frame2.grid_remove()
        self.frame0.grid_remove()
        self.frame1.grid(row = 0, column = 0)
        total = 0
        
    def Show_frame5(self):
        self.frame2.grid_remove()
        self.frame5.grid(row = 0, column = 0)  
        
if __name__ == "__main__":
        root = Tk()
        frames = MathQuiz(root)
        root.title("Quiz")
        root.mainloop()
        
        
