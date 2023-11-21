# Exercise solution : creating a NEWS APP using news api.

import requests
import json

query = input("What type of news are you interesed in? :  ")

# news api
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-10-21&sortBy=publishedAt&apiKey=1abaeb389154469894ac5250894a62ce"

r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))

for articles in news["articles"]:
    print("Title : " , articles["title"])
    print("Description : ", articles["description"])
    print("---------------------------------")

