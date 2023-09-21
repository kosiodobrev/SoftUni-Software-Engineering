juniors = int(input())
seniors = int(input())
type_race = input()
juniors_tax = 0
seniors_tax = 0
number_racers = juniors + seniors

if type_race == "trail":
    juniors_tax += 5.5
    seniors_tax += 7
elif type_race == "cross-country":
    juniors_tax += 8
    seniors_tax += 9.5
    if number_racers >= 50:
        juniors_tax *= 0.75
        seniors_tax *= 0.75
elif type_race == "downhill":
    juniors_tax += 12.25
    seniors_tax += 13.75
elif type_race == "road":
    juniors_tax += 20
    seniors_tax += 21.50

income = juniors * juniors_tax + seniors * seniors_tax
costs = income * 0.05
donation = income - costs
print(f"{donation:.2f}")
