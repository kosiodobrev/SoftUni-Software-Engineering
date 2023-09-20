number_hrizantemi = int(input())
number_roses = int(input())
number_laleta = int(input())
season = input()
holiday = input()
price_hrizantemi = 0
price_roses = 0
price_laleta = 0
price_arange = 2
if season == "Spring" or season == "Summer":
    price_hrizantemi += 2
    price_roses += 4.10
    price_laleta += 2.50
elif season == "Autumn" or season == "Winter":
    price_hrizantemi += 3.75
    price_roses += 4.50
    price_laleta += 4.15
final_price_hrizantemi = number_hrizantemi * price_hrizantemi
final_price_roses = number_roses * price_roses
final_price_laleta = number_laleta * price_laleta
price_buket = final_price_hrizantemi + final_price_roses + final_price_laleta
if holiday == "Y":
    price_buket = price_buket + (price_buket * 0.15)
all_flowers = number_hrizantemi + number_roses + number_laleta
if number_laleta > 7 and season == "Spring":
    price_buket *= 0.95
if number_roses >= 10 and season == "Winter":
    price_buket *= 0.9
if all_flowers > 20:
    price_buket *= 0.80
final_price = price_buket + price_arange
print(f"{final_price:.2f}")