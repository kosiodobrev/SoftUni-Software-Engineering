clothes_boxes = [int(x) for x in input().split()]
capacity = int(input())

total_racks = 0

while clothes_boxes:
    total_racks += 1
    current_rack_capacity = capacity
    while clothes_boxes and clothes_boxes[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_boxes.pop()

print(total_racks)

