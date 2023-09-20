drink = input()
sugar_yes_no = input()
n_drinks = int(input())

money = 0

if drink == "Espresso":
    if sugar_yes_no == "Without":
        money += 0.90 * 0.65
    elif sugar_yes_no == "Normal":
        money += 1
    elif sugar_yes_no == "Extra":
        money += 1.20
    if n_drinks >= 5:
        money *= 0.75
elif drink == "Cappuccino":
    if sugar_yes_no == "Without":
        money += 1 * 0.65
    elif sugar_yes_no == "Normal":
        money += 1.20
    elif sugar_yes_no == "Extra":
        money += 1.60
elif drink == "Tea":
    if sugar_yes_no == "Without":
        money += 0.50 * 0.65
    elif sugar_yes_no == "Normal":
        money += 0.60
    elif sugar_yes_no == "Extra":
        money += 0.70
total_money = money * n_drinks
if total_money > 15:
    total_money *= 0.80
print(f"You bought {n_drinks} cups of {drink} for {total_money:.2f} lv.")