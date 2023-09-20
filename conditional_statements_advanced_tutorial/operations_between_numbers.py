number_one = int(input())
number_two = int(input())
operator = input()
result = 0
is_even = ""
if operator == "+":
    result = number_one + number_two
    if result % 2 == 0:
        is_even = "even"
    else:
        is_even = "odd"
    print(f"{number_one} {operator} {number_two} = {result} - {is_even}")
elif operator == "-":
    result = number_one - number_two
    if result % 2 == 0:
        is_even = "even"
    else:
        is_even = "odd"
    print(f"{number_one} {operator} {number_two} = {result} - {is_even}")
elif operator == "*":
    result = number_one * number_two
    if result % 2 == 0:
        is_even = "even"
    else:
        is_even = "odd"
    print(f"{number_one} {operator} {number_two} = {result} - {is_even}")
elif operator == "/":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one / number_two
        print(f"{number_one} {operator} {number_two} = {result:.2f}")
elif operator == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one % number_two
        print(f"{number_one} {operator} {number_two} = {result}")
