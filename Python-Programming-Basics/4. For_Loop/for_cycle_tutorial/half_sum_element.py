import sys
number = int(input())
sum_all_elements = 0
max_element = -sys.maxsize
for _ in range(number):
    current_number = int(input())
    sum_all_elements += current_number
    if current_number > max_element:
        max_element = current_number
difference = abs(max_element - (sum_all_elements - max_element))
if max_element == sum_all_elements - max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    print("No")
    print(f"Diff = {difference}")