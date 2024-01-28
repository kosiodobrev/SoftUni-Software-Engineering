rows, columns = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    row_nums = [int(el) for el in input().split()]
    matrix.append(row_nums)

for col_index in range(columns):
    col_total = 0
    for row_index in range(rows):
        col_total += matrix[row_index][col_index]
    print(col_total)
