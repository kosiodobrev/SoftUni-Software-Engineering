budget = float(input())
n_nights = int(input())
price_per_night = float(input())
percent_costs = int(input())

costs = budget * percent_costs / 100
if n_nights > 7:
    price_per_night *= 0.95
nights_costs = n_nights * price_per_night
total_costs = costs + nights_costs
difference = abs(budget - total_costs)
if budget >= total_costs:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")



