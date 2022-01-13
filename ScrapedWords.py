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
