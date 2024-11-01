import json

data = {
    "name": "Anna",
    "age": 25,
    "city": "Rīga"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4) 