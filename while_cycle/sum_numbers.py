number = int(input())
sum_other_numbers = 0

while True:
    current_number = int(input())
    sum_other_numbers += current_number
    if sum_other_numbers >= number:
        print(sum_other_numbers)
        break