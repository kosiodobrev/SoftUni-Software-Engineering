budget = float(input())
total_price = 0
name_of_product = input()
products_counter = 0
while True:

    if name_of_product == "Stop":
        print(f"You bought {products_counter} products for {total_price:.2f} leva.")
        break
    price_of_product = float(input())
    products_counter += 1
    if products_counter % 3 == 0:
        price_of_product = price_of_product * 0.5
    total_price += price_of_product
    if total_price > budget:
        print("You don't have enough money!")
        difference = abs(budget - total_price)
        print(f"You need {difference:.2f} leva!")
        break

    name_of_product = input()
