import json

with open("product.json", "r") as file:
    product = json.load(file)

total_price = 0
for product in product:
    total_price+=product["price"]
    average_price = total_price / len(product)
print(f"Vidēja cena: {average_price:.2f} EUR")