import requests
import json
import random
print("This program uses Type.fit's API.")
randomIndex = random.randint(0, 1000)
response = requests.get("https://type.fit/api/quotes")
json_data = json.loads(response.text)
text = json_data[randomIndex]['text']
author = json_data[randomIndex]['author']
printString = str(text) + ' -' + str(author)
if author == None: 
    author = "Author not provided." 
    printString = str(text)
else: 
    pass
print(printString)
#It actually gets good quotes
