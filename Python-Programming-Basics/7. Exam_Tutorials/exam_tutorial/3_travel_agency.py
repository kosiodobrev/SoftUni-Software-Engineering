city_name = input()
packet_type = input()
vip = input()
staying_days = int(input())
price = 0
if staying_days < 1:
    print("Days must be a positive number!")
if city_name == "Bansko" or city_name == "Borovets":
    if packet_type == "withEquipment":
        price = 100
        if vip == "yes":
            price *= 0.90
    elif packet_type == "noEquipment":
        price = 80
        if vip == "yes":
            price *= 0.95
elif city_name == "Varna":
    if packet_type == "withBreakfast":
        price = 130
        if vip == "yes":
            price *= 0.88
    elif packet_type == "noBreakfast":
        price = 100
        if vip == "yes":
            price *= 0.93
else:
    print("Invalid input!")
total_price = staying_days * price
if staying_days > 7:
    total_price = total_price - (price / staying_days)