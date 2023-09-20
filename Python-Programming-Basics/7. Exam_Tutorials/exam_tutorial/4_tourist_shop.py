budget = float(input())
name_product = input()
bought_products_counter = 0
total_price = 0
is_budget_enough = True
while name_product != "Stop":
    price_product = float(input())
    bought_products_counter += 1
    if bought_products_counter % 3 == 0:
        price_product *= 0.5
    total_price += price_product
    if total_price > budget:
        is_budget_enough = False
        break
    if price_product > budget:
        is_budget_enough = False
        break
    name_product = input()
difference = abs(total_price - budget)
if is_budget_enough:
    print(f"You bought {bought_products_counter} products for {total_price:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {difference:.2f} leva!")

