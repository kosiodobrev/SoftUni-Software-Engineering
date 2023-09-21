season = input()
km_per_month = float(input())
price_per_km = 0
season_months = 4
if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        price_per_km = 0.75
    elif 5000 < km_per_month <= 10000:
        price_per_km = 0.95
    elif 10000 < km_per_month <= 20000:
        price_per_km = 1.45
elif season == "Summer":
    if km_per_month <= 5000:
        price_per_km = 0.90
    elif 5000 < km_per_month <= 10000:
        price_per_km = 1.10
    elif 10000 < km_per_month <= 20000:
            price_per_km = 1.45
elif season == "Winter":
    if km_per_month <= 5000:
        price_per_km = 1.05
    elif 5000 < km_per_month <= 10000:
        price_per_km = 1.25
    elif 10000 < km_per_month <= 20000:
            price_per_km = 1.45

money = km_per_month * price_per_km * season_months
salary = money - (money * 0.1)
print(f"{salary:.2f}")