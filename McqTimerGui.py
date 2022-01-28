#import everything from tkinter
from tkinter import *
from tkinter import messagebox as mb


# data1.json serves as the source of data. To extract this, we import json file.
import json
import time 

# json is JavaScript Object Notation
from textwrap import wrap
import requests, random

import json

url =  'https://www.randomlists.com/data/vocabulary-words.json'
r = requests.get(url)

questions = []
answers = []
options=[]


for i in range (0,10):
    words_and_meanings =  random.choices(r.json()['data'], k=4)
    x = random.randint(1,4)
    questions.append(words_and_meanings[x-1]["name"])
    answers.append(x)
    temp_options = [words_and_meanings[0]["detail"], words_and_meanings[1]["detail"], words_and_meanings[2]["detail"], words_and_meanings[3]["detail"]]
    options.append(temp_options)

lists = ['question', 'answer', 'options']

data = {"question": questions, "answer": answers, "options": options }
with open('data1.json', 'w') as database:
    json.dump(data, database, indent=4)


#class to define the components of the GUI
class Quiz:
	def __init__(self):
		
		
		# setting question number to 0
		self.q_no=0
		
		# assigning question to the display_question function to be updated later.
		self.display_title()
		self.display_question()
		
		# opt_selected holds an integer value which is used for the selected option in a question.
		self.opt_selected=IntVar()
		
		# displaying radio button for the current question and used to display options for the current question
		self.opts=self.radio_buttons()
		
		# display options for the current question
		self.display_options()
		
		# displays the button for next and exit.
		self.buttons()
		
		# no of questions
		self.data_size=len(question)
		
		# keep a counter of correct answers
		self.correct=0
		

	# This fucntion counts correct and wrong answers and displays the result at the end in a messagebox.
	def display_result(self):
		
		# calculating percentage of wrong answers
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calculating percentage of correcr answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# displaying the result in a messagebox.
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	# Checking the chosen answer when "next" button is clicked.
	def check_ans(self, q_no):
		
		# checking if the selected option is correct
		if self.opt_selected.get() == answer[q_no]:
			# if the option is correct it return true
			return True

	# Checking the answer, increasing points, and displaying messagebox with the result.
	def next_btn(self):
		
		# Check if the answer is correct
		if self.check_ans(self.q_no):
			
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		
		# Moves to next Question by incrementing the q_no counter
		self.q_no += 1
		
		# checks if the q_no size is equal to the data size
		if self.q_no==self.data_size:
			
			# Displays the score
			self.display_result()
			
			# destroys the GUI
			gui.destroy()
		else:
			# shows the next question
			self.display_question()
			self.display_options()


	# Making the "next" and "quit" buttons
	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_button = Button(gui, text="Next",command=self.next_btn,
		width=10,bg="white",fg="black",font=("ariel",16,"bold"))
		
		# palcing the button on the screen
		next_button.place(x=350,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_button = Button(gui, text="Quit", command=gui.destroy,
		width=5,bg="white", fg="black",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
		quit_button.place(x=700,y=50)


	# Display and select the radio buttons
	def display_options(self):
		val=0
		
		# deselecting the options
		self.opt_selected.set(0)
		
		# looping the options list to display on the screen
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1


	# Displaying the current question on the screen
	def display_question(self):
		
		# setting the Question properties
		q_no = Label(gui, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		
		#placing the option on the screen
		q_no.place(x=70, y=100)


	# Displaying the title
	def display_title(self):
		
		# The title to be shown
		title = Label(gui, text="Vocabulary Quizzer",
		width=50, bg="pink",fg="white", font=("ariel", 20, "bold"))
		
		# place of the title
		title.place(x=0, y=2)


	# Making the radio buttons
	def radio_buttons(self):
		
		# initialize the list with an empty list of options
		q_list = []
		
		# position of the first option
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4:
			
			# setting the radio button properties
			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			
			# adding the button to the list
			q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40
		
		# return the radio buttons
		return q_list






# Creating a GUI Window
gui = Tk()

gui.title("Time Counter")
  
# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
hour.set("00")
minute.set("03")
second.set("00")
  
# Use of Entry class to take input from the user
hourEntry= Entry(gui, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.place(x=550,y=200)
  
minuteEntry= Entry(gui, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=583,y=200)
  
secondEntry= Entry(gui, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=613,y=200)
  
  
def submit():
    try:
        # user input is stored in temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # converting user input to hours, minutes and seconds.
        hours=0
        if mins >60:
             
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the temp value every time
        gui.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pops up with a message:"Time's up"
        if (temp == 0):
            mb.showinfo("Time Countdown", "Time's up ")
 
            gui.destroy()
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
 
# button widget
btn = Button(gui, text='Press to Start!', bd='5',
             command= submit)
btn.place(x = 540,y = 166)
  
# setting the size of the GUI Window
gui.geometry("800x450")

# setting the title of the GUI Window
gui.title("Vocabulary Quizzer")

# loading the data from the json file
with open('data1.json') as f:
	data = json.load(f)

# setting the questions, options, and answers
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

# an object of Quiz class is created
quiz = Quiz()

# Run the GUI
gui.mainloop()
