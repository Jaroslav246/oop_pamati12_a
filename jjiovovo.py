def coke_machine():
  cost = 50
  accepted_coins = [25, 10, 5]
  amount_due = cost

while "amount_due" > 0:
 print(f"Amount Due: {"amount_due"} cents")
 coin = int(input("Insert Coin: "))

if coin in ("accepted_coins"):
  amount_due = coin

if amount_due < 0:
 print(f"Change Owed: {"amount_due"} cents")
else:
 print("Change Owed: 0 cents")
if __name__ == "__main__":
 coke_machine()