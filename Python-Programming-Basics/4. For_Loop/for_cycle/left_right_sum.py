number = int(input())
total_sum_1 = 0
total_sum_2 = 0
for _ in range(number):
    current_number = int(input())
    total_sum_1 += current_number
for _ in range(number):
    current_number = int(input())
    total_sum_2 += current_number
difference = abs(total_sum_1 - total_sum_2)
if difference == 0:
    print(f"Yes, sum = {total_sum_1}")
else:
    print(f"No, diff = {difference}")