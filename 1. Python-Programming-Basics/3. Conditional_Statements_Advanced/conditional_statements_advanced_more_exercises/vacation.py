budget = float(input())
season = input()
accommodation = ""
location = ""
price_location = 0
if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price_location = budget * 0.65
    if season == "Winter":
        location = "Morocco"
        price_location = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price_location = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price_location = budget * 0.60
elif budget > 3000:
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price_location = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price_location = budget * 0.90

print(f"{location} - {accommodation} - {price_location:.2f}")
