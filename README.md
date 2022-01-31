# Vocabulary-Quizzer

This is a program that creates an MCQ-Based test to test your vocabulary.
Words and meanings are scraped from Web-scraping from https://www.randomlists.com/random-vocabulary-words and put into an MCQ format with a timer.

There is also an additional json file that is used to store questions, answers and options.
The attached file here, data1.json is just a sample file. 
Every time McqTimerGui.py is run, the contents of data1.json changes. 

To run the code:

   * Step 1: Save all files (with same names and extensions)
   * Step 2: After saving quizpic.jpg, copy its path in line 8 of Start.py
   * Step 3: Run Start.py

Prerequisite modules:
  * random
  * requests
  * json
  * pillow
  * tkinter (but it's in-built)
