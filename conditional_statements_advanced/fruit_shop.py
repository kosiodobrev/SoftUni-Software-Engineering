fruit = input()
week_day = input()
quantity = float(input())

price_fruit = 0

if week_day == "Monday" or week_day == "Tuesday" or week_day == "Wednesday" or week_day == "Thursday" or week_day == "Friday":
    if fruit == "banana":
        price_fruit += 2.50 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "apple":
        price_fruit += 1.20 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "orange":
        price_fruit += 0.85 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "grapefruit":
        price_fruit += 1.45 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "kiwi":
        price_fruit += 2.70 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "pineapple":
        price_fruit += 5.50 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "grapes":
        price_fruit += 3.85 * quantity
        print(f"{price_fruit:.2f}")
    else:
        print("error")
elif week_day == "Saturday" or week_day == "Sunday":
    if fruit == "banana":
        price_fruit += 2.70 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "apple":
        price_fruit += 1.25 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "orange":
        price_fruit += 0.90 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "grapefruit":
        price_fruit += 1.60 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "kiwi":
        price_fruit += 3 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "pineapple":
        price_fruit += 5.60 * quantity
        print(f"{price_fruit:.2f}")
    elif fruit == "grapes":
        price_fruit += 4.20 * quantity
        print(f"{price_fruit:.2f}")
    else:
        print("error")
else:
    print("error")

