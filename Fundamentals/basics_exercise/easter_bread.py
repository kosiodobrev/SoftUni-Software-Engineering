budget = float(input())
flour_price = float(input())
pack_eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
bread_cost = pack_eggs_price + flour_price + (milk_price * 0.25)
bread_count = 0
eggs_count = 0

while budget > 0:
    if bread_cost > budget:
        break
    budget -= bread_cost
    bread_count += 1
    eggs_count += 3
    if bread_count % 3 == 0:
        eggs_count -= bread_count - 2
    if eggs_count <= 0:
        break

print(f"You made {bread_count} loaves of Easter bread! Now you have {eggs_count} eggs and {budget:.2f}BGN left.")
