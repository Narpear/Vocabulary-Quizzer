# Vocabulary-Quizzer
Web-scraping from https://www.randomlists.com/random-vocabulary-words

This is a program that creates an MCQ-Based test to test your vocabulary.

The program is written in 3 parts as of now:
* The scraping of words from a page with dynamic html.                            (ScrapedWords.py)
* The timer. (Straight from geeksforgeeks, I don't own this).                     (Timer.py)
* The GUI for the MCQ                                                             (McqGui.py)

There is also an additional json file that is used to store questions, answers and options 
The attached file here, data1.json is just a sample file. 
Every time ScrapedWords.py is run, the contents of data1.json changes. 

This project is still under progress. 
It will soon be integrated into a single program, or with reduced number of files. 
