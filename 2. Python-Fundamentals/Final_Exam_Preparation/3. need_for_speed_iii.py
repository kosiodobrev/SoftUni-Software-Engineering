n = int(input())
my_dict = {}
for current_car in range(n):
    car, mileage, fuel = input().split("|")
    if car not in my_dict:
        my_dict[car] = [int(mileage), int(fuel)]

command = input()

while command != "Stop":
    if "Drive" in command:
        new_cmd = command.split(" : ")
        if not my_dict[new_cmd[1]][1] < int(new_cmd[3]):
            my_dict[new_cmd[1]][1] -= int(new_cmd[3])    #fuel
            my_dict[new_cmd[1]][0] += int(new_cmd[2])    #distance
            print(f"{new_cmd[1]} driven for {int(new_cmd[2])} kilometers. {int(new_cmd[3])} liters of fuel consumed.")
            if my_dict[new_cmd[1]][0] >= 100000:
                my_dict.pop(new_cmd[1])
                print(f"Time to sell the {new_cmd[1]}!")
        else:
            print(f"Not enough fuel to make that ride")

    elif "Refuel" in command:
        new_cmd = command.split(" : ")
        if my_dict[new_cmd[1]][1] + int(new_cmd[2]) > 75:
            diff = 75 - my_dict[new_cmd[1]][1]
            print(f"{new_cmd[1]} refueled with {diff} liters")
            my_dict[new_cmd[1]][1] = 75
        else:
            my_dict[new_cmd[1]][1] += int(new_cmd[2])
            print(f"{new_cmd[1]} refueled with {new_cmd[2]} liters")

    elif "Revert" in command:
        new_cmd = command.split(" : ")
        if my_dict[new_cmd[1]][0] - int(new_cmd[2]) < 10000:
            my_dict[new_cmd[1]][0] = 10000
        else:
            my_dict[new_cmd[1]][0] -= int(new_cmd[2])
            print(f"{new_cmd[1]} mileage decreased by {new_cmd[2]} kilometers")

    command = input()

for key, value in my_dict.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
