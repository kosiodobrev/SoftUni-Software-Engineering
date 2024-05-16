numbers = [float(x) for x in input().split()]

same_values = {}

for i in numbers:
    if i not in same_values:
        same_values[i] = 1
    else:
        same_values[i] += 1

for key, value in same_values.items():
    print(f"{key} - {value} times")
