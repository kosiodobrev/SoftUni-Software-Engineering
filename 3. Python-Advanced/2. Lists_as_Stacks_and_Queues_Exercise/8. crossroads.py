from collections import deque

green_light = int(input())
free_window = int(input())
command = input()
all_passed = True
current_car = deque()
passed_cars = 0


while command != "End":
    if command == "green":
        green_light_copy, cycle_copy = green_light, free_window
        while green_light_copy:
            if current_car:

        current_green_light = green_light
    else:
        current_car = deque(command)

    for i in range(green_light):
        if current_car:
            current_car.popleft()
            current_green_light -= 1
        else:
            break

    command = input()



