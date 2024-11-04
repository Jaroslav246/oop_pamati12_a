import json

try:
    with open("people_data.json", "r", encoding="utf-8") as file:
        people = json.load(file)
except FileNotFoundError:
    people = []

while True:
    name = input("Ievadi vārdu: ")
    age = input("Ievadi vecumu: ")
    city = input("Ievadi pilsētu: ")

    people.append = ({
        "name": name,
        "age": age,
        "city": city
    })

    another = input("Vai vēlies pievienot vēl vienu cilvēku? (jā/nē): ").strip().lower()
    if another != "jā":
        break

with open("people_data.json", "w", encoding="utf-8") as file:
    json.dump(people, file, indent=4)

print("Dati par cilvēkiem ir veiksmīgi saglabāti JSON failā!") 