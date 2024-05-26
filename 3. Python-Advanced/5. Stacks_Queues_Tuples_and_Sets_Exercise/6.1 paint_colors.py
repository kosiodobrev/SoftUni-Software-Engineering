from collections import deque

color_string = deque(input().split())

main_colors = ['red', 'blue', 'yellow']
secondary_colors = {'orange': ["red", "yellow"],
                    "purple": ['red', 'blue'],
                    "green": ["blue", "yellow"]}
collected_colors = []

while color_string:
    first_string = color_string.popleft()
    last_string = color_string.pop() if color_string else ""
    for color in (first_string + last_string, last_string + first_string):
        if color in main_colors or color in secondary_colors:
            collected_colors.append(color)
            break
    else:
        if len(first_string) > 1:
            color_string.insert(len(color_string) // 2, first_string[:-1])
        if len(last_string) > 1:
            color_string.insert(len(color_string) // 2, last_string[:-1])

for color in collected_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)

