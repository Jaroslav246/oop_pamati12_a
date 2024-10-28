with open("dati.txt", "r", encoding="utf-8") as file:
    rindas = file.readlines()

for index, rinda in enumerate(rindas, start=1):
    if rinda.strip():
       print(f"{index}: {rinda.strip()}")