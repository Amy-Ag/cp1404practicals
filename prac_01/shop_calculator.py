total=0
item_number=int(input("Number of items: "))
for item in range(item_number):
    item_price = float(input("Price of item: "))
    total += item_price
if total > 100:
    total *= 0.9
print(f"Total price for {item_number} items is {total:.2f}")