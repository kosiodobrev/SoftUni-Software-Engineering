budget = float(input())
needed_liters_fuel = float(input())
day = input()
price_fuel = needed_liters_fuel * 2.10
tour_guide = 100
full_price = price_fuel + tour_guide
if day == "Saturday":
    full_price *= 0.90
elif day == "Sunday":
    full_price *= 0.80
difference = abs(budget - full_price)
if budget >= full_price:
    print(f"Safari time! Money left: {difference:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")