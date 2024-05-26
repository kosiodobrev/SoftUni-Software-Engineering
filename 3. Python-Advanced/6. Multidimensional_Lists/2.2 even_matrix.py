row_num = int(input())

matrix = []

for i in range(row_num):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)
