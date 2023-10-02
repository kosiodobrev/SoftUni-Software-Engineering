collection_of_items = input().split("|")
budget = float(input())
budget_at_start = budget
clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.50
train_ticket = 150
profit = 0
sold_items_list = []
for item in collection_of_items:
    type_of_item, price_for_item = item.split("->")
    price_for_item_float = float(price_for_item)
    if type_of_item == "Clothes":
        if price_for_item_float <= 50 and budget >= price_for_item_float:
            budget -= price_for_item_float
            sold_item = price_for_item_float * 1.40
            rounded_sold_item_price = round(sold_item, 2)
            profit += rounded_sold_item_price
            sold_items_list.append(rounded_sold_item_price)
    elif type_of_item == "Shoes":
        if price_for_item_float <= 35 and budget >= price_for_item_float:
            budget -= price_for_item_float
            sold_item = price_for_item_float * 1.40
            rounded_sold_item_price = round(sold_item, 2)
            profit += rounded_sold_item_price
            sold_items_list.append(rounded_sold_item_price)
    elif type_of_item == "Accessories" and budget >= price_for_item_float:
        if price_for_item_float <= 20.50:
            budget -= price_for_item_float
            sold_item = price_for_item_float * 1.40
            rounded_sold_item_price = round(sold_item, 2)
            profit += rounded_sold_item_price
            sold_items_list.append(rounded_sold_item_price)
new_budget = budget + profit
profit_at_end = new_budget - budget_at_start
formatted_sold_items_list = [f"{price:.2f}" for price in sold_items_list]
print(*formatted_sold_items_list)
print(f"Profit: {profit_at_end:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
