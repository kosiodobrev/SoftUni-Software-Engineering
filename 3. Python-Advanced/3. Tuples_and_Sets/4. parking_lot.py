n_commands = int(input())

car_dict = []

for i in range(n_commands):
    direction, car_number = input().split(", ")
    if car_number not in car_dict:
        if direction == "IN":
            car_dict.append(car_number)
    elif car_number in car_dict:
        if direction == "OUT":
            car_dict.remove(car_number)

if car_dict:
    for i in car_dict:
        print(i)
else:
    print("Parking Lot is Empty")
