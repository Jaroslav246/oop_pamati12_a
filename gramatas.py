nosaukums = input("Ievadiet grāmatas nosaukumu: ")
autors = input("Ievadiet autora vārdu: ")
gads = input("Ievadiet izdošanas gadu: ")
with open("gramatas.txt", "w", encoding="utf-8") as faila_objekts:
    faila_objekts.write(f"Nosaukums: {nosaukums}/n")
    faila_objekts.write(f"Autors: {autors}/n")
    faila_objekts.write(f"Gads: {gads}/n")
    