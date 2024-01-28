row = int(input())

matrix = []
for i in range(row):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)


flatten = []
for row in matrix:
    for el in row:
        flatten.append(el)

print(flatten)
