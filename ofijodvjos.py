import json

words = ["ābele", "priede", "bērzs", "ozols", "liepa"]

with open("words.json", "w", encoding="utf-8") as file:
    json.dump(words, file, indent=4)