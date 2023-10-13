from math import floor

def center_point(x1, y1, x2, y2):
    first_distance = abs(x1) + abs(y1)
    second_distance = abs(x2) + abs(y2)

    if first_distance >= second_distance:
        return f"({floor(x2)}, {floor(y2)})"
    else:
        return f"({floor(x1)}, {floor(y1)})"


first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())

print(center_point(first_x, first_y, second_x, second_y))