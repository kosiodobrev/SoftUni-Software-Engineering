initial_list = input().split(" ")
while True:
    command = input().split()

    if command[0] == "end":
        break

    if command[0] == "exchange":
        index = int(command[1])
        if 0 <= index < len(initial_list):
            initial_list = initial_list[index + 1:] + initial_list[:index + 1]
        else:
            print("Invalid index")

    if command[0] == "max":
        if command[1] == "even":
            initial_list_int = [int(num) for num in initial_list]
            max_even_number = max((num for num in initial_list_int if num % 2 == 0), default=None)
            print(initial_list_int.index(max_even_number))
        elif command[1] == "odd":
            initial_list_int = [int(num) for num in initial_list]
            max_odd_number = max((num for num in initial_list_int if num % 2 != 0), default=None)
            print(initial_list_int.index(max_odd_number))

    if command[0] == "min":
        if command[1] == "even":
            initial_list_int = [int(num) for num in initial_list]
            min_even_number = min((num for num in initial_list_int if num % 2 == 0), default=None)
            print(initial_list_int.index(min_even_number))
        elif command[1] == "odd":
            initial_list_int = [int(num) for num in initial_list]
            min_odd_number = min((num for num in initial_list_int if num % 2 != 0), default=None)
            print(initial_list_int.index(min_odd_number))


