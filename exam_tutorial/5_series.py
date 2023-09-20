budget = float(input())
number_series = int(input())
total_price = 0
for _ in range(1, number_series + 1):
    name_series = input()
    price_series = float(input())
    if name_series == "Thrones":
        price_series *= 0.5
    elif name_series == "Lucifer":
        price_series *= 0.6
    elif name_series == "Protector":
        price_series *= 0.7
    elif name_series == "TotalDrama":
        price_series *= 0.8
    elif name_series == "Area":
        price_series *= 0.9
    total_price += price_series
difference = abs(total_price - budget)
if total_price <= budget:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")