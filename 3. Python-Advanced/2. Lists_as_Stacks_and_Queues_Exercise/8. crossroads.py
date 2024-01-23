from collections import deque

green_light = int(input())
free_window = int(input())
command = input()
green_light_cycle = False
current_car = deque()


while command != "End":
    if command == "green":
        green_light_copy, cycle_copy = green_light, free_window
        green_light_cycle = True
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



