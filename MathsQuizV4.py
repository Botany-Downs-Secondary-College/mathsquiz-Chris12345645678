from tkinter import *
from random import*
import tkinter as tk
user_login = [["1", "2"],["Steven", "IsCool101"]]
user_details = [["Name", "Password", "Age", "Score"],["1", "2", 12, 7],["Steven", "IsCool101", 8, 10]]
current_user = []


class Login:
    def __init__(self, parent):      

        self.username_entry = StringVar()
        self.password_entry = StringVar()
        self.frame0 = LabelFrame(parent, height = 300)
        self.frame0.grid(row=0, column = 0)
        
        self.TitleLabel = Label(self.frame0, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "Sign In To Your Account", font= ("Times", "25", "bold"))#All the title attributes
        self.TitleLabel.grid(columnspan = 5)#Setting the column span for the page
        
        self.User = Label(self.frame0, text = "Username", padx = 20, font =("bold", "14"), pady= 10)#text that says usename above the entry box for the username to be entered
        self.User.grid(row = 1, column = 2)            #defining where it is positioned
        
        self.UserBox = Entry(self.frame0, width = 20, font =("12"), textvariable = self.username_entry)#Where the user puts in their username
        self.UserBox.grid(row = 2, column = 2) #defining where it is positioned
        
        self.Pass = Label(self.frame0, text = "Password", padx = 20, font =("bold", "14"), pady= 10)
        self.Pass.grid(row = 3, column = 2)                  #defining where it is positioned        
        
        self.PassBox = Entry(self.frame0, show = "*", width = 20, font =("12"),textvariable = self.password_entry) #The entry box for the password, which displays '*' so no one can see what is being typed.
        self.PassBox.grid(row = 4, column = 2)  #defining where it is positioned    
        
        self.Feedback = Label(self.frame0, text = "Username or password is incorrect")
        
        self.SignIn = Button(self.frame0, text = "Sign In", padx = 20, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.ShowMathsQuiz)   #Creating the sign in button, that sends it to the check pass function
        self.SignIn.grid(row = 6, column = 2)  #defining where it is positioned
        
        self.Create = Label(self.frame0, text = "If you don't already have an account", padx = 20, font =("bold", "11"), pady= 10)  #Lets the user know they can create an account if they dont have one already. - text
        self.Create.grid(row = 7, column = 2)    #defining where it is positioned           
                       
        self.CreateAccount = Button(self.frame0, text = "Create Account", font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.showCreateAccount)  #Button that takes them to a screen where they can craete a new account
        self.CreateAccount.grid(row = 8, column = 2)  #defining where it is positioned
        
        
        self.Create_Username = StringVar()
        self.Create_Age = IntVar()
        self.Create_Password = StringVar()
        self.Confirm_Password = StringVar()
        self.Create_Age.set("")
        self.frame1 = LabelFrame(root, height = 300)
        
        self.TitleLabel = Label(self.frame1, bg = "light grey", fg = "black", width = 27, padx = 30, pady = 10, text = "Create Your Account", font= ("Times", "25", "bold"))#All the title attributes
        self.TitleLabel.grid(columnspan = 5)#Setting the column span for the page
        
        self.User = Label(self.frame1, text = "Username", padx = 20, font =("bold", "14"), pady= 10)#text that says usename above the entry box for the username to be entered
        self.User.grid(row = 1, column = 2)            #defining where it is positioned
        
        self.CreateUserBox = Entry(self.frame1, width = 20, font =("12"), textvariable = self.Create_Username)#Where the user puts in their username
        self.CreateUserBox.grid(row = 2, column = 2) #defining where it is positioned
        
        self.Age = Label(self.frame1, text = "Age", padx = 20, font =("bold", "14"), pady= 10)#text that says usename above the entry box for the username to be entered
        self.Age.grid(row = 3, column = 2)        
        
        self.AgeBox = Entry(self.frame1, width = 20, font =("12"), textvariable = self.Create_Age)#Where the user puts in their username
        self.AgeBox.grid(row = 4, column = 2) #defining where it is positioned
        
        self.CreatePass = Label(self.frame1, text = "Password", padx = 20, font =("bold", "14"), pady= 10)
        self.CreatePass.grid(row = 5, column = 2)                  #defining where it is positioned        
    
        self.CreatePassBox = Entry(self.frame1, show = "*", width = 20, font =("12"), textvariable = self.Create_Password) #The entry box for the password, which displays '*' so no one can see what is being typed.
        self.CreatePassBox.grid(row = 6, column = 2)  #defining where it is positioned
        
        self.ConfirmPass = Label(self.frame1, text = "Confirm Password", padx = 20, font =("bold", "14"), pady= 10)
        self.ConfirmPass.grid(row = 7, column = 2)                  #defining where it is positioned        
    
        self.ConfirmPassBox = Entry(self.frame1, show = "*", width = 20, font =("12"), textvariable = self.Confirm_Password) #The entry box for the password, which displays '*' so no one can see what is being typed.
        self.ConfirmPassBox.grid(row = 8, column = 2)  #defining where it is positioned
        
        self.Feedback = Label(self.frame1, text = "")
        self.Feedback.grid(row = 9, column = 2)
        
        self.CreateAccountBttn = Button(self.frame1, text = "Create Account", padx = 20, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.Create_Account)   #Creating the sign in button, that sends it to the check pass function
        self.CreateAccountBttn.grid(row = 10, column = 2)  #defining where it is positioned
        
        self.AlreadyHaveAccount = Label(self.frame1, text = "Already have an account?", height = 2, font =("bold", "11"))
        self.AlreadyHaveAccount.grid(row = 11, column = 2)
        
        self.SignInBttn = Button(self.frame1, text = "Sign In", padx = 20, font =("bold", "11"), bg = "white", pady= 10, anchor = W, command = self.showSignIn)   #Creating the sign in button, that sends it to the check pass function
        self.SignInBttn.grid(row = 12, column = 2)  #defining where it is positioned
    
        
    def showCreateAccount(self):
        self.Create_Username.set("")
        self.Create_Age.set("")
        self.Create_Password.set("")
        self.Confirm_Password.set("")             
        self.frame1.grid(row=0, column = 0)
        self.frame0.grid_remove()#removes frame 2 (When user clicks create account and changes from sign in screen to the create account screen)
        
    def showSignIn(self):
        self.username_entry.set("")
        self.password_entry.set("")         
        self.frame0.grid(row = 0, column = 0)
        self.frame1.grid_remove()
        
    def Create_Account(self):    
        count = 0   
        while count < len(user_login):
            if self.Create_Username.get() == user_login[count][0]:
                print(self.Create_Username.get(), user_login[count][0])
                self.Feedback.configure(text = "Username already exists")
                break
            else:
                count +=1
            if count == len(user_login):
                if len(self.Create_Username.get()) < 5 or len(self.Create_Password.get()) < 5:    
                        self.Feedback.configure(text = "Username and password must be > 5 charcters long")
                else:
                    try:    
                        if self.Create_Age.get() >= 8 and self.Create_Age.get() <= 14:
                            if self.Create_Password.get() == self.Confirm_Password.get():
                                user_login.insert(0,[self.Create_Username.get(), self.Create_Password.get()]) 
                                current_user.insert(0, self.Create_Username.get(), self.Create_Password.get(), self.Create_Age.get())
                                self.frame1.grid_remove()
                                frames = MathQuiz(root)                                
                                break
                            else:
                                self.Feedback.configure(text = "Passwords dont match")
                        else:                
                            self.Feedback.configure(text = "Must be between 8 - 14")
                    except:
                        self.Feedback.configure(text = "Please pick a numerical age")
                 
        
    def ShowMathsQuiz(self):
        count = 0
        self.UsersEntry = [self.username_entry.get(), self.password_entry.get()]
        while count < len(user_login):
            if self.username_entry.get() in user_login[count][0]:
                if self.UsersEntry == user_login[count]:
                    self.frame0.grid_remove()
                    frames = MathQuiz(root)
                else:
                    self.Feedback.grid(row = 5, column = 2)
                break
            else:
                self.Feedback = Label(self.frame0, text = "Username or password is incorrect")
                self.Feedback.grid(row = 5, column = 2)                
                count+=1              
    

