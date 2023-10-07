
def rounding_numbers(given_numbers):
    result_list = []
    given_numbers_float = [float(num) for num in given_numbers]
    for i in given_numbers_float:
        rounded_number = round(i)
        result_list.append(rounded_number)
    return result_list


given_numbers = input().split()
print(rounding_numbers(given_numbers))


