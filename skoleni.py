import json

product = {
    "name": "Georgy",
    "priekšmets": "matematika",
    "vērtējums": 6,
}

with open("skoleni.json", "w") as file:
    json.dump(product, file, indent=4) 