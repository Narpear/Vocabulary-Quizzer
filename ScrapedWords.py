# json is JavaScript Object Notation
import requests, random

import json

url =  'https://www.randomlists.com/data/vocabulary-words.json'
r = requests.get(url)

questions = []
answers = []
options1 = []
options2 = []
options3 = []
options4 = []
options5 = []


words_and_meanings =  random.choices(r.json()['data'], k=5)

set1 = words_and_meanings[0]
set2 = words_and_meanings[1]
set3 = words_and_meanings[2]
set4 = words_and_meanings[3]
set5 = words_and_meanings[4]

word1 = set1["name"]

meaning1 = set1["detail"]
meaning2 = set2["detail"]
meaning3 = set3["detail"]
meaning4 = set4["detail"]
meaning5 = set5["detail"]


questions.append(word1)
answers.append(meaning1)
options1.append(meaning1)
options1.append(meaning2)
options1.append(meaning3)
options1.append(meaning4)
options1.append(meaning5)

words_and_meanings =  random.choices(r.json()['data'], k=5)

set1 = words_and_meanings[0]
set2 = words_and_meanings[1]
set3 = words_and_meanings[2]
set4 = words_and_meanings[3]
set5 = words_and_meanings[4]

word2 = set1["name"]

meaning1 = set1["detail"]
meaning2 = set2["detail"]
meaning3 = set3["detail"]
meaning4 = set4["detail"]
meaning5 = set5["detail"]


questions.append(word2)
answers.append(meaning1)
options2.append(meaning1)
options2.append(meaning2)
options2.append(meaning3)
options2.append(meaning4)
options2.append(meaning5)

words_and_meanings =  random.choices(r.json()['data'], k=5)

set1 = words_and_meanings[0]
set2 = words_and_meanings[1]
set3 = words_and_meanings[2]
set4 = words_and_meanings[3]
set5 = words_and_meanings[4]

word3 = set1["name"]

meaning1 = set1["detail"]
meaning2 = set2["detail"]
meaning3 = set3["detail"]
meaning4 = set4["detail"]
meaning5 = set5["detail"]


questions.append(word3)
answers.append(meaning1)
options3.append(meaning1)
options3.append(meaning2)
options3.append(meaning3)
options3.append(meaning4)
options3.append(meaning5)

words_and_meanings =  random.choices(r.json()['data'], k=5)

set1 = words_and_meanings[0]
set2 = words_and_meanings[1]
set3 = words_and_meanings[2]
set4 = words_and_meanings[3]
set5 = words_and_meanings[4]

word4 = set1["name"]

meaning1 = set1["detail"]
meaning2 = set2["detail"]
meaning3 = set3["detail"]
meaning4 = set4["detail"]
meaning5 = set5["detail"]


questions.append(word4)
answers.append(meaning1)
options4.append(meaning1)
options4.append(meaning2)
options4.append(meaning3)
options4.append(meaning4)
options4.append(meaning5)

words_and_meanings =  random.choices(r.json()['data'], k=5)

set1 = words_and_meanings[0]
set2 = words_and_meanings[1]
set3 = words_and_meanings[2]
set4 = words_and_meanings[3]
set5 = words_and_meanings[4]

word5 = set1["name"]

meaning1 = set1["detail"]
meaning2 = set2["detail"]
meaning3 = set3["detail"]
meaning4 = set4["detail"]
meaning5 = set5["detail"]


questions.append(word5)
answers.append(meaning1)
options5.append(meaning1)
options5.append(meaning2)
options5.append(meaning3)
options5.append(meaning4)
options5.append(meaning5)


#print(questions)
#print(answers)

options = [options1, options2, options3, options4, options5]

#print(options)
