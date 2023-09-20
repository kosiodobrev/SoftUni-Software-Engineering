budget = float(input())
season = input()
destination = ""
kind_of_vacation = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        kind_of_vacation = "Camp"
        spent_sum = budget * 0.30
    if season == "winter":
        kind_of_vacation = "Hotel"
        spent_sum = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        kind_of_vacation = "Camp"
        spent_sum = budget * 0.40
    if season == "winter":
        kind_of_vacation = "Hotel"
        spent_sum = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    kind_of_vacation = "Hotel"
    spent_sum = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{kind_of_vacation} - {spent_sum:.2f}")
