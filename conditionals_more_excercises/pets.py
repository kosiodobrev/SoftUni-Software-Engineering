from math import floor
from math import ceil
days = int(input())
left_food_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_gr = float(input())

needed_dog_food = dog_food_per_day_kg * days
needed_cat_food = cat_food_per_day_kg * days
needed_turtle_food = (turtle_food_per_day_gr * days) / 1000  #от гр в кг
total_food_sum = needed_dog_food + needed_cat_food + needed_turtle_food

difference = abs(left_food_kg - total_food_sum)

if total_food_sum <= left_food_kg:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")

