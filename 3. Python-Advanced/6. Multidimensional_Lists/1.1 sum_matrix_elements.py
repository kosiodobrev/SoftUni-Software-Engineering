data = input().split(", ")
row_number, col_number = int(data[0]), int(data[1])

matrix = []
sum_nums = 0

for row in range(row_number):
    data_row = input().split(", ")
    row_numbers = []
    for index in range(len(data_row)):
        current_element = int(data_row[index])
        sum_nums += current_element
        row_numbers.append(int(data_row[index]))
    matrix.append(row_numbers)
print(sum_nums)
print(matrix)
