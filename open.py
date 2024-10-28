with open("vardi1.txt", "w", encoding="utf-8") as faila_objekts:
    while True:
        vards = input("Ievadiet vārdu (ievadiet 'beigt', lai pabeigtu): ")
        if vards.lower() == 'beigt':
            break
        faila_objekts.write(vards + "\n")

print("\nIevadītie vārdi:")
with open("vardi1.txt", "r", encoding="utf-8") as faila_objekts:
    for rinda in faila_objekts:
        print(rinda.strip())