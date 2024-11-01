import json

with open("people.json", "r") as file:
    data = json.load(file)

print(data)