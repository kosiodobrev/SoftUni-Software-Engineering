type_flower = input()
number_flower = int(input())
budget = int(input())
price_flower = 0
if type_flower == "Roses":
    price_flower = 5
    if number_flower > 80:
        price_flower *= 0.9
if type_flower == "Dahlias":
    price_flower = 3.80
    if number_flower > 90:
        price_flower *= 0.85
if type_flower == "Tulips":
    price_flower = 2.80
    if number_flower > 80:
        price_flower *= 0.85
if type_flower == "Narcissus":
    price_flower = 3
    if number_flower < 120:
        price_flower *= 1.15
if type_flower == "Gladiolus":
    price_flower = 2.50
    if number_flower < 80:
        price_flower *= 1.20
total_flower_price = price_flower * number_flower

difference = abs(total_flower_price - budget)

if budget >= total_flower_price:
    print(f"Hey, you have a great garden with {number_flower} {type_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
