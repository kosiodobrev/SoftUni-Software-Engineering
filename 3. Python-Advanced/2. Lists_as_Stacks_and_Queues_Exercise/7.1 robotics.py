from collections import deque
from datetime import datetime, timedelta

name_of_robots = input().split(";")
starting_time = input()
products = deque()

robots = {}

for r in name_of_robots:
    name, process_time = r.split("-")
    robots[name] = [int(process_time), 0]

factory_time = datetime.strptime(starting_time, "%H:%M:%S")

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1

        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f"{robot_name} - {product} {factory_time.strftime('[%H:%M:%S]')}")

