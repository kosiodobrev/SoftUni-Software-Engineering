from collections import deque
green_light = int(input())
free_windows = int(input())
command = input()
green_light_cycle = True
waiting_cars = deque([])
passed_cars = 0
all_passed = True

while command != "END":
    if command != "green":
        waiting_cars.append(command)
    elif command == "green":
        green_light_cycle = True
        green_light_copy = green_light
        free_windows_copy = free_windows
        remaining_time = green_light_copy + free_windows_copy
        while green_light_copy:
            if waiting_cars:
                current_car = waiting_cars.popleft()
                car_copy = current_car
                if len(car_copy) <= green_light_copy:
                    green_light_copy -= len(current_car)
                    passed_cars += 1
                else:
                    car_copy = car_copy[green_light_copy:]
                    green_light_copy = 0
                    if len(car_copy) > free_windows_copy:
                        car_copy = car_copy[free_windows_copy:]
                        print("A crash happened!")
                        print(''.join(current_car), f"was hit at {car_copy[0]}.")
                        exit()
                    else:
                        passed_cars += 1
            else:
                green_light_copy = 0
    command = input()

if all_passed:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
