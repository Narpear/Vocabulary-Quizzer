#Import tkinter library
from tkinter import *
from tkinter import ttk


#Create an instance of tkinter frame or window
start= Tk()


#Set the geometry of tkinter frame
start.geometry("750x250")
def startquiz():
    start.destroy()
    import McqTimerGui

#Create a label
Label(start, text= "Welcome to Vocabulary Quizzer! Click \"START\" to start your quiz.", font= ('Helvetica 17 bold')).pack(pady=30)
#Create a button to open a New Window
ttk.Button(start, text="START", command=startquiz).pack()
start.mainloop()
