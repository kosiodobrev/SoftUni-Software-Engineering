n = int(input())

matrix = []
sum_diagonal = 0

for row in range(n):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)
for col in range(n):
    sum_diagonal += matrix[col][col]

print(sum_diagonal)
