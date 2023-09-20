type_fuel = str(input())
liters_fuel = float(input())
club_card = str(input())

end_price = 0

if type_fuel == "Gasoline" or type_fuel == "Diesel" or type_fuel == "Gas":
    if type_fuel == "Gasoline":
        end_price = liters_fuel * 2.22
    if type_fuel == "Diesel":
        end_price = liters_fuel * 2.33
    if type_fuel == "Gas":
        end_price = liters_fuel * 0.93

    if club_card == "Yes" and type_fuel == "Gasoline":
        end_price -= liters_fuel * 0.18
    if club_card == "Yes" and type_fuel == "Diesel":
        end_price -= liters_fuel * 0.12
    if club_card == "Yes" and type_fuel == "Gas":
        end_price -= liters_fuel * 0.08

    if 20 <= liters_fuel <= 25:
        end_price *= 0.92
    elif liters_fuel > 25:
        end_price *= 0.90
print(f"{end_price:.2f} lv.")