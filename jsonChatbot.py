import json
import requests
import os
from pprint import pprint
url = "https://api.telegram.org/bot<urtoken>/getUpdates"
response  =  requests.get(url)
os.system("clear")
print(response)
print("============================")
print("json Data ")
pprint(response.json())


for msg in response.json()["result"]:
    msg["message"]["text"]
    with open('data.txt', 'a') as f:
            json.dump(msg["message"]["text"], f, ensure_ascii=False)




