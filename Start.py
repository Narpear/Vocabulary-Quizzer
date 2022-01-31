#Import tkinter library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#Create an instance of tkinter frame or window
start= Tk()

load= Image.open(r"C:\Users\prerk\Python Projects\Computer Project SEM 1\quizpic.jpg")
render = ImageTk.PhotoImage(load)
img = Label(start, image=render)
img.place(x=230, y=70)

#Set the geometry of tkinter frame
start.geometry("750x400")

def startquiz():
    start.destroy()
    import McqTimerGui

#Create a label
Label(start, text= "Welcome to Vocabulary Quizzer!Click \"START\" to start your quiz.", font= ('Helvetica 17 bold'),fg='white',bg='black').pack()
#Create a button to open a New Window
ttk.Button(start, text="START", command=startquiz).place(x=330,y=350)

start.configure(bg='black')

start.mainloop()
