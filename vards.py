name = input("Please enter your name:")
with open("vards.txt", "w") as file:
    file.write(name)