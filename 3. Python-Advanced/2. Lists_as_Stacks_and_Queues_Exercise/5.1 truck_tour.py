from collections import deque

petrol_pumps = int(input())
all_pumps = deque()
position = 0
needed_distance = 0
stops = 0

for _ in range(petrol_pumps):
    amount_of_petrol, distance = [int(x) for x in input().split()]
    all_pumps.append([amount_of_petrol, distance])

while stops < petrol_pumps:
    fuel = 0
    for i in range(petrol_pumps):
        fuel += all_pumps[i][0]
        needed_distance = all_pumps[i][1]
        if fuel < needed_distance:
            stops = 0
            position += 1
            all_pumps.rotate(-1)
            break
        fuel -= needed_distance
        stops += 1
print(position)
