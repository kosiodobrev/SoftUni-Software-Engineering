def sequence_function(elements):
    elements = [int(num) for num in elements]
    minimum_number = min(elements)
    maximum_number = max(elements)
    sum_all_number = 0
    for num in elements:
        sum_all_number += num
    return f"The minimum number is {minimum_number}\nThe maximum number is {maximum_number}\nThe sum number is: {sum_all_number}"



sequence = input().split()
print(sequence_function(sequence))