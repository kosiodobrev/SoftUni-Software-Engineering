number = int(input())
even_sum = 0
odd_sum = 0
for i in range(1, number + 1):
    current_number = int(input())
    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number
difference = abs(even_sum - odd_sum)
if difference == 0:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {difference}")