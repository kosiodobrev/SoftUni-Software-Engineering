rows = int(input())

matrix = []

for i in range(rows):
    rows = [int(el) for el in input().split(", ")]
    matrix.append(rows)

flattened = []

for row in matrix:
    for el in row:
        flattened.append(el)

print(flattened)
