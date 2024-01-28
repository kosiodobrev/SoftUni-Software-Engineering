row = int(input())

matrix = []

for _ in range(row):
    data = [int(x) for x in input().split()]
    matrix.append(data)

sum_number = 0

for row_index in range(row):
    sum_number += matrix[row_index][row_index]
print(sum_number)

