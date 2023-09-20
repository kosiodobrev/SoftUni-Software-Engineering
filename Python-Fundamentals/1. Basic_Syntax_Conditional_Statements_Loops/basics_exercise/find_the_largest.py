number = input()
sorted_number = sorted(number, reverse=True)
largest_number = int("".join(sorted_number))
print(largest_number)
