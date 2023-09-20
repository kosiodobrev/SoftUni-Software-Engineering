type_fuel = str(input())
current_liters = float(input())

type_fuel = type_fuel.lower()

if type_fuel == "diesel" or type_fuel == "gasoline" or type_fuel == "gas":
    if current_liters >= 25:
        print(f"You have enough {type_fuel}.")
    else:
        print(f"Fill your tank with {type_fuel}!")
else:
    print("Invalid fuel!")