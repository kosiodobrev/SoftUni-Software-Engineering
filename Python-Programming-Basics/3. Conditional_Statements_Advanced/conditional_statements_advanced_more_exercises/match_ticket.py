budget = float(input())
category = input()
number_people = int(input())
transport_budget = 0
ticket_price = 0

if category == "VIP":
    ticket_price += 499.99
elif category == "Normal":
    ticket_price += 249.99

if 1 <= number_people <= 4:
    transport_budget = budget * 0.75
elif 5 <= number_people <= 9:
    transport_budget = budget * 0.60
elif 10 <= number_people <= 24:
    transport_budget = budget * 0.5
elif 25 <= number_people <= 49:
    transport_budget = budget * 0.4
elif number_people >= 50:
    transport_budget = budget * 0.25

costs = ticket_price * number_people + transport_budget
difference = abs(costs - budget)
if costs < budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")