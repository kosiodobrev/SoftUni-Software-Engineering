def sorting_function(elements):
    elements = [int(num) for num in elements]
    sorted_list = sorted(elements)
    return sorted_list



numbers = input().split(" ")
print(sorting_function(numbers))
