n = int(input())

matrix = []

for row in range(n):
    matrix_data = list(input())
    matrix.append(matrix_data)

symbol = input()
position = None

for row_index in range(n):
    if position:
        break
    for col_index in range(n):
        if matrix[row_index][col_index] == symbol:
            position = (row_index, col_index)
            break

if position is not None:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")
