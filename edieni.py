edieni = ["Pica", "Sushi", "Burger"]
with open("edieni.txt", "w", encoding="utf-8") as faila_objekts:
    for ediens in edieni:
        faila_objekts.write(ediens + "/n")