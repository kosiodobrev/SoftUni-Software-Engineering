from collections import deque

petrol_pumps = int(input())
pumps = deque()

for _ in range(petrol_pumps):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])

start_position = 0
stops = 0

while stops < petrol_pumps:
    fuel = 0
    for i in range(petrol_pumps):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1
print(start_position)
