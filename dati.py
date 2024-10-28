dati = ["Pirmais ieraksts", "Otrais ieraksts", "Trešais ieraksts"]
with open("dati.txt", "w", encoding="utf-8") as faila_objekts:
    for ieraksts in dati:
        faila_objekts.write(ieraksts + "/n")