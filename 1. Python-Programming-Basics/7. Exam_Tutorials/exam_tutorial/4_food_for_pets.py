number_days = int(input())
food_quantity = float(input())
food_eaten_by_dog_counter = 0
food_eaten_by_cat_counter = 0
bisquits_total = 0
for days in range(1, number_days + 1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())
    food_eaten_by_dog_counter += food_eaten_by_dog
    food_eaten_by_cat_counter += food_eaten_by_cat
    if days % 3 == 0:
        bisquits = (food_eaten_by_dog + food_eaten_by_cat) * 0.1
        bisquits_total += bisquits
total_eaten_food = food_eaten_by_dog_counter + food_eaten_by_cat_counter
percent_food_eaten = total_eaten_food / food_quantity * 100
percent_eaten_by_dog = food_eaten_by_dog_counter / total_eaten_food * 100
percent_eaten_by_cat = food_eaten_by_cat_counter / total_eaten_food * 100
print(f"Total eaten biscuits: {round(bisquits_total)}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_eaten_by_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_by_cat:.2f}% eaten from the cat.")
