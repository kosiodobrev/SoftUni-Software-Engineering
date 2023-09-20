percent_fats = int(input())
percent_protein = int(input())
percent_carbohydrates = int(input())
full_calories = int(input())
percent_water = int(input())

calories_from_fats = full_calories * (percent_fats / 100) / 9
calories_from_protein = full_calories * (percent_protein / 100) / 4
calories_from_carbohydrates = full_calories * (percent_carbohydrates / 100) / 4

weight_food = calories_from_fats + calories_from_protein + calories_from_carbohydrates
calories_per_gram = full_calories / weight_food
without_water = calories_per_gram * (100 - percent_water) / 100

print(f"{without_water:.4f}")