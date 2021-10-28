#week5
import requests
data=requests.get("http://api.open-notify.org/astros.json")
astros=data.json()
astros=astros["people"]
for person in astros:
    print(person['name'])
