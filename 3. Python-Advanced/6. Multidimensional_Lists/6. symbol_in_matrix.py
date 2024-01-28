rows = int(input())

matrix = []
result = []

for _ in range(rows):
    data = [x for x in input()]
    matrix.append(data)

symbol = input()
row_counter = 0
col_counter = 0

for row_index in matrix:
    for col_index in row_index:
        if col_index == symbol:
            result.append(col_index)
            break
        col_counter += 1
    if result:
        break
    row_counter += 1
    col_counter = 0

if result:
    print(f"({row_counter}, {col_counter})")
else:
    print(f"{symbol} does not occur in the matrix")



