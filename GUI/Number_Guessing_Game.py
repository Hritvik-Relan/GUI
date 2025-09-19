import tkinter
import math
import tkinter.messagebox
import random

root=tkinter.Tk()
root.minsize(250, 260)
root.title("Guess the number game")

number=random.randint(1, 50)

def check_num():
    guess=text_guess.get()
    guess= int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("High", "Your guess is too high")
    elif guess < number:
        tkinter.messagebox.showinfo("Low", "Your guess is too low")
    elif guess == number:
        tkinter.messagebox.showinfo("Congratulations", "Your guess was correct")
        new_number()

def new_number():
    number = random.randint(1, 20)

def btn_confirm():
    myName=text_name.get()
    tkinter.messagebox.showinfo("name", "Well "+ myName + ",I am thinking of a number between 1 and 20")

text_guess=tkinter.Entry(root, width=10)
text_guess.place(x=90, y= 150)

label = tkinter.Label(root, text = "Welcome to our game")
label.pack()

label_name= tkinter.Label(root, text = "What is your name?")
label_name.place(x=10, y=60)

text_name=tkinter.Entry(root, width = 20)
text_name.place(x=10, y=90)

btnOK=tkinter.Button(root, text="Ok", command = btn_confirm)
btnOK.place(x=200, y=90, height = 28)

label_guess=tkinter.Label(root, text="Take a guess")
label_guess.place(x=10, y= 150)

btncheck=tkinter.Button(root, text="Guess", command=check_num)
btncheck.place(x=200, y=150, width=45, height= 28)

root.mainloop()