from math import ceil
x_loze = int(input())
grozde_kv_m = float(input())
needed_wine = int(input())
number_workers = int(input())

harvest = x_loze * 0.4
grozde_kg = harvest * grozde_kv_m  #кг грозде
made_wine = ceil(grozde_kg / 2.5)

difference = ceil(abs(needed_wine - made_wine))
wine_for_workers = difference / number_workers

if made_wine < needed_wine:
    print(f"It will be a tough winter! More {difference} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {made_wine} liters.")
    print(f"{difference} liters left -> {ceil(wine_for_workers)} liters per person.")