class MathQuiz:
    score = 0
    total = 0    
    def __init__(self, parent):
        self.frame1 = LabelFrame(parent, bg = "light blue", height = 300)
        self.frame1.grid(row=0, column = 0)
        
        self.TitleLabel = Label (self.frame1, bg = "light blue", fg = "black", width = 20, padx = 30, pady = 10, text = "Welcome to Maths Mania", font= ("Times", "14", "bold"))
        self.TitleLabel.grid(columnspan = 5)
        
        self.logout_btn = Button(self.frame1, text = "Logout", bg = "white", command = self.logout)
        self.logout_btn.grid(row = 1, column = 0)
        
        self.button1 = Button(self.frame1, text = "     Addition     ", font =("bold", "10"), bg = "white", pady= 10, anchor = W, command = self.Show_frame2)
        self.button1.grid(row = 8, column = 2)
        
        self.button2 = Button(self.frame1, text = "  Subtraction   ", font =("bold", "10"), bg = "white", pady= 10, anchor = W)
        self.button2.grid(row = 9, column = 2)
    
        self.button3 = Button(self.frame1, text = " Multiplication  ", font =("bold", "10"), bg = "white", pady= 10, anchor = W)
        self.button3.grid(row = 10, column = 2)    
        
        
        self.frame2 = LabelFrame(parent, bg = "light blue", height = 300)
        #self.frame2.grid(row=0, column = 0)
        
        self.score_display = Label(self.frame2, text = "score = 0", bg = "light blue")
        self.score_display.grid(row = 0, column = 2)
       
        self.problem_label = Label(self.frame2, text = "", width = 18, height = 3)
        self.problem_label.grid(row = 1, column = 0, sticky = W)
        
        self.answer_entry = Entry(self.frame2, width = 7, font = "10")
        self.answer_entry.grid(row = 1, column = 1, sticky = W)
        
        self.check_btn = Button(self.frame2, text = "Check Answer", bg = "white", relief = RIDGE, command = self.check_answer)
        self.check_btn.grid(row = 2, column = 1)        
        
        self.feedback = Label(self.frame2, text = "", height = 3, bg = "lightblue")
        self.feedback.grid(row = 3, column = 0)
        
        self.home_btn = Button(self.frame2, text = "Home", bg = "white", command = self.Show_frame1, relief = RIDGE)
        self.home_btn.grid(row = 2, column = 0)   
        self.next_problem()
        
        
        self.frame5 = LabelFrame(parent, height = "600", width = "300",  bg = "lightblue")
        #frame5.grid(row=0, column = 0)

                                
                                
        self.label = Label(self.frame5, text = "You answered {} question(s) correct out of 20".format(user_details[1][3]), padx = 10, fg = "black",bg = "lightblue")
        self. label.grid(row = 0, column = 0, columnspan = 3)
        
        count = 0
        while count < len(user_details):
            self.leaderboard_name = Label(self.frame5, text = user_details[count][0], width = 12, bg = "light blue")
            self.leaderboard_name.grid(row = count+1, column = 0)
            
            self.leaderboard_age = Label(self.frame5, text = user_details[count][2], width = 12, bg = "light blue")
            self.leaderboard_age.grid(row = count+1, column = 1)
            
            self.leaderboard_score = Label(self.frame5, text = user_details[count][3], width = 12, bg = "light blue")
            self.leaderboard_score.grid(row = count+1, column = 2) 
            count+=1
            
        self.home_btn = Button(self.frame5, text = "Home",font=20, bg = "white", command = self.Show_frame5, relief = RIDGE)
        self.home_btn.grid(row = count+2, column = 0)
    
        self.end_btn = Button(self.frame5, text = "End",font=20, bg = "white", relief = RIDGE)
        self.end_btn.grid(row = count+2, column = 2)        
    
    def logout(self):
        frames = Login(root) 
        self.frame1.grid_remove()
        
        
        
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
                self.score_display.configure(text = "score = {}".format(self.score))
                self.next_problem()
            else:
                self.feedback.configure(text = "Wrong!", fg = "red", bg = "lightblue") 
                self.answer_entry.delete(0, END)
                self.total = self.total + 1   
                self.score_display.configure(text = "score = {}".format(self.score))
                self.next_problem()
        except ValueError:
            self.feedback.configure(text = "That is not a number", fg = "black", bg = "lightblue")
            self.answer_entry.delete(0, END)
            self.answer_entry.focus()
        if self.total == 5:
            current_user.insert(2, self.score)
            print(current_user)
            user_details.insert(1, current_user)
            print(user_details)
            self.Show_frame5()
    
    def Show_frame1(self):
        self.frame2.grid_remove()
        self.frame1.grid(row = 0, column = 0)        
            
    def Show_frame2(self):
        self.frame1.grid_remove()
        self.frame2.grid(row = 0, column = 0)
      
        
    def Show_frame5(self):
        self.frame2.grid_remove()
        self.frame5.grid(row = 0, column = 0)  
        
if __name__ == "__main__":
        root = Tk()
        frames = Login(root)
        root.title("Quiz")
        root.mainloop()