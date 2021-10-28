#week5 slicing info from API
import requests
data=requests.get("http://api.open-notify.org/astros.json").json()
astros=data["people"]
print(astros)
for whoever in astros:
    print(whoever['name'])